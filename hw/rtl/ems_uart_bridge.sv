// ems_uart_bridge.sv -- host command protocol over UART (all fields little-endian).
//
//   'W' addr[2] data[8]            single cfg write            -> 'k'
//   'B' addr[2] count[2] data[8]*n burst cfg write (addr++)    -> 'k'
//   'F' x[4]*N_FEAT                load a trial into the on-chip feature buffer,
//                                  run it once                 -> result packet
//   'T' runs[2]                    re-run the buffered trial `runs` times
//                                  back-to-back (throughput)   -> result packet
//
// Result packet (72 bytes):
//   'R' class[1] prob[4]*3 fam_prob[4]*12 lat_cycles[4] total_cycles[4] runs[2]
// lat_cycles   : core compute latency of the last run (first feature -> result)
// total_cycles : first feature of run 1 -> result of the last run
//
// Features are buffered first and then streamed at one per cycle, so the
// on-chip counters measure compute only, never UART time.
module ems_uart_bridge
  import ems_pkg::*;
  import ems_params_pkg::*;
(
  input  logic                  clk,
  input  logic                  rst_n,
  // uart
  input  logic                  rx_valid,
  input  logic [7:0]            rx_data,
  output logic                  tx_start,
  output logic [7:0]            tx_data,
  input  logic                  tx_busy,
  // core
  output logic                  cfg_we,
  output logic [15:0]           cfg_addr,
  output logic [63:0]           cfg_wdata,
  output logic                  s_valid,
  input  logic                  s_ready,
  output logic signed [X_W-1:0] s_data,
  input  logic                  m_valid,
  output logic                  m_ready,
  input  logic [1:0]            m_class,
  input  logic [P_W-1:0]        m_prob     [3],
  input  logic [P_W-1:0]        m_fam_prob [12],
  input  logic [31:0]           m_lat_cycles,
  output logic                  busy
);
  localparam int AW = $clog2(N_FEAT);
  localparam int PKT_BYTES = 72;

  typedef enum logic [3:0] {
    CMD, W_ARGS, B_HDR, B_DATA, F_DATA, T_ARGS, PRIME, RUN, SEND, ACK
  } st_t;
  st_t st;

  /* verilator lint_off UNUSEDSIGNAL */
  logic [79:0] sh;          // byte shift register (new bytes enter at the top)
  /* verilator lint_on UNUSEDSIGNAL */
  logic [3:0]  nb;          // bytes collected for the current field group
  logic [15:0] b_addr, b_left, runs, results;
  logic [AW-1:0] widx;      // feature buffer write index

  // result packet
  logic [PKT_BYTES*8-1:0] pkt;
  logic [6:0]             pkt_i;
  logic [31:0]            total_cyc;
  logic                   counting;

  // ───────── feature buffer ─────────
  logic          fb_we;
  logic [AW-1:0] ridx, ridx_next;
  logic [31:0]   fb_q;
  wire accept = s_valid && s_ready;
  always_comb ridx_next = (st == PRIME) ? '0 : !accept ? ridx
                       : (ridx == AW'(N_FEAT - 1)) ? '0 : ridx + 1'b1;

  ems_sdp_ram #(.WIDTH(32), .DEPTH(1 << AW)) u_fbuf (
    .clk, .we(fb_we), .waddr(widx), .wdata(sh[79:48]), .raddr(ridx_next), .rdata(fb_q));

  assign s_data  = fb_q;
  assign m_ready = 1'b1;
  assign busy    = (st != CMD);

  logic [15:0] sent;        // trials fully streamed in this run batch
  assign s_valid = (st == RUN) && (sent != runs);

  always_ff @(posedge clk or negedge rst_n) begin
    if (!rst_n) begin
      st <= CMD; sh <= '0; nb <= '0; b_addr <= '0; b_left <= '0; runs <= '0;
      results <= '0; widx <= '0; ridx <= '0; sent <= '0;
      cfg_we <= 1'b0; cfg_addr <= '0; cfg_wdata <= '0; fb_we <= 1'b0;
      tx_start <= 1'b0; tx_data <= '0; pkt <= '0; pkt_i <= '0;
      total_cyc <= '0; counting <= 1'b0;
    end else begin
      cfg_we <= 1'b0; fb_we <= 1'b0; tx_start <= 1'b0;
      if (rx_valid) sh <= {rx_data, sh[79:8]};
      if (counting) total_cyc <= total_cyc + 32'd1;

      unique case (st)
        CMD: if (rx_valid) begin
          nb <= '0;
          unique case (rx_data)
            8'h57: st <= W_ARGS;                          // 'W'
            8'h42: st <= B_HDR;                           // 'B'
            8'h46: begin st <= F_DATA; widx <= '0; end    // 'F'
            8'h54: st <= T_ARGS;                          // 'T'
            default: ;
          endcase
        end
        W_ARGS: if (rx_valid) begin
          if (nb == 4'd9) begin
            cfg_we <= 1'b1;
            cfg_addr <= sh[23:8];                         // bytes 0-1 (after this shift)
            cfg_wdata <= {rx_data, sh[79:24]};            // bytes 2-9
            st <= ACK;
          end
          nb <= nb + 4'd1;
        end
        B_HDR: if (rx_valid) begin
          if (nb == 4'd3) begin
            b_addr <= sh[71:56];                          // bytes 0-1 (3 shifts in)
            b_left <= {rx_data, sh[79:72]};
            nb <= '0;
            st <= ({rx_data, sh[79:72]} == 16'd0) ? ACK : B_DATA;
          end else nb <= nb + 4'd1;
        end
        B_DATA: if (rx_valid) begin
          if (nb == 4'd7) begin
            cfg_we <= 1'b1; cfg_addr <= b_addr; cfg_wdata <= {rx_data, sh[79:24]};
            b_addr <= b_addr + 16'd1; b_left <= b_left - 16'd1;
            nb <= '0;
            if (b_left == 16'd1) st <= ACK;
          end else nb <= nb + 4'd1;
        end
        F_DATA: begin
          if (rx_valid) begin
            if (nb == 4'd3) begin
              fb_we <= 1'b1;                              // writes sh[79:48] next cycle
              nb <= '0;
            end else nb <= nb + 4'd1;
          end
          if (fb_we) begin
            if (widx == AW'(N_FEAT - 1)) begin runs <= 16'd1; st <= PRIME; end
            widx <= widx + 1'b1;
          end
        end
        T_ARGS: if (rx_valid) begin
          if (nb == 4'd1) begin
            runs <= ({rx_data, sh[79:72]} == 16'd0) ? 16'd1 : {rx_data, sh[79:72]};
            st <= PRIME;
          end else nb <= nb + 4'd1;
        end
        PRIME: begin                                      // ridx=0 -> fb_q valid next cycle
          ridx <= '0; sent <= '0; results <= '0;
          total_cyc <= '0; counting <= 1'b1;
          st <= RUN;
        end
        RUN: begin
          ridx <= ridx_next;
          if (accept && ridx == AW'(N_FEAT - 1)) sent <= sent + 16'd1;
          if (m_valid) begin
            results <= results + 16'd1;
            if (results + 16'd1 == runs) begin
              counting <= 1'b0;
              pkt <= {runs, total_cyc, m_lat_cycles,
                      15'd0, m_fam_prob[11], 15'd0, m_fam_prob[10], 15'd0, m_fam_prob[9],
                      15'd0, m_fam_prob[8],  15'd0, m_fam_prob[7],  15'd0, m_fam_prob[6],
                      15'd0, m_fam_prob[5],  15'd0, m_fam_prob[4],  15'd0, m_fam_prob[3],
                      15'd0, m_fam_prob[2],  15'd0, m_fam_prob[1],  15'd0, m_fam_prob[0],
                      15'd0, m_prob[2], 15'd0, m_prob[1], 15'd0, m_prob[0],
                      6'd0, m_class, 8'h52};
              pkt_i <= '0;
              st <= SEND;
            end
          end
        end
        SEND: if (!tx_busy && !tx_start) begin
          tx_data <= pkt[7:0];
          pkt <= pkt >> 8;
          tx_start <= 1'b1;
          pkt_i <= pkt_i + 7'd1;
          if (pkt_i == 7'(PKT_BYTES - 1)) st <= CMD;
        end
        ACK: if (!tx_busy && !tx_start) begin
          tx_data <= 8'h6b;                               // 'k'
          tx_start <= 1'b1;
          st <= CMD;
        end
        default: st <= CMD;
      endcase
    end
  end
endmodule
