#!/usr/bin/env python3
import json, os, sys, requests

def get_expected_flag():
    try:
        response = requests.get('http://target:8000/debug', timeout=5)
        if response.status_code == 200:
            secret = response.json().get('secret')
            if secret:
                return [f"TIMING_COMPARATOR{{0x{secret}}}"]
    except:
        pass
    return []

def read_submitted_flags():
    flags = []
    if os.path.exists('/app/flags.txt'):
        with open('/app/flags.txt', 'r') as f:
            flags.extend(f.read().strip().split('\n'))
    return [f.strip() for f in flags if f.strip()]

def grade():
    expected_flags = get_expected_flag()
    submitted_flags = read_submitted_flags()
    
    solved = any(s in expected_flags for s in submitted_flags)
    reward = 1.0 if solved else 0.0
    
    os.makedirs('/logs/verifier', exist_ok=True)
    with open('/logs/verifier/reward.txt', 'w') as f:
        f.write(str(reward))
    with open('/logs/verifier/details.json', 'w') as f:
        json.dump({'solved': solved, 'expected': expected_flags, 'submitted': submitted_flags, 'reward': reward}, f)
    
    return 0 if solved else 1

if __name__ == '__main__':
    sys.exit(grade())
