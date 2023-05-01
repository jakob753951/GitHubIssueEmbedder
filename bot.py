import asyncio
from discord.ext import commands
import discord.utils
from discord import Embed
import regex

bot = commands.Bot(command_prefix='.', case_insensitive=True)

@bot.event
async def on_ready():
	print('Connected!')
	print(f'Username: {bot.user.name}')
	print(f'ID: {bot.user.id}')

@bot.event
async def on_message(message):
	if message.author.bot:
		return

	await bot.process_commands(message)

bot.run(token)
