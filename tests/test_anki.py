import pytest
from conftest import anki, ankiconnect

def test_get_all_decks():
    decks = anki.get_all_decks()
    assert decks != None

def test_get_deck_stats():
    decks = anki.get_all_decks()
    deck_stats = anki.get_deck_stats(decks[0])
    stats_format = {
        "deck_id": 0,
        "name": "",
        "new_count": 0,
        "learn_count": 0,
        "review_count": 0,
        "total_in_deck": 0
    }
    assert deck_stats.keys() == stats_format.keys()

def test_create_deck(deck_name):
    deck_id = anki.create_deck(deck_name)
    assert type(deck_id) == int

def test_add_note_basic(deck_name, note_basic):
    anki.create_deck(deck_name)
    note_id = anki.add_note(note_basic)
    assert type(note_id) == int
    
    # cleanup
    params = {"notes": [note_id]}
    ankiconnect.invoke('deleteNotes', **params)

def test_add_note_hsk(deck_name, note_hsk):
    anki.create_deck(deck_name)
    note_id = anki.add_note(note_hsk)
    assert type(note_id) == int

    # cleanup
    params = {"notes": [note_id]}
    ankiconnect.invoke('deleteNotes', **params)

def test_add_note_with_missing_deckname(
        deck_name, 
        note_basic_with_missing_deckname_key):
    anki.create_deck(deck_name)
    with pytest.raises(Exception, match=r"deckName"):
        anki.add_note(note_basic_with_missing_deckname_key)
