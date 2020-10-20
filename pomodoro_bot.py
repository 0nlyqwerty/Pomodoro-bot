import discord
from discord.ext import commands
import os
import platform

# Get token from ./token.txt
CURRENT_DIR_PATH = os.path.dirname(__file__)
if CURRENT_DIR_PATH == "":
    CURRENT_DIR_PATH = "."
if platform.system() == "Linux":
    CURRENT_DIR_PATH = CURRENT_DIR_PATH + "/"
elif platform.system() == "Windows":
    CURRENT_DIR_PATH = CURRENT_DIR_PATH + "\\"
t = open(CURRENT_DIR_PATH + "token.txt", "r", encoding="utf-8")
TOKEN = t.read().split()[0]

version = '1.0.0'
game = discord.Game(f"Pomodoro Bot {version}")
bot = commands.Bot(command_prefix='!', status=discord.Status.online,
                   activity=game, help_command=None)


@bot.event
async def on_ready():
    print(" ---------------------")
    print(" POMODORO BOT on_ready")
    print(" ---------------------")


bot.run(TOKEN)
