import discord, os, glob
import discord.ext, discord.ext.commands
from config import (
    TOGIN,
    WHOCANBOSSME,
    messages,
)
from utils import get_music_folder
import asyncio, random

intents = discord.Intents.default()
intents.message_content = True
bot = discord.ext.commands.Bot(command_prefix="!", intents=intents)
client = discord.Client

@bot.event
async def on_ready():
    print(f'Bot ta as pampa. logado como {bot.user}')

@bot.command(name='play')
async def play(ctx, *, song_name: str):
    if ctx.author.id not in WHOCANBOSSME:
        randomize = random.randrange(0, len(messages))
        await ctx.send(messages[randomize])
        return
    
    if not ctx.author.voice:
        await ctx.send("Você precisa estar em um canal pra usar esse comando")
        return
    
    voice_channel = ctx.author.voice.channel   
    music_folder = get_music_folder()
    song_path = None
    supported_extensions = ['mp3', 'wav', 'ogg', 'flac', 'aac', 'm4a']

    for extension in supported_extensions:
        potential_path = glob.glob(os.path.join(music_folder, f'{song_name}.{extension}'))
        if potential_path:
            song_path = potential_path[0]
            break

    if not song_path:
        await ctx.send(f"A música '{song_name}' não foi encontrada na pasta de músicas.")
        return

    if ctx.voice_client is None:
        voice_client = await voice_channel.connect()
    else:
        voice_client = ctx.voice_client

    if voice_client.is_playing():
        voice_client.stop()

    current_song = song_path
    stop_flag = False

    await ctx.send(f"Tocando: {song_name} em loop")

    while not stop_flag:
        if not voice_client.is_playing():
            voice_client.play(discord.FFmpegOpusAudio(source=current_song))
        await asyncio.sleep(1)
    
@bot.command(name='stop', help='Para a musica que ta tocando')
async def stop(ctx):
    if ctx.author.id not in WHOCANBOSSME:
        randomize = random.randrange(0, len(messages))
        await ctx.send(messages[randomize])
        return
    
    if ctx.voice_client:
        await ctx.voice_client.disconnect()
        await ctx.send("Parando a música.")
    else:
        await ctx.send("O bot não está em um canal de voz.")

if __name__== "__main__":
    bot.run(TOGIN)
