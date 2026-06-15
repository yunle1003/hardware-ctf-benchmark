#!/usr/bin/env python3
"""使用 Yosys 生成的 Netlist 分析時序漏洞"""
import json
from pathlib import Path

def analyze_netlist():
    """分析 Yosys 合成生成的 Netlist"""
    netlist_file = Path("rtl/synthesis.json")
    
    if not netlist_file.exists():
        print("[!] Netlist not found. Run: yosys -p \"read_verilog rtl/vulnerable.v; synth_ice40 -json rtl/synthesis.json\"")
        return
    
    with open(netlist_file) as f:
        netlist = json.load(f)
    
    print("[*] Analyzing Yosys-generated Netlist...")
    print(f"[+] Modules: {list(netlist.get('modules', {}).keys())}")
    
    # 查找時序路徑
    for module_name, module in netlist.get('modules', {}).items():
        print(f"\n[*] Module: {module_name}")
        
        # 統計邏輯門
        cells = module.get('cells', {})
        print(f"[+] Logic gates: {len(cells)}")
        
        # 查找比較相關的邏輯
        for cell_name, cell in cells.items():
            cell_type = cell.get('type', '')
            if 'eq' in cell_type.lower() or 'cmp' in cell_type.lower():
                print(f"    [!] Comparison logic found: {cell_name} ({cell_type})")
    
    print("\n[+] Netlist analysis complete!")
    print("[+] Ready to exploit timing vulnerability in synthesized design")

if __name__ == "__main__":
    analyze_netlist()
