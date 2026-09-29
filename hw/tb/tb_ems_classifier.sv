// tb_ems_classifier.sv -- bit-exact check of ems_classifier against the golden
// model vectors (hw/scripts/golden_model.py --gen-vectors).
//
// Streams features back-to-back (the core's own s_ready is the only throttle),
// checks class + final probs + all 12 family probs for every trial, and reports
// compute latency and trial-to-trial throughput in cycles.
//
// Plusargs: +VEC=<vector file>  +OUT=<per-trial results file>
// Run from hw/ (see hw/Makefile: `make sim`).
`timescale 1ns/1ps
module tb_ems_classifier;
  import ems_pkg::*;

  localparam real CLK_MHZ = 100.0;

  logic clk = 0, rst_n = 0;
  always #5 clk = ~clk;

  logic                  cfg_we = 0;
  logic [15:0]           cfg_addr = 0;
  logic [63:0]           cfg_wdata = 0;
  logic                  s_valid = 0, s_ready;
  logic signed [X_W-1:0] s_data = 0;
  logic                  m_valid;
  logic [1:0]            m_class;
  logic [P_W-1:0]        m_prob [3];
  logic [P_W-1:0]        m_fam_prob [12];
  logic [31:0]           m_lat_cycles;

  ems_classifier #(
    .WEIGHTS_FILE("rtl/mem/weights.mem"), .EXP_FILE("rtl/mem/exp_lut.mem")
  ) dut (
    .clk, .rst_n, .cfg_we, .cfg_addr, .cfg_wdata,
    .s_valid, .s_ready, .s_data,
    .m_valid, .m_ready(1'b1), .m_class, .m_prob, .m_fam_prob, .m_lat_cycles);

  // expected results, in order
  typedef struct { logic [1:0] cls; logic [P_W-1:0] p [3]; logic [P_W-1:0] fp [12]; } exp_t;
  exp_t exp_q [$];

  int    n_trials = 0, n_bad = 0;
  longint cyc = 0, last_valid_cyc = -1;
  longint lat_min = 64'h7fffffff, lat_max = 0, lat_sum = 0;
  longint per_min = 64'h7fffffff, per_max = 0, per_sum = 0, n_per = 0;
  int    fout;
  bit    back_to_back = 0;   // set while trials of one segment stream continuously

  always @(posedge clk) cyc <= cyc + 1;

  // ───────────── checker ─────────────
  always @(posedge clk) if (rst_n && m_valid) begin
    exp_t e;
    bit bad;
    if (exp_q.size() == 0) $fatal(1, "result with no expectation");
    e = exp_q.pop_front();
    bad = (m_class !== e.cls);
    for (int j = 0; j < 3; j++)  bad |= (m_prob[j] !== e.p[j]);
    for (int i = 0; i < 12; i++) bad |= (m_fam_prob[i] !== e.fp[i]);
    if (bad) begin
      n_bad++;
      if (n_bad <= 5)
        $display("MISMATCH trial %0d: got cls %0d p %h %h %h | exp cls %0d p %h %h %h",
                 n_trials, m_class, m_prob[0], m_prob[1], m_prob[2],
                 e.cls, e.p[0], e.p[1], e.p[2]);
    end
    // per-trial results: class p0 p1 p2 fp0..fp11 lat_cycles
    $fwrite(fout, "%0d %0d %0d %0d", m_class, m_prob[0], m_prob[1], m_prob[2]);
    for (int i = 0; i < 12; i++) $fwrite(fout, " %0d", m_fam_prob[i]);
    $fdisplay(fout, " %0d", m_lat_cycles);
    lat_sum += m_lat_cycles;
    if (m_lat_cycles < lat_min) lat_min = m_lat_cycles;
    if (m_lat_cycles > lat_max) lat_max = m_lat_cycles;
    if (back_to_back && last_valid_cyc >= 0) begin
      longint per;
      per = cyc - last_valid_cyc;
      per_sum += per; n_per++;
      if (per < per_min) per_min = per;
      if (per > per_max) per_max = per;
    end
    last_valid_cyc = cyc;
    n_trials++;
  end

  // ───────────── driver ─────────────
  task automatic send_x(input logic [31:0] v);
    @(negedge clk);
    while (!s_ready) begin s_valid = 0; @(negedge clk); end
    s_valid = 1; s_data = v;
  endtask

  task automatic idle_until_drained();
    @(negedge clk); s_valid = 0;
    while (exp_q.size() != 0) @(negedge clk);
    back_to_back = 0; last_valid_cyc = -1;
  endtask

  task automatic cfg_write(input logic [15:0] a, input logic [63:0] d);
    @(negedge clk); cfg_we = 1; cfg_addr = a; cfg_wdata = d;
    @(negedge clk); cfg_we = 0;
  endtask

  initial begin
    string vec, outf, tag;
    int fd, r;
    logic [63:0] a, d;
    exp_t e;
    bit in_cfg = 0;

    if (!$value$plusargs("VEC=%s", vec)) vec = "tb/vectors/core.txt";
    if (!$value$plusargs("OUT=%s", outf)) outf = "tb/out/core_results.txt";
    fd = $fopen(vec, "r");
    if (fd == 0) $fatal(1, "cannot open %s", vec);
    fout = $fopen(outf, "w");
    if (fout == 0) $fatal(1, "cannot open %s (mkdir tb/out?)", outf);

    repeat (5) @(negedge clk);
    rst_n = 1;

    while (!$feof(fd)) begin
      r = $fscanf(fd, "%s", tag);
      if (r != 1) break;
      if (tag == "C") begin
        r = $fscanf(fd, "%h %h", a, d);
        if (!in_cfg) begin idle_until_drained(); in_cfg = 1; end
        cfg_write(a[15:0], d);
      end else if (tag == "X") begin
        r = $fscanf(fd, "%h", a);
        in_cfg = 0; back_to_back = 1;
        send_x(a[31:0]);
      end else if (tag == "E") begin
        r = $fscanf(fd, "%h", a); e.cls = a[1:0];
        for (int j = 0; j < 3; j++)  begin r = $fscanf(fd, "%h", a); e.p[j]  = a[P_W-1:0]; end
        for (int i = 0; i < 12; i++) begin r = $fscanf(fd, "%h", a); e.fp[i] = a[P_W-1:0]; end
        exp_q.push_back(e);
      end else $fatal(1, "bad vector tag '%s'", tag);
    end
    idle_until_drained();
    repeat (10) @(negedge clk);

    $display("--------------------------------------------------------------");
    $display("trials checked : %0d   mismatches: %0d", n_trials, n_bad);
    $display("latency cycles : min %0d  mean %0.1f  max %0d   (%0.2f us @ %0.0f MHz)",
             lat_min, real'(lat_sum) / n_trials, lat_max,
             real'(lat_sum) / n_trials / CLK_MHZ, CLK_MHZ);
    if (n_per > 0)
      $display("period cycles  : min %0d  mean %0.1f  max %0d   (%0.0f trials/s @ %0.0f MHz)",
               per_min, real'(per_sum) / n_per, per_max,
               CLK_MHZ * 1e6 / (real'(per_sum) / n_per), CLK_MHZ);
    $display("--------------------------------------------------------------");
    $fclose(fout);
    if (n_bad != 0 || n_trials == 0) $fatal(1, "FAIL");
    $display("PASS");
    $finish;
  end
endmodule
