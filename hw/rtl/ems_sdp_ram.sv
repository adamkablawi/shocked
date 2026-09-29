// ems_sdp_ram.sv -- simple dual-port RAM (1 write, 1 registered read).
// Infers block RAM in Vivado. Optional $readmemh init (also used as a ROM).
module ems_sdp_ram #(
  parameter int    WIDTH     = 32,
  parameter int    DEPTH     = 1024,
  parameter string INIT_FILE = ""
) (
  input  logic                     clk,
  input  logic                     we,
  input  logic [$clog2(DEPTH)-1:0] waddr,
  input  logic [WIDTH-1:0]         wdata,
  input  logic [$clog2(DEPTH)-1:0] raddr,
  output logic [WIDTH-1:0]         rdata
);
  (* ram_style = "block" *) logic [WIDTH-1:0] mem [DEPTH];

  initial begin
    if (INIT_FILE != "") $readmemh(INIT_FILE, mem);
    else for (int i = 0; i < DEPTH; i++) mem[i] = '0;
  end

  always_ff @(posedge clk) begin
    if (we) mem[waddr] <= wdata;
    rdata <= mem[raddr];
  end
endmodule
