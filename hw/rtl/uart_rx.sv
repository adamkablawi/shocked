// uart_rx.sv -- 8N1 UART receiver, samples mid-bit.
module uart_rx #(
  parameter int CLKS_PER_BIT = 108     // 100 MHz / 921600 baud
) (
  input  logic       clk,
  input  logic       rst_n,
  input  logic       rx,
  output logic       valid,             // 1-cycle pulse
  output logic [7:0] data
);
  localparam int CW = $clog2(CLKS_PER_BIT + 1);
  typedef enum logic [1:0] {IDLE, START, DATA, STOP} st_t;
  st_t st;
  logic [CW-1:0] cnt;
  logic [2:0]    bitn;
  logic          rx_s1, rx_s;             // 2-FF synchroniser

  always_ff @(posedge clk or negedge rst_n) begin
    if (!rst_n) begin
      rx_s1 <= 1'b1; rx_s <= 1'b1;
      st <= IDLE; cnt <= '0; bitn <= '0; valid <= 1'b0; data <= '0;
    end else begin
      rx_s1 <= rx; rx_s <= rx_s1;
      valid <= 1'b0;
      unique case (st)
        IDLE: if (!rx_s) begin st <= START; cnt <= '0; end
        START: if (cnt == CW'(CLKS_PER_BIT / 2)) begin
                 cnt <= '0;
                 st  <= rx_s ? IDLE : DATA;       // glitch -> back to idle
                 bitn <= '0;
               end else cnt <= cnt + 1'b1;
        DATA: if (cnt == CW'(CLKS_PER_BIT - 1)) begin
                cnt <= '0;
                data <= {rx_s, data[7:1]};
                if (bitn == 3'd7) st <= STOP;
                bitn <= bitn + 3'd1;
              end else cnt <= cnt + 1'b1;
        STOP: if (cnt == CW'(CLKS_PER_BIT - 1)) begin
                st <= IDLE; cnt <= '0;
                valid <= rx_s;                     // drop framing errors
              end else cnt <= cnt + 1'b1;
        default: st <= IDLE;
      endcase
    end
  end
endmodule
