from anki import anki
import llm

def generate_and_add_card(query: str):
    try:
        llm_response: dict = llm.give_me_a_json(query)
        add_note_response: dict = anki.add_note_from_json(llm_response)
        return add_note_response, llm_response
    except Exception:
        raise