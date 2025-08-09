from pathlib import Path
import json
from typing import Any, Dict

def _ensure_logs_dir(log_dir: str = "logs") -> Path:
    p = Path(log_dir)
    p.mkdir(parents=True, exist_ok=True)
    return p

def log_event(event: Dict[str, Any],
              log_dir: str = "logs",
              filename: str = "example_log.json") -> None:
    """
    Append one JSON line to logs/<filename>, creating logs/ if missing.
    """
    log_path = _ensure_logs_dir(log_dir) / filename
    with log_path.open("a", encoding="utf-8") as f:
        f.write(json.dumps(event, ensure_ascii=False) + "\n")
