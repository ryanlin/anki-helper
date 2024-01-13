"""Wrapper for requests to ankiconnect.

Simplifies requests to AnkiConnect with the `invoke()` function. Clarifies error messages with error raising. Suggested by AnkiConnect dev: https://foosoft.net/projects/anki-connect/.

Examples:
    response: dict = ankiconnect.invoke("deckNames")

    params = {"deck": "Biology"}
    response = ankiconnect.invoke(action="createDeck",**params)
"""

import json
import urllib.request

DEFAULT_URL = "http://localhost:8765"
url = DEFAULT_URL

def reset_url() -> None:
    global url
    url = DEFAULT_URL

def set_url(new_url: str) -> None:
    global url
    url = new_url

def format_request(action: str, **params) -> dict:
    return {"action": action, "params": params, "version": 6}

def invoke(action: str, **params) -> dict:
    """Makes a request to AnkiConnect to perform an action using given params.

    Args:
        action: desired action from AnkiConnect. Supported actions are named identical to AnkiConnect actions.
        **params: contextual info relevant to the action

    Returns:
        A dict with "result" and "error" keys.

    Raises:
        - Exception: generic error 😭
    """
    # format and send request
    request_dict: dict = format_request(action, **params)
    request_json: str = json.dumps(request_dict).encode("utf-8")
    request = urllib.request.urlopen(urllib.request.Request(url, request_json))
    response: dict = json.load(request)
    
    # Raise errors if any
    if len(response) != 2:
        raise Exception("response has an unexpected number of fields")
    if "error" not in response:
        raise Exception("response is missing required error field")
    if "result" not in response:
        raise Exception("response is missing required result field")
    if response["error"] is not None:
        raise Exception(response["error"])
    
    return response