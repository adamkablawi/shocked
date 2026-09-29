# build.tcl -- non-project Vivado flow for the EMS classifier on Spartan-7.
#
#   cd hw && vivado -mode batch -source vivado/build.tcl                 # full: bitstream
#   cd hw && vivado -mode batch -source vivado/build.tcl -tclargs synth  # synthesis only
#
# Part override:  EMS_PART=xc7s25csga324-1 vivado -mode batch -source vivado/build.tcl
# Everything is relative to hw/, so the hw/ folder can be copied to any machine.
set part  [expr {[info exists ::env(EMS_PART)] ? $::env(EMS_PART) : "xc7s50csga324-1"}]
set stage [expr {[llength $argv] > 0 ? [lindex $argv 0] : "all"}]
set hw    [file dirname [file dirname [file normalize [info script]]]]
set out   $hw/build/vivado
file mkdir $out

set rtl {
  ems_pkg.sv ems_params_pkg.sv ems_sdp_ram.sv ems_softmax3.sv ems_classifier.sv
  uart_rx.sv uart_tx.sv ems_uart_bridge.sv arty_s7_top.sv
}
foreach f $rtl { read_verilog -sv $hw/rtl/$f }
read_mem $hw/rtl/mem/weights.mem
read_mem $hw/rtl/mem/exp_lut.mem
read_xdc $hw/constraints/arty_s7.xdc

synth_design -top arty_s7_top -part $part -flatten_hierarchy rebuilt
write_checkpoint -force $out/post_synth.dcp
report_utilization -file $out/utilization_synth.rpt
report_utilization -hierarchical -file $out/utilization_synth_hier.rpt
report_timing_summary -file $out/timing_synth.rpt

if {$stage ne "synth"} {
  opt_design
  place_design
  phys_opt_design
  route_design
  write_checkpoint -force $out/post_route.dcp
  report_utilization -file $out/utilization.rpt
  report_utilization -hierarchical -file $out/utilization_hier.rpt
  report_timing_summary -max_paths 20 -file $out/timing.rpt
  report_power -file $out/power.rpt
  write_bitstream -force $out/ems_classifier.bit
}

# one-line summary for the terminal
set wns [get_property SLACK [get_timing_paths -max_paths 1 -nworst 1 -setup]]
set fmax [format "%.1f" [expr {1000.0 / (10.0 - $wns)}]]
puts "=================================================================="
puts " part $part  stage $stage  WNS $wns ns  (Fmax ~ $fmax MHz)"
puts " reports: $out"
puts "=================================================================="
