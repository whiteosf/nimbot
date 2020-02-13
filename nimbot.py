import os

from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
token = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')

@bot.command(name='nim')
async def play_nim(ctx):
    await ctx.send("Still working on it, kiddo.")

bot.run(token)
#Commenting:   See you did a lot. 
# Btw, what does .gitignore contain and is it used in the actual bot work, or just acts as info?

