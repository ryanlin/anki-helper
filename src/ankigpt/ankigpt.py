"""Generates JSON usable with AnkiConnect from natural language queries.

Currently designed for HSK Chinese flashcards.
Queries can be Chinese, pinyin, or english.

Example Usage:
    note_json: dict = ankigpt.generate_note("苹果")

Unofficially supported usage that sometimes work:
    note_2: dict = ankigpt.generate_note("跑步 in deck sports")
    note_3: dict = ankigpt.generate_note(
        "仔细 with example 他好仔细地学习"
    )
"""

import config
import ankigpt.llm as llm

ANKIHELPER_INSTRUCTION = "\nYou create Anki cards based on the user input. The user input will be Chinese characters, pinyin, and/or english.\n"

DECKNAME_INSTRUCTION = f"\nIf a deck name is not specified in the user query, pair the key \"deckName\" with the value \"{config.default_deckname} \" in the JSON.\n"

MODELNAME_INSTRUCTION = f"\nIf a model name is not specified in the user query, pair the key \"modelName\" with the value \"{config.default_modelname}\" in the json.\n"

EXAMPLES_HSK = f"""
Your JSON should NOT include any keys or fields other than the ones shown in the given examples.

Examples:

User:
便宜

You:
{{
    "deckName": {config.default_deckname},
    "modelName": {config.default_modelname},
    "tags": ["AI-Generated"],
    "fields": {{
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
    }}
}}

User:
打篮球 in deck sports

You:
{{
    "deckName": "sports",
    "modelName": {config.default_modelname}",
    "tags": ["AI-Generated"],
    "fields": {{
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
    }}
}}
"""

def generate_note(query: str) -> dict:
    system_prompt = "".join(
        [
            ANKIHELPER_INSTRUCTION,
            DECKNAME_INSTRUCTION,
            MODELNAME_INSTRUCTION
        ]
    )
    note_json = llm.generate_json(
        system_prompt, 
        query,
        EXAMPLES_HSK
    )
    return note_json

