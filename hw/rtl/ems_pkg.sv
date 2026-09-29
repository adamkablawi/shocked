// ems_pkg.sv -- fixed-point formats and cfg address map.
// Must match hw/scripts/fxp.py exactly.
package ems_pkg;
  localparam int X_W   = 32;  // raw feature / mu, Q13.19
  localparam int Z_W   = 18;  // normalised feature, Q4.13
  localparam int WT_W  = 18;  // folded LDA weight, Q1.16
  localparam int ACC_W = 48;  // MAC accumulators
  localparam int L_W   = 32;  // logits, Q.16
  localparam int M_W   = 17;  // inv-sd mantissa (unsigned)
  localparam int S_W   = 6;   // inv-sd shift
  localparam int P_W   = 17;  // probability, unsigned Q0.16
  localparam int C_W   = 18;  // meta coefficient, Q2.15
  localparam int E_W   = 18;  // exp LUT value, Q1.17

  localparam int LDA_SHIFT  = 13;  // acc Q.29 -> logit Q.16
  localparam int META_SHIFT = 15;  // p*c Q.31 -> logit Q.16

  localparam int EXP_IDX_W = 10;
  localparam int LOG2E_Q16 = 94548;
  localparam int DIFF_W    = 22;         // clamped (max - logit), Q.16
  localparam int DIFF_CLAMP = 32 << 16;  // 2^21

  // cfg address map (64-bit data words)
  localparam logic [15:0] ADDR_CALIB = 16'h0000;  // + k : {s, m, mu}
  localparam logic [15:0] ADDR_W     = 16'h0800;  // + k : {w2, w1, w0}
  localparam logic [15:0] ADDR_BIAS  = 16'h1000;  // + fam*3 + j
  localparam logic [15:0] ADDR_MC    = 16'h1010;  // + j*12 + i
  localparam logic [15:0] ADDR_MB    = 16'h1040;  // + j
endpackage
