import os
import random

from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
token = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')

@bot.command(name='nim')
async def play_nim(ctx):
    await ctx.send("Still working on it, kiddo.")

@bot.command(name="flip_coin")
async def flip_coin(ctx):
    await ctx.send(random.choice(["Heads", "Tails"]))

@bot.command(name="add")
async def add(ctx, *args):
    try:
        await ctx.send(sum(*args))
    except:
        await ctx.send("Value error")

@bot.command(name="subtract")
async def sub(ctx, x, y):
    try:
        await ctx.send(x-y)
    except:
        await ctx.send("Value error")

@bot.command(name="multiply")
async def mult(ctx, x, y):
    try:
        await ctx.send(x*y)
    except:
        await ctx.send("Value error")

@bot.command(name="divide")
async def div(ctx, x, y):
    try:
        await ctx.send(x/y)
    except:
        await ctx.send("Value error")
        
@bot.command(name="to_power")
async def pow(ctx, x, y):
    try:
        await ctx.send(x^y)
    except:
        await ctx.send("Value error")

bot.run(token)

