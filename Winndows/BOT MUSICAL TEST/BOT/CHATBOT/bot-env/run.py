import discord
from discord.ext import commands
from discord.ext.commands import Bot


# Comando para unir el bot a un canal de voz
@bot.command()
async def join(ctx):
    channel = ctx.author.voice.channel
    await channel.connect()

# Comando para reproducir música
@bot.command()
async def play(ctx, url):
    voice_client = ctx.voice_client

    if not voice_client.is_playing():
        voice_client.stop()
        voice_client.play(discord.FFmpegPCMAudio(url))
        await ctx.send(f'Reproduciendo: {url}')
    else:
        await ctx.send('El bot ya está reproduciendo música.')

# Comando para pausar la música
@bot.command()
async def pause(ctx):
    voice_client = ctx.voice_client
    if voice_client.is_playing():
        voice_client.pause()
        await ctx.send('Música pausada.')

# Comando para reanudar la música
@bot.command()
async def resume(ctx):
    voice_client = ctx.voice_client
    if voice_client.is_paused():
        voice_client.resume()
        await ctx.send('Música reanudada.')

# Comando para desconectar el bot del canal de voz
@bot.command()
async def leave(ctx):
    voice_client = ctx.voice_client
    if voice_client.is_connected():
        await voice_client.disconnect()
        await ctx.send('Bot desconectado.')

# Ejecuta el bot con tu token

intents = discord.Intents.default()
intents.message_content = True

client = bot(intents=intents)
client.run('MTE0NDQ3MDk2NTEyMDY2MzY2Mw.GB0v8T.qckQ2iOMlbC-iG0ozxVyVZoikblrOcvz3oX6mw')


# Configura el prefijo de los comandos del bot
bot = commands.Bot(command_prefix='!')