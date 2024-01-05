from openai import OpenAI
import json

import config

JSON_ONLY_INSTRUCTION = "You are a helpful assistant designed to output JSON. Please respond only with JSON."

JSON_PROPERTIES_INSTRUCTION = "Your JSON should NOT include any fields other than the ones shown in the given examples."

ANKI_HELPER_INSTRUCTION = "You are meant to create Anki cards based on the user input. The user input will be Chinese characters, or Chinese characters and/or pinyin and english."

ANKI_DECKNAME_INSTRUCTION = f"In your JSON, include a top level property \"deckName\" with the value {config.ANKI_DECKNAME}"

ANKI_KEY_INSTRUCTION = f"In your JSON, include a property \"Key\" under \"fields\" with the same value as you would have assigned to the property \"Simplified\" that is also under \"fields\""

FEW_SHOT_INSTRUCTION = """
Examples:

User input:
便宜

You, the JSON machine (make sure not to add any extra fields):
{
    "deckName": "anki-helper",
    "modelName": "HSK",
    "tags": [
        "AI-Generated",
    ],
    "fields": {
        "Key": "便宜",
        "Simplified": "便宜",
        "Traditional": "便宜",
        "Pinyin.1": "piányi",
        "Pinyin.2": "pian2yi5",
        "Meaning": "cheap",
        "Part of speech": "adjective",
        "Audio": "",
        "Homophone": "",
        "Homograph": "",
        "SentenceSimplified": "这件衣服很便宜。",
        "SentenceTraditional": "這件衣服很便宜。",
        "SentenceSimplifiedCloze": "这件衣服很[ ]。",
        "SentenceTraditionalCloze": "這件衣服很[ ]。",
        "SentencePinyin.1": "Zhè jiàn yīfu hěn piányi.",
        "SentencePinyin.2": "Zhe4 jian4 yi1fu hen3 pian2yi.",
        "SentenceMeaning": "These clothes are very cheap.",
        "SentenceAudio": "",
        "SentenceImage": "",
    }
}

User input:
打篮球 to deck sports
basketball

You, the JSON machine (make sure not to add any extra fields):
{
    "deckName": "sports",
    "modelName": "HSK",
    "tags": [
        "AI-Generated"
    ],
    "fields": {
        "Key": "打篮球",
        "Simplified": "打篮球",
        "Traditional": "打籃球",
        "Pinyin.1": "dǎ lánqiú",
        "Pinyin.2": "da3 lan2qiu2",
        "Meaning": "play basketball",
        "Part of speech": "verb",
        "Audio": "",
        "Homophone": "",
        "Homograph": "",
        "SentenceSimplified": "我想打篮球。",
        "SentenceTraditional": "我想打籃球。",
        "SentenceSimplifiedCloze": "我想[ ]。",
        "SentenceTraditionalCloze": "我想[ ]。",
        "SentencePinyin.1": "Wǒ xiǎng dǎ lánqiú.",
        "SentencePinyin.2": "Wo3 xiang3 da3 lan2qiu2.",
        "SentenceMeaning": "I want to play basketball.",
        "SentenceAudio": "",
        "SentenceImage": ""
    },
}
"""

JSON_INSTRUCTION = f"{JSON_ONLY_INSTRUCTION}\n{JSON_PROPERTIES_INSTRUCTION}\n"

ANKI_INSTRUCTION = f"{ANKI_HELPER_INSTRUCTION}"

SYSTEM_PROMPT = f"{JSON_INSTRUCTION}\n{ANKI_INSTRUCTION}\n{FEW_SHOT_INSTRUCTION}"

client = OpenAI(api_key=config.OPENAI_API_KEY)

def generate_note_json(query: str) -> dict:
    completion = client.chat.completions.create(
        model="gpt-4-1106-preview",
        response_format={"type": "json_object"},
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": f"{query}"}])
    note_json_str: str = completion.choices[0].message.content
    note_json: dict = json.loads(note_json_str)
    return note_json