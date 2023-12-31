# ankiconnect.py

# wrapper for requests to ankiconnect.
# https://foosoft.net/projects/anki-connect/

import json
import urllib.request
import config

DEFAULT_URL = "http://localhost:8765"
URL =  config.ANKICONNECT_URL or DEFAULT_URL

def format_request(action, **params) -> dict:
    return {'action': action, 'params': params, 'version': 6}

def invoke(action, **params) -> dict:
    requestJson = json.dumps(
        format_request(action, **params)).encode('utf-8')
    response = json.load(
        urllib.request.urlopen(urllib.request.Request(URL, requestJson)))
    # handle response
    if len(response) != 2:
        raise Exception('response has an unexpected number of fields')
    if 'error' not in response:
        raise Exception('response is missing required error field')
    if 'result' not in response:
        raise Exception('response is missing required result field')
    if response['error'] is not None:
        if 'deckName' in response['error']:
            raise KeyError(response['error'])
        else:
            raise Exception(response['error'])
    return response