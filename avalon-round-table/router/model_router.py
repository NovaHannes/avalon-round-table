import yaml
import os

from knights.nexus import handle_nexus
from knights.cadmus import handle_cadmus
from knights.lancelot_simulated import handle_lancelot

class ModelRouter:
    def __init__(self, config_path="router/knights_config.yaml"):
        with open(config_path, "r") as f:
            full_config = yaml.safe_load(f)
        self.knights = {k["name"]: k for k in full_config["knights"]}

    def invoke(self, knight_name, prompt):
        knight = self.knights.get(knight_name)
        if not knight:
            raise ValueError(f"Knight '{knight_name}' not found.")

        model_type = knight["model_type"]
        config = knight["config"]

        if model_type == "openai":
            return handle_nexus(prompt, config)

        elif model_type == "vertex_ai":
            return handle_cadmus(prompt, config)

        elif model_type == "simulated":
            host = config["host_model"]
            persona_prompt = config["persona_prompt"]
            full_prompt = f"{persona_prompt.strip()}\n\n{prompt.strip()}"
            return self.invoke(host, full_prompt)

        else:
            raise NotImplementedError(f"Model type '{model_type}' not supported.")
