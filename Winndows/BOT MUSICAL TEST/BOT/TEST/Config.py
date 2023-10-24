import discord
from discord.ext import commands
from discord.utils import get

from discord import Intents

TOKEN = 'MTEyMDE2NDQ0NDIwMzQwMTI2Ng.G0e3GX.t7WSZ95FZE_DpAdHGtWtYAmRVcEUsWXvjHCauM'

intents = Intents.default()
intents.messages = True
intents.members = True

bot = commands.Bot(command_prefix='xxx', intents=intents)

@bot.command()
async def p(ctx, url):
    voice_channel = ctx.author.voice.channel
    voice_client = get(bot.voice_clients, guild=ctx.guild)

    if voice_client is not None:
        await voice_client.move_to(voice_channel)
    else:
        voice_client = await voice_channel.connect()

    voice_client.play(discord.FFmpegPCMAudio(url))

bot.run(TOKEN)
