from pathlib import Path
import re
import yaml

def _normalize_name(name: str) -> str:
    """
    Make a stable key like 'nexus', 'cadmus', 'lancelot' from 'Sir Nexus', etc.
    """
    s = name.strip().lower()
    s = re.sub(r"^sir\s+", "", s)     # drop leading 'sir '
    s = re.sub(r"[^a-z0-9]+", " ", s) # non-alnum -> space
    s = "_".join(s.split())           # spaces -> underscores
    return s

def load_personas(config_path: str) -> dict[str, str]:
    """
    Supports either:
      knights:
        nexus:
          persona: "..."
        cadmus:
          persona: "..."
    OR:
      knights:
        - name: "Sir Nexus"
          persona: "..."
          config: { persona_prompt: "..." }
        - name: "Sir Lancelot"
          config:
            persona_prompt: "..."
    Accepts 'persona', 'prompt', or 'config.persona_prompt'.
    If no persona is present, we synthesize a minimal default.
    """
    text = Path(config_path).read_text(encoding="utf-8")
    data = yaml.safe_load(text) or {}
    personas: dict[str, str] = {}

    knights = data.get("knights")
    if not knights:
        return personas

    def _extract(name: str, info: dict) -> None:
        key = _normalize_name(name)
        persona = (
            (info.get("persona") or info.get("prompt"))
            or (info.get("config", {}) or {}).get("persona_prompt")
            or ""
        ).strip()

        if not persona:
            # fallback persona so the knight is usable even if YAML omits it
            persona = f"You are {name}, a Knight of the Avalon Round Table. " \
                      f"Be clear, disciplined, and helpful."

        personas[key] = persona

    if isinstance(knights, dict):
        for name, info in knights.items():
            if isinstance(info, dict):
                _extract(str(name), info)

    elif isinstance(knights, list):
        for entry in knights:
            if isinstance(entry, dict):
                name = (entry.get("name") or entry.get("id") or "").strip()
                if not name:
                    continue
                _extract(name, entry)

    return personas
