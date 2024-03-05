import discord
from dotenv import load_dotenv
import os
load_dotenv()

intents = discord.Intents.all()
bot = discord.Client(intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} está online!')



# PARÂMETROS DE CONFIGURAÇÕES
# 1. Permissões

admRoles = []
userRoles = []
participantRoles = []
eventRole = None

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')
bot.run(os.getenv("BOT_KEY"))