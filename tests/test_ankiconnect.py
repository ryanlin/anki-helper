from conftest import ankiconnect

def test_set_url():
    url = "http://localhost:9090"
    ankiconnect.set_url(url)
    assert ankiconnect.url == url

    # Clean up test
    ankiconnect.reset_url()

def test_invoke_response_format():
    response_format = {'result': None, 'error': None}
    response = ankiconnect.invoke('deckNames')
    assert response
    assert len(response) > 0
    assert response_format.keys() == response.keys()