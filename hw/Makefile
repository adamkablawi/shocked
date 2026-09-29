# hw/Makefile -- export, lint and simulate the FPGA classifier (run from hw/).
#   make export    regenerate mem/*.mem + ems_params_pkg.sv from the joblib
#   make vectors   golden-model checks + test vectors
#   make lint      verilator -Wall on the synthesizable RTL
#   make sim       softmax unit test + core bit-exact test + UART end-to-end test
#   make all       everything above
PY   ?= python3
VL   ?= verilator
VLFLAGS = --binary --timing -j 8 -Wno-fatal -Wno-lint -Wno-style -Irtl

CORE_RTL = rtl/ems_pkg.sv rtl/ems_params_pkg.sv rtl/ems_sdp_ram.sv \
           rtl/ems_softmax3.sv rtl/ems_classifier.sv
TOP_RTL  = $(CORE_RTL) rtl/uart_rx.sv rtl/uart_tx.sv rtl/ems_uart_bridge.sv rtl/arty_s7_top.sv

.PHONY: all export vectors lint sim sim-softmax sim-core sim-top clean

all: export vectors lint sim

export:
	$(PY) scripts/export_model.py

vectors:
	$(PY) scripts/golden_model.py --check-float --check-fixed --gen-vectors --gen-softmax

lint:
	$(VL) --lint-only -Wall -Wno-DECLFILENAME -Irtl $(TOP_RTL) --top-module arty_s7_top

sim: sim-softmax sim-core sim-top

sim-softmax:
	$(VL) $(VLFLAGS) -Mdir build/obj_sm --top-module tb_softmax3 \
	  rtl/ems_pkg.sv rtl/ems_sdp_ram.sv rtl/ems_softmax3.sv tb/tb_softmax3.sv -o Vtb >/dev/null 2>&1
	./build/obj_sm/Vtb

sim-core:
	@mkdir -p tb/out
	$(VL) $(VLFLAGS) -Mdir build/obj_core --top-module tb_ems_classifier \
	  $(CORE_RTL) tb/tb_ems_classifier.sv -o Vtb >/dev/null 2>&1
	./build/obj_core/Vtb +VEC=$(or $(VEC),tb/vectors/core.txt) +OUT=$(or $(OUT),tb/out/core_results.txt)

sim-top:
	$(VL) $(VLFLAGS) -Mdir build/obj_top --top-module tb_top_uart \
	  $(TOP_RTL) tb/tb_top_uart.sv -o Vtb >/dev/null 2>&1
	./build/obj_top/Vtb

clean:
	rm -rf build tb/out
