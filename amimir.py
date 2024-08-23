import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

# Charger les variables d'environnement à partir du fichier .env
load_dotenv()

# Remplacez 'YOUR_BOT_TOKEN' par le token de votre bot
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.messages = True  # Activer l'intent pour écouter les messages

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Le bot est prêt. Connecté en tant que {bot.user}')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    print(f"Message reçu de {message.author}: {repr(message.content)}")  # Affiche le contenu du message pour le débogage

    if "bonne nuit" in message.content.lower():
        await message.channel.send(f'Bonne nuit, {message.author.mention} !')

    await bot.process_commands(message)

bot.run(TOKEN)