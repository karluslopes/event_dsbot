import discord
from dotenv import load_dotenv
import os
load_dotenv()

intents = discord.Intents.all()
bot = discord.Client(intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} está online!')

bot.run(os.getenv("BOT_KEY"))