// ems_classifier.sv -- FourConnModel stacking classifier core.
//
// Features stream in (one per cycle max) in family order erp, bp, tf, conn:
//   z_k   = sat((x_k - mu_k) * m_k >>r s_k)            per-subject normalisation
//   lg_f  = (sum_k z_k * w'_k >>r 13) + b'_f            one 3-class LDA per family
//   p_f   = softmax3(lg_f)                              shared softmax unit
//   mlg   = (sum p * c >>r 15) + mb                     logistic meta-learner
//   class = argmax(mlg), probs = softmax3(mlg)
//
// All parameters (calibration, weights, biases, meta) are writable through the
// cfg port; weights/biases/meta power up with the exported FourConnModel.
// Bit-exact with hw/scripts/fxp.py:infer_q.
module ems_classifier
  import ems_pkg::*;
  import ems_params_pkg::*;
#(
  parameter string WEIGHTS_FILE = "weights.mem",
  parameter string EXP_FILE     = "exp_lut.mem"
) (
  input  logic                   clk,
  input  logic                   rst_n,

  // configuration write port (use between trials)
  input  logic                   cfg_we,
  input  logic [15:0]            cfg_addr,
  /* verilator lint_off UNUSEDSIGNAL */
  input  logic [63:0]            cfg_wdata,   // upper bits unused by narrow targets
  /* verilator lint_on UNUSEDSIGNAL */

  // feature stream in (x, Q13.19)
  input  logic                   s_valid,
  output logic                   s_ready,
  input  logic signed [X_W-1:0]  s_data,

  // result out (held until m_ready)
  output logic                   m_valid,
  input  logic                   m_ready,
  output logic [1:0]             m_class,
  output logic [P_W-1:0]         m_prob     [3],
  output logic [P_W-1:0]         m_fam_prob [12],
  output logic [31:0]            m_lat_cycles   // first feature accepted -> m_valid
);
  localparam int AW = $clog2(N_FEAT);
  localparam int CAL_W = S_W + M_W + X_W;   // 55
  localparam int WROW_W = 3 * WT_W;         // 54

  // ─────────────────────────── configuration ───────────────────────────
  logic signed [L_W-1:0] bias [N_FAM][3];
  logic signed [C_W-1:0] mc   [3][12];
  logic signed [L_W-1:0] mb   [3];

  wire cal_we = cfg_we && (cfg_addr[15:11] == ADDR_CALIB[15:11]);
  wire wt_we  = cfg_we && (cfg_addr[15:11] == ADDR_W[15:11]);

  always_ff @(posedge clk or negedge rst_n) begin
    if (!rst_n) begin
      bias <= BIAS_INIT; mc <= MC_INIT; mb <= MB_INIT;
    end else if (cfg_we) begin
      for (int f = 0; f < N_FAM; f++)
        for (int j = 0; j < 3; j++)
          if (cfg_addr == ADDR_BIAS + 16'(f * 3 + j)) bias[f][j] <= cfg_wdata[L_W-1:0];
      for (int j = 0; j < 3; j++) begin
        for (int i = 0; i < 12; i++)
          if (cfg_addr == ADDR_MC + 16'(j * 12 + i)) mc[j][i] <= cfg_wdata[C_W-1:0];
        if (cfg_addr == ADDR_MB + 16'(j)) mb[j] <= cfg_wdata[L_W-1:0];
      end
    end
  end

  // ─────────────────────────── stream control ───────────────────────────
  typedef enum logic [2:0] {ST_STREAM, ST_DRAIN, ST_META, ST_MLOG, ST_MSOFT, ST_OUT} cstate_t;
  cstate_t cst;

  logic [AW-1:0] feat_idx;
  logic [1:0]    fam_idx;
  wire  accept   = s_valid && s_ready;
  wire  fam_last = (feat_idx == AW'(FAM_END[fam_idx]));
  wire  trial_last = (feat_idx == AW'(N_FEAT - 1));

  assign s_ready = (cst == ST_STREAM);

  // memories (registered read at feat_idx on accept -> data valid in stage 1)
  logic [CAL_W-1:0]  cal_q;
  logic [WROW_W-1:0] wt_q;
  ems_sdp_ram #(.WIDTH(CAL_W), .DEPTH(2048)) u_cal (
    .clk, .we(cal_we), .waddr(cfg_addr[10:0]), .wdata(cfg_wdata[CAL_W-1:0]),
    .raddr(11'(feat_idx)), .rdata(cal_q));
  ems_sdp_ram #(.WIDTH(WROW_W), .DEPTH(2048), .INIT_FILE(WEIGHTS_FILE)) u_wt (
    .clk, .we(wt_we), .waddr(cfg_addr[10:0]), .wdata(cfg_wdata[WROW_W-1:0]),
    .raddr(11'(feat_idx)), .rdata(wt_q));

  // ─────────────────────────── datapath pipeline ───────────────────────────
  // stage 1: RAM outputs valid, x registered
  logic                 v1, fl1;
  logic [1:0]           fi1;
  logic signed [X_W-1:0] x1;
  // stage 2: diff
  logic                 v2, fl2;
  logic [1:0]           fi2;
  logic signed [X_W:0]  diff2;
  logic        [M_W-1:0] m2;
  logic        [S_W-1:0] s2;
  logic [WROW_W-1:0]    w2;
  // stages 3,4: diff*m (two registers so DSP MREG/PREG can absorb them)
  logic                 v3, fl3, v4, fl4;
  logic [1:0]           fi3, fi4;
  logic signed [X_W+M_W+1:0] pm3, pm4;   // 33 x 18 signed
  logic        [S_W-1:0] s3, s4;
  logic [WROW_W-1:0]    w3, w4;
  // stage 5: z
  logic                 v5, fl5;
  logic [1:0]           fi5;
  logic signed [Z_W-1:0] z5;
  logic [WROW_W-1:0]    w5;
  // stage 6: z*w
  logic                 v6, fl6;
  logic [1:0]           fi6;
  logic signed [Z_W+WT_W-1:0] zw6 [3];
  // stage 7: accumulate
  logic signed [ACC_W-1:0] acc [3];

  localparam logic signed [X_W+M_W+1:0] PM_ONE = 1;

  // arithmetic shift right with round-half-up (matches fxp._rshift_round)
  function automatic logic signed [ACC_W:0] rshr(input logic signed [ACC_W:0] v, input int sh);
    logic signed [ACC_W:0] one;
    one = 1;
    return (v + (one <<< (sh - 1))) >>> sh;
  endfunction

  function automatic logic signed [Z_W-1:0] sat_z(input logic signed [X_W+M_W+1:0] v);
    localparam logic signed [X_W+M_W+1:0] HI = (1 <<< (Z_W - 1)) - 1;
    localparam logic signed [X_W+M_W+1:0] LO = -(1 <<< (Z_W - 1));
    return (v > HI) ? Z_W'(HI) : (v < LO) ? Z_W'(LO) : Z_W'(v);
  endfunction

  function automatic logic signed [L_W-1:0] sat_l(input logic signed [ACC_W:0] v);
    localparam logic signed [ACC_W:0] HI = (1 <<< (L_W - 1)) - 1;
    localparam logic signed [ACC_W:0] LO = -(1 <<< (L_W - 1));
    return (v > HI) ? L_W'(HI) : (v < LO) ? L_W'(LO) : L_W'(v);
  endfunction

  always_ff @(posedge clk or negedge rst_n) begin
    if (!rst_n) begin
      feat_idx <= '0; fam_idx <= '0;
      {v1, v2, v3, v4, v5, v6} <= '0;
      {fl1, fl2, fl3, fl4, fl5, fl6} <= '0;
    end else begin
      // stage 0 -> 1
      v1 <= accept; fl1 <= accept && fam_last; fi1 <= fam_idx; x1 <= s_data;
      if (accept) begin
        feat_idx <= trial_last ? '0 : feat_idx + 1'b1;
        if (fam_last) fam_idx <= trial_last ? 2'd0 : fam_idx + 2'd1;
      end
      // 1 -> 2
      v2 <= v1; fl2 <= fl1; fi2 <= fi1;
      diff2 <= {x1[X_W-1], x1} - {cal_q[X_W-1], cal_q[X_W-1:0]};
      m2 <= cal_q[X_W +: M_W];
      s2 <= cal_q[X_W+M_W +: S_W];
      w2 <= wt_q;
      // 2 -> 3 -> 4
      v3 <= v2; fl3 <= fl2; fi3 <= fi2; s3 <= s2; w3 <= w2;
      pm3 <= diff2 * $signed({1'b0, m2});
      v4 <= v3; fl4 <= fl3; fi4 <= fi3; s4 <= s3; w4 <= w3;
      pm4 <= pm3 + (PM_ONE <<< (s3 - 1'b1));        // round-half-up constant
      // 4 -> 5 : arithmetic shift, saturate
      v5 <= v4; fl5 <= fl4; fi5 <= fi4; w5 <= w4;
      z5 <= sat_z(pm4 >>> s4);
      // 5 -> 6
      v6 <= v5; fl6 <= fl5; fi6 <= fi5;
      for (int j = 0; j < 3; j++)
        zw6[j] <= z5 * $signed(w5[j*WT_W +: WT_W]);
    end
  end

  // stage 7: accumulate. At a family's last feature the final sum goes through
  // two more registered steps (round/shift, then +bias/saturate) into the job FIFO.
  logic                   job_push;
  logic [1:0]             job_fam_in;
  logic signed [L_W-1:0]  job_lg_in [3];
  logic                   fin_v, rnd_v;
  logic [1:0]             fin_fam, rnd_fam;
  logic signed [ACC_W-1:0] fin_acc [3];
  logic signed [ACC_W:0]   rnd_acc [3];

  always_ff @(posedge clk or negedge rst_n) begin
    if (!rst_n) begin
      job_push <= 1'b0; job_fam_in <= '0;
      fin_v <= 1'b0; rnd_v <= 1'b0; fin_fam <= '0; rnd_fam <= '0;
      for (int j = 0; j < 3; j++) begin
        acc[j] <= '0; job_lg_in[j] <= '0; fin_acc[j] <= '0; rnd_acc[j] <= '0;
      end
    end else begin
      fin_v <= v6 && fl6; fin_fam <= fi6;
      if (v6) begin
        for (int j = 0; j < 3; j++) begin
          logic signed [ACC_W-1:0] a;
          a = acc[j] + ACC_W'(zw6[j]);
          fin_acc[j] <= a;
          acc[j] <= fl6 ? '0 : a;
        end
      end
      rnd_v <= fin_v; rnd_fam <= fin_fam;
      for (int j = 0; j < 3; j++) rnd_acc[j] <= rshr((ACC_W+1)'(fin_acc[j]), LDA_SHIFT);
      job_push <= rnd_v; job_fam_in <= rnd_fam;
      for (int j = 0; j < 3; j++) job_lg_in[j] <= sat_l(rnd_acc[j] + (ACC_W+1)'(bias[rnd_fam][j]));
    end
  end

  // ─────────────────────────── family job FIFO (depth 4) ───────────────────────────
  logic [1:0]            fq_fam [4];
  logic signed [L_W-1:0] fq_lg  [4][3];
  logic [1:0]            fq_wp, fq_rp;
  logic [2:0]            fq_cnt;
  logic                  fq_pop;

  always_ff @(posedge clk or negedge rst_n) begin
    if (!rst_n) begin
      fq_wp <= '0; fq_rp <= '0; fq_cnt <= '0;
    end else begin
      if (job_push) begin
        fq_fam[fq_wp] <= job_fam_in;
        for (int j = 0; j < 3; j++) fq_lg[fq_wp][j] <= job_lg_in[j];
        fq_wp <= fq_wp + 2'd1;
      end
      if (fq_pop) fq_rp <= fq_rp + 2'd1;
      fq_cnt <= fq_cnt + 3'(job_push) - 3'(fq_pop);
    end
  end

  // ─────────────────────────── shared softmax ───────────────────────────
  logic                  sm_start, sm_busy, sm_done;
  logic signed [L_W-1:0] sm_lg [3];
  logic        [P_W-1:0] sm_p  [3];
  logic                  sm_is_meta;     // current softmax job is the final one
  logic [1:0]            sm_fam;
  logic signed [L_W-1:0] mlg [3];

  ems_softmax3 #(.EXP_FILE(EXP_FILE)) u_sm (
    .clk, .rst_n, .start(sm_start), .lg(sm_lg), .busy(sm_busy), .done(sm_done), .p(sm_p));

  wire sm_free = !sm_busy && !sm_start;
  assign fq_pop   = sm_free && (fq_cnt != 0) && (cst != ST_MSOFT);

  // ─────────────────────────── meta-learner + control ───────────────────────────
  logic [P_W-1:0]         fam_p [12];
  logic [2:0]             fams_done;
  logic [3:0]             mi;          // meta input index 0..11
  logic signed [ACC_W-1:0] macc [3];
  logic signed [ACC_W:0]   mrnd [3];
  logic [31:0]            lat_cnt;

  always_ff @(posedge clk or negedge rst_n) begin
    if (!rst_n) begin
      cst <= ST_STREAM; sm_start <= 1'b0; sm_is_meta <= 1'b0; sm_fam <= '0;
      fams_done <= '0; mi <= '0; m_valid <= 1'b0; m_class <= '0;
      lat_cnt <= '0; m_lat_cycles <= '0;
      for (int j = 0; j < 3; j++) begin
        sm_lg[j] <= '0; macc[j] <= '0; mrnd[j] <= '0; mlg[j] <= '0; m_prob[j] <= '0;
      end
      for (int i = 0; i < 12; i++) begin fam_p[i] <= '0; m_fam_prob[i] <= '0; end
    end else begin
      sm_start <= 1'b0;

      // latency counter: runs from the first accepted feature to m_valid
      if (accept && feat_idx == '0) lat_cnt <= 32'd1;
      else if (cst != ST_STREAM || feat_idx != '0) lat_cnt <= lat_cnt + 32'd1;

      // launch family softmax jobs
      if (fq_pop) begin
        for (int j = 0; j < 3; j++) sm_lg[j] <= fq_lg[fq_rp][j];
        sm_fam <= fq_fam[fq_rp]; sm_is_meta <= 1'b0; sm_start <= 1'b1;
      end

      // collect family probabilities
      if (sm_done && !sm_is_meta) begin
        for (int j = 0; j < 3; j++) fam_p[sm_fam * 3 + j] <= sm_p[j];
        fams_done <= fams_done + 3'd1;
      end

      unique case (cst)
        ST_STREAM: if (accept && trial_last) cst <= ST_DRAIN;
        ST_DRAIN: if (fams_done == 3'd4) begin
          fams_done <= '0; mi <= '0;
          for (int j = 0; j < 3; j++) macc[j] <= '0;
          cst <= ST_META;
        end
        ST_META: begin
          if (mi != 4'd12) begin
            for (int j = 0; j < 3; j++) begin
              logic signed [P_W+C_W:0] pc;     // s18 x s18
              pc = $signed({1'b0, fam_p[mi]}) * mc[j][mi];
              macc[j] <= macc[j] + ACC_W'(pc);
            end
            mi <= mi + 4'd1;
          end else begin
            for (int j = 0; j < 3; j++) mrnd[j] <= rshr((ACC_W+1)'(macc[j]), META_SHIFT);
            cst <= ST_MLOG;
          end
        end
        ST_MLOG: begin
          for (int j = 0; j < 3; j++) begin
            logic signed [L_W-1:0] l;
            l = sat_l(mrnd[j] + (ACC_W+1)'(mb[j]));
            mlg[j] <= l;
            sm_lg[j] <= l;
          end
          sm_is_meta <= 1'b1; sm_start <= 1'b1;
          cst <= ST_MSOFT;
        end
        ST_MSOFT: if (sm_done) begin
          m_class <= (mlg[1] > mlg[0]) ? ((mlg[2] > mlg[1]) ? 2'd2 : 2'd1)
                                       : ((mlg[2] > mlg[0]) ? 2'd2 : 2'd0);
          for (int j = 0; j < 3; j++) m_prob[j] <= sm_p[j];
          for (int i = 0; i < 12; i++) m_fam_prob[i] <= fam_p[i];
          m_lat_cycles <= lat_cnt + 32'd1;
          m_valid <= 1'b1;
          cst <= ST_OUT;
        end
        ST_OUT: if (m_ready) begin
          m_valid <= 1'b0;
          cst <= ST_STREAM;
        end
        default: cst <= ST_STREAM;
      endcase
    end
  end
endmodule
