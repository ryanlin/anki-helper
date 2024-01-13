import json
from context import llm

def test_generate():
    json_dict = {"key": "value"}
    system_prompt = "You are great at repeating JSON. Repeat the given JSON."
    user_prompt = json.dumps(json_dict)
    generated_text = llm.generate(system_prompt, user_prompt)
    assert type(generated_text) == str
    assert generated_text == user_prompt

def test_generate_json():
    json_dict = {"key": "value"}
    system_prompt = "You are great at repeating JSON. Repeat the given JSON."
    user_prompt = json.dumps(json_dict)
    generated_json = llm.generate_json(system_prompt, user_prompt)
    assert type(generated_json) == dict
    assert generated_json == json_dict