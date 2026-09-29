// tb_softmax3.sv -- bit-exact unit test of ems_softmax3 against fxp.softmax3_q
// on adversarial logits (golden_model.py --gen-softmax). Run from hw/.
`timescale 1ns/1ps
module tb_softmax3;
  import ems_pkg::*;

  logic clk = 0, rst_n = 0;
  always #5 clk = ~clk;

  logic                  start = 0, busy, done;
  logic signed [L_W-1:0] lg [3];
  logic        [P_W-1:0] p  [3];

  ems_softmax3 #(.EXP_FILE("rtl/mem/exp_lut.mem")) dut (
    .clk, .rst_n, .start, .lg, .busy, .done, .p);

  initial begin
    int fd, r, n = 0, bad = 0, cycles = 0;
    logic [31:0] a [3];
    logic [16:0] e [3];

    fd = $fopen("tb/vectors/softmax.txt", "r");
    if (fd == 0) $fatal(1, "cannot open tb/vectors/softmax.txt");
    for (int j = 0; j < 3; j++) lg[j] = '0;
    repeat (3) @(negedge clk);
    rst_n = 1;

    while (!$feof(fd)) begin
      r = $fscanf(fd, "%h %h %h %h %h %h", a[0], a[1], a[2], e[0], e[1], e[2]);
      if (r != 6) break;
      @(negedge clk);
      for (int j = 0; j < 3; j++) lg[j] = a[j];
      start = 1;
      @(negedge clk); start = 0;
      cycles = 1;
      while (!done) begin @(negedge clk); cycles++; end
      if (p[0] !== e[0] || p[1] !== e[1] || p[2] !== e[2]) begin
        bad++;
        if (bad <= 5)
          $display("MISMATCH lg %h %h %h: got %h %h %h exp %h %h %h",
                   a[0], a[1], a[2], p[0], p[1], p[2], e[0], e[1], e[2]);
      end
      n++;
    end
    $display("softmax3: %0d vectors, %0d mismatches, %0d cycles/call", n, bad, cycles);
    if (bad != 0 || n == 0) $fatal(1, "FAIL");
    $display("PASS");
    $finish;
  end
endmodule
