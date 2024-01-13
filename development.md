# AnkiHelper Development
Notes for AnkiHelper Development

## Setup
1. Install packages: `pip install requirements.txt`
2. Install dev packages: `pip install dev-requirements.txt`

## Testing
This project kinda uses pytest.
- Run all tests: `pytest -v`
- Run specific test: `pytest tests\test_name.py -v`

## Misc

### Virtual Env Variables
If using a Python virtual environment, environment variables can be add in `<venv>/bin/activate` where `<venv>` is the directory of your virtual environment.

Example environment variables in virtualenv:
```sh
# .venv/bin/activate

deactivate() {
  ...

  # Unset my personal local environment variables
  # These were set at the bottom of this file
  unset OPENAI_API_KEY
  unset DISCORD_BOT_TOKEN
}
...

# My personal local environment variables
# Make sure to unset in deactivate() above
export OPENAI_API_KEY="openai-api-secret-key"
export DISCORD_BOT_TOKEN="discord.bot.token"
```
More info [here](https://stackoverflow.com/a/38645983/14514959).