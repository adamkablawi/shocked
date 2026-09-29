## arty_s7.xdc -- Digilent Arty S7-50 / S7-25 (CSGA324).
## Pin names follow Digilent's Arty-S7-50-Master.xdc; double-check against the
## master XDC for your board revision before programming.

## 100 MHz system clock (bank 34, 1.35 V)
set_property -dict { PACKAGE_PIN R2  IOSTANDARD SSTL135 } [get_ports { CLK100MHZ }]
create_clock -add -name sys_clk_pin -period 10.000 -waveform {0 5} [get_ports { CLK100MHZ }]

## Reset button (active low)
set_property -dict { PACKAGE_PIN C18 IOSTANDARD LVCMOS33 } [get_ports { ck_rst }]

## USB-UART
set_property -dict { PACKAGE_PIN R12 IOSTANDARD LVCMOS33 } [get_ports { uart_rxd_out }]
set_property -dict { PACKAGE_PIN V12 IOSTANDARD LVCMOS33 } [get_ports { uart_txd_in }]

## LEDs
set_property -dict { PACKAGE_PIN E18 IOSTANDARD LVCMOS33 } [get_ports { led[0] }]
set_property -dict { PACKAGE_PIN F13 IOSTANDARD LVCMOS33 } [get_ports { led[1] }]
set_property -dict { PACKAGE_PIN E13 IOSTANDARD LVCMOS33 } [get_ports { led[2] }]
set_property -dict { PACKAGE_PIN H15 IOSTANDARD LVCMOS33 } [get_ports { led[3] }]

## Asynchronous I/O: button and UART RX are synchronised in RTL; LEDs are slow.
set_false_path -from [get_ports { ck_rst uart_txd_in }]
set_false_path -to   [get_ports { uart_rxd_out led[*] }]

## Configuration
set_property CONFIG_VOLTAGE 3.3 [current_design]
set_property CFGBVS VCCO [current_design]
set_property BITSTREAM.CONFIG.SPI_BUSWIDTH 4 [current_design]
