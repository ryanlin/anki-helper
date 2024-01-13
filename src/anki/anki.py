from . import ankiconnect

def get_all_decks() -> dict:
    response = ankiconnect.invoke(action="deckNames")
    data = response["result"]
    return data

def get_deck_stats(deckName: str) -> dict:
    params = {"decks": [deckName]}
    response = ankiconnect.invoke(action="getDeckStats",**params)
    first_key = next(iter(response["result"]))
    data = response["result"][first_key]
    return data

def create_deck(deckName: str) -> None:
    params = {"deck": deckName}
    response = ankiconnect.invoke(action="createDeck",**params)
    data = response["result"]
    return data

def delete_deck(deckName: str, cardsToo: bool = True) -> dict:
    params = {"decks": [deckName], "cardsToo": cardsToo}
    response = ankiconnect.invoke(action="deleteDecks",**params)
    data = response["result"]
    return data

def delete_decks(decks: list[str], cardsToo: bool = True) -> dict:
    params = {"decks": decks, "cardsToo": cardsToo}
    response = ankiconnect.invoke(action="deleteDecks",**params)
    data = response["result"]
    return data

def add_note(json: dict) -> dict:
    params = {"note": json}
    response = ankiconnect.invoke(action="addNote",**params)
    data = response["result"]
    return data