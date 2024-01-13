from context import create, ankiconnect

def test_generate_and_add_card_hsk(note_hsk):
  query = "菠萝"
  note_json, note_id = create.generate_and_add_card(query)
  expected_keys = note_hsk.keys()
  assert note_json.keys() == expected_keys
  assert type(note_id) == int

  # cleanup
  params = {"notes": [note_id]}
  ankiconnect.invoke('deleteNotes', **params)