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
rolesPermissions = {
    "administrador": [],
    "usuario": [],
    "particiante": [],
    "visitante": [],
    }
autoEnableVisitor = False
eventRole = None

# 2. Canais
eventChannels = {
    "voice": None,
    "ping": None,
    "split": None,
    "ranking": None,
    }
autoCreateTopic = False

# 3. Espólios
adminFee = 10
autoEnableSplit = True

# 4. Xp/hora
xpModifier = 100
xpBaseLevel = 100 # Constante
autoMessageLevel = ''
levelRoles = {}
autoMessageRoles = {}

# Predefinições
standardEventTypes = ["evento"]
presets = {
    "id": [],
    "tipo": [],
    "pode participar": [],
    "canal de voz": [],
    "permitir visitante": [],
    "habilitar split": [],
    "habilitar tópico": [],
    "confirmação de inscrição": [],
    "incluir descrição": [],
}


bot.run(os.getenv("BOT_KEY"))