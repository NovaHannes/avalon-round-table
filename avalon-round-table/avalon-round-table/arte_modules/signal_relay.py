import json
from datetime import datetime

def log_event(event, filepath="logs/example_log.json"):
    log_entry = {
        "timestamp": datetime.utcnow().isoformat(),
        "event": event
    }
    with open(filepath, "a") as f:
        f.write(json.dumps(log_entry) + "\n")
