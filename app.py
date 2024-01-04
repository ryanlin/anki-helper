# main.py
#
# Main entrypoint

# 1. LLM Interaction
#  -> Prompt + Parsing response into JSON 
# 2. Sending JSON object to Anki Connect
#  -> Figure out how to do a shared deck


import config, create
import discord
from discord.ext import commands

# Initialize intents
intents = discord.Intents.default()
intents.message_content = True #v2
intents.messages = True  # Enable message intents

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.command(name='add')
async def add(ctx):
    # Remove the command prefix and the command name from the message to get the raw arguments
    query = ctx.message.content[len(ctx.prefix) + len(ctx.invoked_with) + 1:]

    try: 
        await ctx.send(f'Creating an example with query `{query}` . . .')
        note_id, generated_json  = create.generate_and_add_card(query)

        message = f"Done! Added **{generated_json['fields']['Simplified']}** to deck **{generated_json['deckName']}**"
        formatted_note_info = f"""
            ```
            Key:\t\t {generated_json['fields']['Key']}
            Example:\t\t {generated_json['fields']['SentenceSimplified']}
            ```
        """

        await ctx.send(message + formatted_note_info)
    except Exception as e:
        await ctx.send(f'Uh oh, something went wrong: `'+str(e)+'`')

bot.run(config.DISCORD_BOT_TOKEN)