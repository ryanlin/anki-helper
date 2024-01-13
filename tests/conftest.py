import os
import sys
import pytest

# Add project root path
project_root_path = os.path.abspath(
    os.path.join(os.path.dirname(__file__),'..')
    )
sys.path.insert(0, project_root_path)

# Add project src path
project_src_path = os.path.abspath(
    os.path.join(project_root_path, 'src')
    )
sys.path.insert(0, project_src_path)

import anki.ankiconnect as ankiconnect
import anki.anki as anki
import ankigpt.llm as llm
import ankigpt.ankigpt as ankigpt
import create

@pytest.fixture
def deck_name():
    name = "[test] deck"
    yield name
    params = {"decks": [name], "cardsToo": True}
    anki.ankiconnect.invoke(action='deleteDecks',**params)

@pytest.fixture
def note_basic(deck_name):
    note = {
        "deckName": deck_name,
        "modelName": "Basic",
        "tags": ["test"],
        "fields": {
            "Front": "Basic Front",
            "Back": "Basic Back"
        }
    }
    return note

@pytest.fixture
def note_hsk(deck_name):
    note = {
        "deckName": deck_name,
        "modelName": "HSK",
        "tags": ["test"],
        "fields": {
            "Key": "感冒",
            "Simplified": "感冒",
            "Traditional": "感冒",
            "Pinyin.1": "gǎnmào",
            "Pinyin.2": "gan3mao4",
            "Meaning": "to catch a cold",
            "Part of speech": "verb",
            "Audio": "",
            "Homophone": "",
            "Homograph": "",
            "SentenceSimplified": "他感冒了，不能去上班。",
            "SentenceTraditional": "他感冒了，不能去上班。",
            "SentenceSimplifiedCloze": "他[ ]了，不能去上班。",
            "SentenceTraditionalCloze": "他[ ]了，不能去上班。",
            "SentencePinyin.1": "Tā gǎnmào le, bùnéng qù shàngbān.",
            "SentencePinyin.2": "Ta1 gan3mao4 le, bu4neng2 qu4 shang4ban1.",
            "SentenceMeaning": "He has a cold and can't go to work.",
            "SentenceAudio": "",
            "SentenceImage": ""
        }
    }
    return note

@pytest.fixture
def note_basic_with_missing_deckname_key():
    note = {
        "modelName": "Basic",
        "tags": ["test"],
        "fields": {
            "Front": "Basic Front",
            "Back": "Basic Back"
        }
    }
    return note

@pytest.fixture
def query_1():
    yield "菠萝"