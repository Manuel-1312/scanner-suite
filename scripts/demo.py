from pathlib import Path
import sys
sys.path.append(str(Path(__file__).resolve().parents[1]))
import json
from core.config import load_config

config = load_config()
engines = config.get("engines", {})
print("=== Scanner Suite Pro Demo ===\n")
print("Loaded engines:")
for name, info in engines.items():
    print(f"- {name}: {info.get('description')} (command template: {info.get('command')})")

profile_path = Path("profiles/quick.json")
profile = json.loads(profile_path.read_text()) if profile_path.exists() else {"target": "127.0.0.1"}
target = profile.get("target")
selected_engines = list(engines.keys())
commands = [f"{engines[name]['command']} {target}" for name in selected_engines if name in engines]
print("\nSample run (dry-run):")
for cmd in commands:
    print(f"  $ {cmd}")
print("\nResulting report path:", config.get("report", {}).get("output", "scanner-report.json"))
print("Demo complete. To execute for real, install the scanners and run `python core/scanner.py profiles/quick.json --engines " + ",".join(selected_engines) + "`.")