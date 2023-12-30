# anki-helper/config.py
#
# Edit these values to better match your setup.

# Some variables like secret keys are better stored as environment variables.
# If using virtualenv, edit <venv>/bin/activate where <venv> is the name of your virtual environment directory.
# in <venv>/bin/activate:
# - at bottom of file, export environment variables
#   - e.g. export DISCORD_BOT_TOKEN="discord.bot.token"
# - at end of deactivate() function, unset variables
#   - e.g. unset DISCORD_BOT_TOKEN

import os

# Discord
DISCORD_BOT_TOKEN=os.getenv("DISCORD_BOT_TOKEN")
# DISCORD_BOT_TOKEN="unsafe.bot.token.anyone.can.see"

# OpenAI
OPENAI_API_KEY=os.getenv("OPENAI_API_KEY")
# OPENAI_API_KEY="unsafe-secret-key-easy-to-steal"

# Anki
DEFAULT_DECKNAME = "anki-helper"
DECKNAME = DEFAULT_DECKNAME

# AnkiConnect
ANKICONNECT_HOST="localhost"
ANKICONNECT_PORT="8765"
ANKICONNECT_ADDRESS = f"http://{ANKICONNECT_HOST}:{ANKICONNECT_PORT}"