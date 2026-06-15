#!/bin/bash
set -e

echo "[*] Task 001: Timing Side-Channel Attack"
echo "[*] =========================================="
echo

# Create output directories
mkdir -p /app /logs/agent /logs/verifier

# Step 1: Synthesize RTL with Yosys
echo "[1] Synthesizing RTL with Yosys..."
cd /workspace/assets/timing-comparator/rtl
yosys -p "read_verilog -sv vulnerable.v; synth_ice40 -json synthesis.json" 2>&1 | tail -5
echo "[+] Synthesis complete: synthesis.json ($(ls -lh synthesis.json | awk '{print $5}'))"
echo

# Step 2: Compile and simulate
echo "[2] Compiling and simulating Verilog..."
iverilog -o test testbench.v vulnerable.v
vvp test 2>&1 | grep "Test"
echo "[+] Simulation complete"
echo

# Step 3: Analyze netlist
echo "[3] Analyzing netlist for vulnerabilities..."
python3 /workspace/solution/analyze_netlist.py
echo

# Step 4: Run exploit
echo "[4] Running exploit..."
python3 /workspace/solution/exploit.py
echo

# Step 5: Grade solution
echo "[5] Grading submission..."
python3 /workspace/tests/grade.py
echo

echo "[*] Test complete!"
