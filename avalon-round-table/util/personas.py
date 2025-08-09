from pathlib import Path
import yaml

def load_personas(config_path: str) -> dict[str, str]:
    """
    Expected YAML structure:
      knights:
        nexus:
          persona: "You are Sir Nexus ..."
        cadmus:
          persona: "..."
    (Also accepts 'prompt' if 'persona' is missing.)
    """
    text = Path(config_path).read_text(encoding="utf-8")
    data = yaml.safe_load(text) or {}

    personas: dict[str, str] = {}
    for name, info in (data.get("knights") or {}).items():
        if not isinstance(info, dict):
            continue
        prompt = (info.get("persona") or info.get("prompt") or "").strip()
        if prompt:
            personas[name] = prompt
    return personas
