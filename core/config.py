from __future__ import annotations
from pathlib import Path
import yaml

CONFIG_PATH = Path(__file__).resolve().parents[1] / "config" / "scanners.yaml"


def load_config() -> dict:
    with CONFIG_PATH.open("r", encoding="utf-8") as fh:
        return yaml.safe_load(fh)
