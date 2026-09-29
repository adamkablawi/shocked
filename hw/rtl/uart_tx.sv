// uart_tx.sv -- 8N1 UART transmitter.
module uart_tx #(
  parameter int CLKS_PER_BIT = 108
) (
  input  logic       clk,
  input  logic       rst_n,
  input  logic       start,             // accepted when !busy
  input  logic [7:0] data,
  output logic       busy,
  output logic       tx
);
  localparam int CW = $clog2(CLKS_PER_BIT + 1);
  logic [CW-1:0] cnt;
  logic [3:0]    bitn;                  // 0 start, 1..8 data, 9 stop
  logic [9:0]    frame;

  always_ff @(posedge clk or negedge rst_n) begin
    if (!rst_n) begin
      busy <= 1'b0; tx <= 1'b1; cnt <= '0; bitn <= '0; frame <= '1;
    end else if (!busy) begin
      tx <= 1'b1;
      if (start) begin
        frame <= {1'b1, data, 1'b0};
        busy <= 1'b1; cnt <= '0; bitn <= '0;
        tx <= 1'b0;
      end
    end else if (cnt == CW'(CLKS_PER_BIT - 1)) begin
      cnt <= '0;
      if (bitn == 4'd9) busy <= 1'b0;
      else begin
        bitn <= bitn + 4'd1;
        tx <= frame[bitn + 4'd1];
      end
    end else cnt <= cnt + 1'b1;
  end
endmodule
