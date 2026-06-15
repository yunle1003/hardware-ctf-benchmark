#!/usr/bin/env python3
"""
Analyze Yosys-generated netlist for timing vulnerabilities
"""

import json
from pathlib import Path

def analyze_netlist():
    """Analyze synthesized hardware netlist"""
    netlist_file = Path("../environment/assets/timing-comparator/rtl/synthesis.json")
    
    if not netlist_file.exists():
        print("[!] Netlist not found. Run Yosys synthesis first:")
        print("    yosys -p \"read_verilog -sv rtl/vulnerable.v; synth_ice40 -json rtl/synthesis.json\"")
        return False
    
    try:
        with open(netlist_file) as f:
            netlist = json.load(f)
    except:
        print("[!] Error reading netlist")
        return False
    
    print("[*] Analyzing Yosys-generated Netlist...")
    
    modules = netlist.get('modules', {})
    print(f"[+] Found {len(modules)} modules")
    
    # Analyze vulnerable_comparator module
    vuln_module = modules.get('vulnerable_comparator', {})
    if vuln_module:
        cells = vuln_module.get('cells', {})
        print(f"[+] vulnerable_comparator: {len(cells)} logic gates")
        
        # Look for comparison logic
        for cell_name, cell in cells.items():
            cell_type = cell.get('type', '')
            if 'eq' in cell_type.lower() or 'xor' in cell_type.lower():
                print(f"    [!] Comparison logic: {cell_name} ({cell_type})")
    
    print("\n[+] Netlist analysis complete!")
    return True

if __name__ == "__main__":
    analyze_netlist()
