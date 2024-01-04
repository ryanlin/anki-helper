import config
import anki
import llm

DECKNAME = config.ANKI_DECKNAME or "Default"    

def add_stuff_to_json(json: dict) -> dict:
    # bandaid fix for jsons w weird or missing mandatory note fields
    # ideas:
    # - re-prompt LLM to correct errors
    # - implement commands for user to set deckName and stuff 
    json["deckName"] = DECKNAME
    anki.create_deck(DECKNAME)
    # anki.create_model(json, modelName)
    json["fields"]["Key"] = json["fields"]["Simplified"]
    return json

def generate_and_add_card(query: str):
    # Keep prompting until the LLM gives us something usable
    # bandaid: add the fields ourselves
    user_prompt = query
    generated_json = None
    while True:
        try:
            generated_json: dict = llm.generate_note_json(user_prompt)
            note_id: dict = anki.add_note(generated_json)
            response = note_id, generated_json
            return note_id, generated_json
        except KeyError as e:
            print(f"Key Error: {e}. Applying bandaid...")
            # tell llm to try again
            # ideas: make a prompt including the missing keys and reprompt

            # bandaid: add fields with default values
            modified_json = add_stuff_to_json(generated_json)
            note_id: int = anki.add_note(modified_json)
            return note_id, modified_json
        except:
            raise