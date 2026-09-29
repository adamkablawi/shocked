// arty_s7_top.sv -- board top for Digilent Arty S7 (XC7S50 / XC7S25).
//   CLK100MHZ -> core clock, USB-UART at 921600 baud, BTN reset (ck_rst, active low).
//   LEDs: [0] heartbeat, [1] bridge busy, [3:2] last predicted class.
module arty_s7_top #(
  parameter int    CLKS_PER_BIT = 108,             // 100e6 / 921600
  parameter string WEIGHTS_FILE = "weights.mem",
  parameter string EXP_FILE     = "exp_lut.mem"
) (
  input  logic       CLK100MHZ,
  input  logic       ck_rst,          // active-low reset button
  input  logic       uart_txd_in,     // host -> FPGA
  output logic       uart_rxd_out,    // FPGA -> host
  output logic [3:0] led
);
  import ems_pkg::*;

  logic clk;
  assign clk = CLK100MHZ;

  // reset synchroniser (async assert, sync release)
  /* verilator lint_off SYNCASYNCNET */  // standard async-assert / sync-release synchroniser
  logic [2:0] rst_sync;
  always_ff @(posedge clk or negedge ck_rst)
    if (!ck_rst) rst_sync <= '0;
    else         rst_sync <= {rst_sync[1:0], 1'b1};
  wire rst_n = rst_sync[2];
  /* verilator lint_on SYNCASYNCNET */

  logic       rx_valid, tx_start, tx_busy;
  logic [7:0] rx_data, tx_data;
  uart_rx #(.CLKS_PER_BIT(CLKS_PER_BIT)) u_rx (
    .clk, .rst_n, .rx(uart_txd_in), .valid(rx_valid), .data(rx_data));
  uart_tx #(.CLKS_PER_BIT(CLKS_PER_BIT)) u_tx (
    .clk, .rst_n, .start(tx_start), .data(tx_data), .busy(tx_busy), .tx(uart_rxd_out));

  logic                  cfg_we, s_valid, s_ready, m_valid, m_ready, br_busy;
  logic [15:0]           cfg_addr;
  logic [63:0]           cfg_wdata;
  logic signed [X_W-1:0] s_data;
  logic [1:0]            m_class;
  logic [P_W-1:0]        m_prob [3];
  logic [P_W-1:0]        m_fam_prob [12];
  logic [31:0]           m_lat_cycles;

  ems_uart_bridge u_bridge (
    .clk, .rst_n, .rx_valid, .rx_data, .tx_start, .tx_data, .tx_busy,
    .cfg_we, .cfg_addr, .cfg_wdata, .s_valid, .s_ready, .s_data,
    .m_valid, .m_ready, .m_class, .m_prob, .m_fam_prob, .m_lat_cycles, .busy(br_busy));

  ems_classifier #(.WEIGHTS_FILE(WEIGHTS_FILE), .EXP_FILE(EXP_FILE)) u_core (
    .clk, .rst_n, .cfg_we, .cfg_addr, .cfg_wdata,
    .s_valid, .s_ready, .s_data,
    .m_valid, .m_ready, .m_class, .m_prob, .m_fam_prob, .m_lat_cycles);

  logic [26:0] hb;
  logic [1:0]  last_cls;
  always_ff @(posedge clk or negedge rst_n)
    if (!rst_n) begin hb <= '0; last_cls <= '0; end
    else begin
      hb <= hb + 1'b1;
      if (m_valid) last_cls <= m_class;
    end
  assign led = {last_cls, br_busy, hb[26]};
endmodule
