import botrun
import discord
from discord.ext import commands
import logging
import random

logging.basicConfig(level=logging.INFO)

description = '''An example bot to showcase the discord.ext.commands extension
module.
There are a number of utility commands being showcased here.'''
bot = commands.Bot(command_prefix='.', description=description)
client = discord.Client()

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command()
async def add(left : int, right : int):
    """Adds two numbers together."""
    await bot.say(left + right)

@bot.command(description='For when you wanna settle the score some other way')
async def choose(*choices : str):
    """Chooses between multiple choices."""
    await bot.say(random.choice(choices))

@bot.command()
async def joined(member : discord.Member):
    """Says when a member joined."""
    await bot.say('{0.name} joined in {0.joined_at}'.format(member))

@bot.group(pass_context=True)
async def cool(ctx):
    """Says if a user is cool.
    In reality this just checks if a subcommand is being invoked.
    """
    if ctx.invoked_subcommand is None:
        await bot.say('No, {0.subcommand_passed} is not cool'.format(ctx))

@cool.command(name='bot')
async def _bot():
    """Is the bot cool?"""
    await bot.say('Yes, the bot is cool.')

@cool.command(name='limp_noodle')
async def _limp():
    """Is limp_noodle cool?"""
    await bot.say('Yes, limp_noodle is always cool.')

@bot.event
async def on_message(message):
    if "nooo" in message.content:
        await bot.send_message(message.channel, 'VEGETA YES!')
    if "christmas" in message.content:
        await bot.send_message(message.channel, 'Christmas is about friendship and family and KILLING SANTA')
    if "can i" in message.content:
        await bot.send_message(message.channel, 'no')
        await bot.process_commands(message)



bot.run(botrun.token)
