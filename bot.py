import discord
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

bot.run('TU_TOKEN_DE_DISCORD')




                              
