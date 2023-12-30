from . import ankiconnect

DEFAULT_DECKNAME = "Default"

def create_deck(deckName: str) -> dict:
    params = {"deck": deckName}
    try:
        res = ankiconnect.invoke(action='createDeck',**params)
        return res
    except Exception:
        raise

def add_note(note: dict) -> dict:
    params = {"note": note}
    try:
        response = ankiconnect.invoke(action='addNote',**params)
        return response
    except Exception:
        raise

def create_note_from_json(json: dict) -> dict:
    # bandaid fix for jsons w weird or missing mandatory note fields
    # ideas:
    # - get LLM to fill these properly
    # - implement commands to set deckName and stuff 
    try:
        json["deckName"] = DEFAULT_DECKNAME
        json["fields"]["Key"] = json["fields"]["Simplified"]
        return json
    except:
        raise

def add_note_from_json(json: dict) -> dict:
    note = create_note_from_json(json)
    try:
        response = add_note(note)
        return response
    except Exception:
        raise