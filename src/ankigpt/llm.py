import os
import json
from openai import OpenAI

JSON_INSTRUCTION = "You are a system that only outputs JSON."

api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

def generate(system_prompt: str, user_prompt: str) -> str:
    completion = client.chat.completions.create(
        model="gpt-4-1106-preview",
        response_format={"type": "json_object"},
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ]
    )
    return completion.choices[0].message.content

def generate_json(
        system_prompt: str,
        user_prompt: str,
        examples: str = "") -> dict:
    json_prompt = JSON_INSTRUCTION + system_prompt + examples
    generated_json: str = generate(json_prompt, user_prompt)
    return json.loads(generated_json)