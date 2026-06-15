#!/usr/bin/env python3
import json
from pathlib import Path
flags_file = Path("/tmp/flags/flags.txt")
content = flags_file.read_text() if flags_file.exists() else ""
result = {"score": 1.0 if "TIMING_LEAK{0xDEADBEEF}" in content else 0.0}
print(json.dumps(result, indent=2))
