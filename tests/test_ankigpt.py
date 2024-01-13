from context import ankigpt

def test_generate_note_json_hsk(note_hsk):
    note_json = ankigpt.generate_note('礼貌')
    expected_keys = note_hsk.keys()
    assert note_json.keys() == expected_keys
    assert note_json['fields'].keys() == note_json['fields'].keys()