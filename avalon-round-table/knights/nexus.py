import openai
import os

def handle_nexus(prompt, config):
    openai.api_key = os.environ.get(config["api_key_env"])

    response = openai.ChatCompletion.create(
        model=config["model_name"],
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content
