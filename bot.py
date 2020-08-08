# Python 3.8.5 code for mathBot

import discord
from discord.ext import commands
from _private import TOKEN, pp as penis_length

from random import randint

description = '''
An example bot to showcase the discord.ext.commands extension module

There are a number of utility commands being showcases here.
'''

# Creates a bot object that all bot commands run through
bot = commands.Bot(command_prefix='_', description=description)

# Runs whenever the bot launches
@bot.event
async def on_ready():
    print()
    print(f'Logged in as {str(bot.user)}')
    print('------')

# A command for adding two numbers or concatenating two strings
@bot.command()
async def add(context, left: str, right: str):
    try:
        left = int(left)
        try:
            right = int(right)
        except Exception:
            left = str(left)
    except Exception:
        pass
    await context.send(left + right)

# A command to roll dice in NdN format
@bot.command()
async def roll(context, dice: str):
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception as e:
        await context.send('Format has to be in NdN please');
        return

    if rolls >= 20:
        rolls = 20
        await context.send('Roll is capped at 20 dice per roll')

    if limit >= 1000:
        limit = 1000
        await context.send('Sides are capped at 1000 sides per die')

    result = ', '.join(str(randint(1, limit)) for r in range(rolls))
    await context.send(result)

@bot.command()
async def repeat(context, *, _input: str):
    try:
        count, message = _input.split(' ', 1)
        count = int(count)

        if count >= 20:
            await context.send('Repeat caps at 20 messages')
            count = 20

        for i in range(count):
            await context.send(message)

    except Exception as e:
        await context.send('Syntax: _repeat times message')

@bot.command()
async def pp(context):
    try:
        await context.send(penis_length[context.author.id])
        return
    except Exception:
        await context.send('Some loser invoked this command')

bot.run(TOKEN)

