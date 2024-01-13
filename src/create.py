import config
import anki.anki as anki
import ankigpt.ankigpt as ankigpt

deck_name = config.default_deckname
model_name = config.default_modelname

def generate_and_add_card(query: str):
    note_json: dict = ankigpt.generate_note(query)
    note_id: int = anki.add_note(note_json)
    return note_json, note_id