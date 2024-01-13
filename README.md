# AnkiHelper

AnkiHelper is a GPT-based AI assistant that creates entire Chinese flashcards in Anki from just 1 word. Save time while watching shows and instantly create cards with pinyin, translations, and example sentences.

![Anki-Helper Demo](anki-helper-demo.gif)

Interfaceable through a Discord bot, the Anki Helper is currently available for self-hosting and development. WIP!

- [Usage](#usage)
- [Setup](#setup)
- [Development](#development)

## Usage

Once the assistant is [set up](#setup), the bot can be added to the Discord server and used by all members. 

Add cards with `!add` command
```
!add 苹果
```
Experimental
```
!add 跑步 in deck sports
```
```
!add 仔细 with example 他好仔细地学习
```

## Setup

### API Registrations and Keys
1. Register [OpenAI API Account and Key](https://help.openai.com/en/articles/4936850-where-do-i-find-my-api-key)
2. Register [Discord App and Bot Token](https://discord.com/developers/applications)

### Programs
1. Install [Python](https://www.python.org/downloads/)
2. Install [Anki](https://apps.ankiweb.net/)
3. Install [AnkiConnect add-on](https://ankiweb.net/shared/info/2055492159)
4. Clone this repo

### Environment
1. Install Python packages: `pip install requirements.txt`
2. Add Tokens and Keys to environment variables. Make sure the variable names match those in `src/config.py`

### Hosting the App
1. Start Anki with the Anki-Connect add-on
2. Run Anki-Helper: `python3 src/app.py`

### Using the Discord Bot
1. Add bot to server with [generated URL](https://discord.com/developers/docs/getting-started#step-1-creating-an-app).
2. Start using commands in the server! 
    - try: `!add 加油`!

## Development
More info on the [development page](development.md).
### Setup
1. Install packages: `pip install requirements.txt`
2. Install dev packages: `pip install dev-requirements.txt`

### Testing
- Run all tests: `pytest -v`
- Run specific test: `pytest tests\test_name.py -v`

### Roadmap
p0
- ~~Create card from word using LLM.~~
- ~~Add card to an anki deck.~~

p1
- Shared/Live deck collaboration.

### Change log

2024-01-12
- added wrapper module for requests to AnkiConnect
- added basic tests