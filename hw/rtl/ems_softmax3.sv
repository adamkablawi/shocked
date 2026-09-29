// ems_softmax3.sv -- 3-way softmax on Q.16 logits -> Q0.16 probabilities.
//
//   d_j = min(max - lg_j, 32.0)          (>= 0)
//   t_j = (d_j * log2(e)) >> 16          Q.16
//   e_j = EXP_LUT[t_j frac] >> int(t_j)  (0 if int(t_j) >= 18)
//   p_j = floor(e_j * 2^16 / (e0+e1+e2)) (exact restoring division)
//
// Sequential: ~70 cycles per call. Bit-exact with fxp.softmax3_q.
module ems_softmax3
  import ems_pkg::*;
#(
  parameter string EXP_FILE = "exp_lut.mem"
) (
  input  logic                   clk,
  input  logic                   rst_n,
  input  logic                   start,     // accepted when !busy
  input  logic signed [L_W-1:0]  lg [3],
  output logic                   busy,
  output logic                   done,      // 1-cycle pulse, p valid from then on
  output logic        [P_W-1:0]  p  [3]
);
  typedef enum logic [2:0] {IDLE, MAX, DIFF, TMUL, LUT_A, LUT_D, SUM, DIV} state_t;
  state_t state;

  logic signed [L_W-1:0]    lg_r [3];
  logic        [DIFF_W-1:0] d    [3];
  logic        [DIFF_W-1:0] t    [3];   // Q.16, < 2^22
  logic        [E_W-1:0]    e    [3];
  logic        [E_W+1:0]    ssum;       // <= 3 * 2^17
  logic        [1:0]        j;

  // exp LUT (block/distributed ROM, registered read)
  logic [EXP_IDX_W-1:0] rom_addr;
  logic [E_W-1:0]       rom_q;
  ems_sdp_ram #(.WIDTH(E_W), .DEPTH(1 << EXP_IDX_W), .INIT_FILE(EXP_FILE)) u_exp (
    .clk, .we(1'b0), .waddr('0), .wdata('0), .raddr(rom_addr), .rdata(rom_q));

  // max of the three logits (registered in MAX, used in DIFF)
  logic signed [L_W-1:0] mx, mx_c;
  always_comb begin
    mx_c = lg_r[0];
    if (lg_r[1] > mx_c) mx_c = lg_r[1];
    if (lg_r[2] > mx_c) mx_c = lg_r[2];
  end

  // restoring divider: q = floor((e_j << 16) / ssum), 17 quotient bits
  logic [E_W+1:0]  rem;       // < ssum
  logic [16:0]     num_lo;    // remaining low numerator bits (MSB first)
  logic [P_W-1:0]  q;
  logic [4:0]      bitn;
  logic [E_W+2:0]  rem_sh;
  assign rem_sh = {rem, num_lo[16]};

  assign busy = (state != IDLE);

  always_ff @(posedge clk or negedge rst_n) begin
    if (!rst_n) begin
      state <= IDLE; done <= 1'b0; j <= '0; bitn <= '0;
      rom_addr <= '0; ssum <= '0; rem <= '0; num_lo <= '0; q <= '0; mx <= '0;
      for (int k = 0; k < 3; k++) begin
        lg_r[k] <= '0; d[k] <= '0; t[k] <= '0; e[k] <= '0; p[k] <= '0;
      end
    end else begin
      done <= 1'b0;
      unique case (state)
        IDLE: if (start) begin
          for (int k = 0; k < 3; k++) lg_r[k] <= lg[k];
          state <= MAX;
        end
        MAX: begin
          mx <= mx_c;
          state <= DIFF;
        end
        DIFF: begin
          for (int k = 0; k < 3; k++) begin
            logic signed [L_W:0] df;
            df = {mx[L_W-1], mx} - {lg_r[k][L_W-1], lg_r[k]};
            d[k] <= (df >= (L_W+1)'(DIFF_CLAMP)) ? DIFF_W'(DIFF_CLAMP) : DIFF_W'(df);
          end
          state <= TMUL;
        end
        TMUL: begin
          for (int k = 0; k < 3; k++) begin
            logic [DIFF_W+16:0] prod;
            prod = d[k] * 17'(LOG2E_Q16);
            t[k] <= DIFF_W'(prod >> 16);
          end
          j <= '0;
          state <= LUT_A;
        end
        LUT_A: begin
          rom_addr <= t[j][15 -: EXP_IDX_W];
          state <= LUT_D;
        end
        LUT_D: begin
          // rom_q valid one cycle after rom_addr was registered
          state <= LUT_D;
          if (bitn == 5'd1) begin
            e[j] <= (t[j][DIFF_W-1:16] >= 18) ? '0 : (rom_q >> t[j][20:16]);
            bitn <= '0;
            if (j == 2'd2) state <= SUM;
            else begin j <= j + 2'd1; state <= LUT_A; end
          end else bitn <= bitn + 5'd1;
        end
        SUM: begin
          ssum <= (E_W+2)'(e[0]) + (E_W+2)'(e[1]) + (E_W+2)'(e[2]);
          j <= '0;
          rem <= '0; num_lo <= '0; q <= '0; bitn <= 5'd18;   // 18 = load
          state <= DIV;
        end
        DIV: begin
          if (bitn == 5'd18) begin
            // numerator = e_j << 16 : top part e_j >> 1 (< ssum), low 17 bits
            rem    <= (E_W+2)'(e[j] >> 1);
            num_lo <= {e[j][0], 16'b0};
            q      <= '0;
            bitn   <= 5'd17;
          end else if (bitn != 0) begin
            if (rem_sh >= {1'b0, ssum}) begin
              rem <= (E_W+2)'(rem_sh - {1'b0, ssum});
              q   <= {q[P_W-2:0], 1'b1};
            end else begin
              rem <= rem_sh[E_W+1:0];
              q   <= {q[P_W-2:0], 1'b0};
            end
            num_lo <= {num_lo[15:0], 1'b0};
            bitn   <= bitn - 5'd1;
          end else begin
            p[j] <= q;
            if (j == 2'd2) begin
              done  <= 1'b1;
              state <= IDLE;
            end else begin
              j    <= j + 2'd1;
              bitn <= 5'd18;
            end
          end
        end
        default: state <= IDLE;
      endcase
    end
  end
endmodule
