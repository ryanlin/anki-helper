import ankiconnect

def get_all_decks() -> dict:
    try:
        response = ankiconnect.invoke(action='deckNames')
        data = response['result']
        return data
    except:
        raise

def get_all_models() -> dict:
    try:
        response = ankiconnect.invoke(action='modelNames')
        data = response['result']
        return data
    except:
        raise

def create_deck(deckName: str) -> None:
    params = {"deck": deckName}
    try:
        response = ankiconnect.invoke(action='createDeck',**params)
        data = response['result']
        return data
    except:
        raise

def delete_deck(deckName: str, cardsToo: bool = True) -> dict:
    params = {"decks": [deckName], "cardsToo": cardsToo}
    try:
        response = ankiconnect.invoke(action='deleteDecks',**params)
        data = response['result']
        return data
    except:
        raise

def delete_decks(decks: list[str], cardsToo: bool = True) -> dict:
    params = {"decks": decks, "cardsToo": cardsToo}
    try:
        response = ankiconnect.invoke(action='deleteDecks',**params)
        data = response['result']
        return data
    except:
        raise

def add_note(json: dict) -> dict:
    params = {"note": json}
    try:
        response = ankiconnect.invoke(action='addNote',**params)
        data = response['result']
        return data
    except:
        raise