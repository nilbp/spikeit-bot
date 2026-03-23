import discord
import os

from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Bot conectado como {bot.user.name}")

@bot.command()
async def hola(ctx):
    await ctx.send("¡Hola!")

bot.run(os.getenv("SPIKEIT_BOT_TOKEN"))




                              
