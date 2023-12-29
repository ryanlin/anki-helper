import anki
import llm

def generate_flashcard(query: str):
    llm_response = llm.give_me_a_json(query)
    card_creation_response = anki.create_card(llm_response)
    return card_creation_response, llm_response
