# Task 001: Timing Side-Channel in Hardware (Yosys Synthesis)

## 工具流程
1. Verilog RTL 設計
2. **Yosys 邏輯合成** → JSON Netlist
3. Python 分析 Netlist 中的時序漏洞

## 漏洞
非恆定時間比較洩露秘密位的位置

## 步驟
```bash
# 1. 用 SystemVerilog 模式合成到 Netlist
yosys -p "read_verilog -sv rtl/vulnerable.v; synth_ice40 -json rtl/synthesis.json"

# 2. 分析漏洞
python3 solution/analyze_netlist.py

# 3. 利用漏洞
python3 solution/exploit.py
```

Flag: TIMING_LEAK{0xDEADBEEF}
