import discord
from dotenv import load_dotenv
from discord.ext import commands    
import os

# Load environment variables from .env file
load_dotenv()

# Ensure you have your bot token in an environment variable named 'DISCORD_BOT_TOKEN'
TOKEN = os.getenv('DISCORD_BOT_TOKEN')
if not TOKEN:
    raise ValueError("No token found. Please set the DISCORD_BOT_TOKEN environment variable.")  

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} - {bot.user.id}')
    print('------')

@bot.command()
async def hello(ctx):
    await ctx.send('Hello! I am your Discord bot.')

bot.run(TOKEN)
