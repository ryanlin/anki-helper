# ankiconnect.py

# wrapper for requests to ankiconnect.
# https://foosoft.net/projects/anki-connect/

import json
import urllib.request

DEFAULT_URL = "http://localhost:8765"
url = DEFAULT_URL

def format_request(action, **params) -> dict:
    return {'action': action, 'params': params, 'version': 6}

def request(action, **params):
    requestJson = json.dumps(format_request(action, **params)).encode('utf-8')
    response = json.load(
        urllib.request.urlopen(urllib.request.Request(url, requestJson)))
    return response

def invoke(action, **params):
    requestJson = json.dumps(
        format_request(action, **params)).encode('utf-8')
    response = json.load(
        urllib.request.urlopen(urllib.request.Request(url, requestJson)))
    if len(response) != 2:
        raise Exception('response has an unexpected number of fields')
    if 'error' not in response:
        raise Exception('response is missing required error field')
    if 'result' not in response:
        raise Exception('response is missing required result field')
    if response['error'] is not None:
        if 'deckName' in response['error']:
            raise KeyError(response['error'])
        else:
            raise Exception(response['error'])
    return response

def invoke_old(action, **params):
    requestJson = json.dumps(format_request(action, **params)).encode('utf-8')
    response = json.load(urllib.request.urlopen(urllib.request.Request(DEFAULT_URL, requestJson)))
    if len(response) != 2:
        raise Exception('response has an unexpected number of fields')
    if 'error' not in response:
        raise Exception('response is missing required error field')
    if 'result' not in response:
        raise Exception('response is missing required result field')
    if response['error'] is not None:
        raise Exception(response['error'])
    return response['result']

def get_deck_names_and_ids() -> dict:
    return invoke(action='deckNamesAndIds')

def find_deck_id(deckName: str) -> str:
    decks = invoke(action='deckNamesAndIds')
    if deckName in decks:
        return decks[deckName]
    else:
        return None

def create_deck(deckName: str) -> dict:
    deck = invoke(action='createDeck', deck=deckName)
    return deck

def delete_deck(deckName: str, cardsToo: bool = True) -> dict:
    decks = [deckName]
    result = invoke(action='deleteDecks', decks=decks, cardsToo=cardsToo)
    return result

def delete_decks(decks: list[str], cardsToo: bool = True) -> dict:
    # broken do not use
    result = invoke(action='deleteDecks', decks=decks, cardsToo=cardsToo)
    return result

def find_notes(query) -> dict:
    result = invoke(action='findNotes', query=query)
    return result

def get_note_info(note_id: int) -> dict:
    result = invoke(action='notesInfo', notes=[note_id])
    return result

def get_notes_info(notes: list[int]) -> dict:
    result = invoke(action='notesInfo', notes=notes)
    return result