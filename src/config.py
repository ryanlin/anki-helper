"""Variables shared between modules.

Secret keys should be set as environment variables.
"""

import os

DISCORD_KEY = os.getenv("DISCORD_BOT_TOKEN")
OPENAI_KEY = os.getenv("OPENAI_API_KEY")

default_deckname = "anki-helper"
default_modelname = "HSK"
ankiconnect_url = "http://localhost:8765"