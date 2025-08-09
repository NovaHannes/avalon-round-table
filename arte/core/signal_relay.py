import json
import os
from datetime import datetime

def log_event(data, output_dir="logs"):
    """Logs the deliberation result to a timestamped JSON file."""
    # Ensure output directory exists
    os.makedirs(output_dir, exist_ok=True)

    # Create a filename with timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"roundtable_log_{timestamp}.json"
    filepath = os.path.join(output_dir, filename)

    # Write data to file
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

    print(f"📁 Transcript logged to: {filepath}")
