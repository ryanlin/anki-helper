import requests
import config
import json
import random

import llm

TEST_JSON = """
{
    "tags": [
        "AI-Generated"
    ],
    "fields": {
        "Key": {
            "value": "283",
            "order": 0
        },
        "Simplified": {
            "value": "趁着",
            "order": 1
        },
        "Traditional": {
            "value": "趁著",
            "order": 2
        },
        "Pinyin.1": {
            "value": "chènzhe",
            "order": 3
        },
        "Pinyin.2": {
            "value": "chen4zhe",
            "order": 4
        },
        "Meaning": {
            "value": "taking advantage of",
            "order": 5
        },
        "Part of speech": {
            "value": "preposition",
            "order": 6
        },
        "Audio": {
            "value": "",
            "order": 7
        },
        "Homophone": {
            "value": "",
            "order": 8
        },
        "Homograph": {
            "value": "",
            "order": 9
        },
        "SentenceSimplified": {
            "value": "他趁着我不在家的时候进了我房间。",
            "order": 10
        },
        "SentenceTraditional": {
            "value": "他趁著我不在家的時候進了我房間。",
            "order": 11
        },
        "SentenceSimplifiedCloze": {
            "value": "他[ ]我不在家的时候进了我房间。",
            "order": 12
        },
        "SentenceTraditionalCloze": {
            "value": "他[ ]我不在家的時候進了我房間。",
            "order": 13
        },
        "SentencePinyin.1": {
            "value": "Tā chènzhe wǒ bù zàijiā de shíhou jìnle wǒ fángjiān.",
            "order": 14
        },
        "SentencePinyin.2": {
            "value": "Ta1 chen4zhe wo3 bu4 zai4 jia1 de shi2hou jin4 le wo3 fang2jian1.",
            "order": 15
        },
        "SentenceMeaning": {
            "value": "He entered my room while I was not at home.",
            "order": 16
        },
        "SentenceAudio": {
            "value": "",
            "order": 17
        },
        "SentenceImage": {
            "value": "",
            "order": 18
        }
    },
    "modelName": "HSK"
}
"""

def put_stuff_in_json(note: dict) -> dict:
    new_fields = {
      "deckName": config.DECK_NAME,
    }
    note.update(new_fields)
    note["fields"]["Key"] = note["fields"]['Simplified']
    return note

def create_card_from_json(json_dict: dict):
    url =  config.ANKICONNECT_ADDRESS
    headers = {'Content-Type': 'application/json'}
    data = {
        "action": "addNote",
        "version": 6,
        "params": {
            "note": json_dict  # Ensure this is a list of notes
        }
    }
    dumped = json.dumps(data)
    response = requests.post(url, data=dumped, headers=headers)
    response_json = response.json()
    print(response_json)
    return response_json

def create_card(note_dict: dict):
    modified_note = put_stuff_in_json(note_dict)
    return create_card_from_json(modified_note)