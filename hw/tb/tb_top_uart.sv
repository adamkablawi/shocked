// tb_top_uart.sv -- end-to-end test of arty_s7_top through its UART pins,
// using the exact byte protocol the host scripts use.
//   'B' calibration burst -> 'k'
//   'W' single write      -> 'k'
//   'F' trial 0, trial 1  -> result packets checked bit-exact vs golden vectors
//   'T' 4                 -> throughput packet (4 back-to-back runs)
// Fast UART (8 clocks/bit) to keep simulation short. Run from hw/.
`timescale 1ns/1ps
module tb_top_uart;
  import ems_params_pkg::*;

  localparam int CPB = 8;
  localparam int BIT_NS = CPB * 10;

  logic clk = 0, rst_n = 0;
  always #5 clk = ~clk;

  logic       rx_line = 1'b1;   // host -> FPGA
  logic       tx_line;          // FPGA -> host
  logic [3:0] led;

  arty_s7_top #(.CLKS_PER_BIT(CPB),
                .WEIGHTS_FILE("rtl/mem/weights.mem"), .EXP_FILE("rtl/mem/exp_lut.mem")) dut (
    .CLK100MHZ(clk), .ck_rst(rst_n), .uart_txd_in(rx_line), .uart_rxd_out(tx_line), .led);

  // ───────── host UART model ─────────
  task automatic send_byte(input logic [7:0] b);
    rx_line = 1'b0; #(BIT_NS);
    for (int i = 0; i < 8; i++) begin rx_line = b[i]; #(BIT_NS); end
    rx_line = 1'b1; #(BIT_NS);
  endtask

  task automatic send_le(input logic [63:0] v, input int nbytes);
    for (int i = 0; i < nbytes; i++) send_byte(v[8*i +: 8]);
  endtask

  logic [7:0] rxq [$];
  initial forever begin
    logic [7:0] b;
    @(negedge tx_line);
    #(BIT_NS / 2);
    for (int i = 0; i < 8; i++) begin #(BIT_NS); b[i] = tx_line; end
    #(BIT_NS);
    rxq.push_back(b);
  end

  task automatic recv(output logic [7:0] b);
    int guard = 0;
    while (rxq.size() == 0) begin
      #(BIT_NS);
      if (++guard > 1_000_000) $fatal(1, "timeout waiting for FPGA byte");
    end
    b = rxq.pop_front();
  endtask

  task automatic recv_le(output logic [31:0] v, input int nbytes);
    logic [7:0] b;
    v = '0;
    for (int i = 0; i < nbytes; i++) begin recv(b); v[8*i +: 8] = b; end
  endtask

  task automatic expect_ack(input string what);
    logic [7:0] b;
    recv(b);
    if (b !== 8'h6b) $fatal(1, "%s: expected 'k', got %h", what, b);
    $display("  %s -> ack", what);
  endtask

  // ───────── vectors (first segment of core.txt) ─────────
  logic [63:0] calib [N_FEAT];
  logic [31:0] feats [2][N_FEAT];
  logic [31:0] expv  [2][16];     // cls, p0..p2, fp0..fp11
  int errors = 0;

  task automatic load_vectors();
    int fd, r, nc = 0, t = 0, nx = 0;
    string tag;
    logic [63:0] a, d;
    fd = $fopen("tb/vectors/core.txt", "r");
    if (fd == 0) $fatal(1, "cannot open tb/vectors/core.txt");
    while (t < 2) begin
      r = $fscanf(fd, "%s", tag);
      if (tag == "C") begin r = $fscanf(fd, "%h %h", a, d); calib[nc++] = d; end
      else if (tag == "X") begin r = $fscanf(fd, "%h", a); feats[t][nx++] = a[31:0]; end
      else if (tag == "E") begin
        for (int i = 0; i < 16; i++) begin r = $fscanf(fd, "%h", a); expv[t][i] = a[31:0]; end
        t++; nx = 0;
      end
    end
    $fclose(fd);
  endtask

  task automatic check_packet(input int t, input int exp_runs);
    logic [7:0]  b;
    logic [31:0] v, lat, total, runs;
    recv(b);
    if (b !== 8'h52) $fatal(1, "expected 'R', got %h", b);
    recv_le(v, 1);
    if (v !== expv[t][0]) begin errors++; $display("  class mismatch: %0d vs %0d", v, expv[t][0]); end
    for (int i = 1; i < 16; i++) begin
      recv_le(v, 4);
      if (v !== expv[t][i]) begin errors++; $display("  field %0d mismatch: %h vs %h", i, v, expv[t][i]); end
    end
    recv_le(lat, 4); recv_le(total, 4); recv_le(runs, 2);
    if (runs != exp_runs) begin errors++; $display("  runs %0d != %0d", runs, exp_runs); end
    $display("  trial %0d: class %0d  lat %0d cycles  total %0d cycles over %0d run(s) -> %0.1f cycles/trial",
             t, expv[t][0], lat, total, runs, real'(total) / runs);
  endtask

  initial begin
    load_vectors();
    repeat (5) @(negedge clk);
    rst_n = 1;
    repeat (10) @(negedge clk);

    $display("[1] calibration burst (%0d words)", N_FEAT);
    send_byte("B"); send_le(64'h0000, 2); send_le(64'(N_FEAT), 2);
    for (int k = 0; k < N_FEAT; k++) send_le(calib[k], 8);
    expect_ack("burst write");

    $display("[2] single write (family-0 class-0 bias, unchanged value)");
    send_byte("W"); send_le(64'h1000, 2); send_le(64'(BIAS_INIT[0][0]), 8);
    expect_ack("single write");

    for (int t = 0; t < 2; t++) begin
      $display("[3.%0d] feature load + run", t);
      send_byte("F");
      for (int k = 0; k < N_FEAT; k++) send_le(64'(feats[t][k]), 4);
      check_packet(t, 1);
    end

    $display("[4] throughput: 4 back-to-back runs of the buffered trial");
    send_byte("T"); send_le(64'd4, 2);
    check_packet(1, 4);

    if (errors != 0) $fatal(1, "FAIL: %0d field mismatches", errors);
    $display("PASS");
    $finish;
  end
endmodule
