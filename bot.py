# 디스코드 
import discord
# OpenAI
from openai import OpenAI
# 인공지능 비서
from assistants import assist

client_AI = OpenAI()

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user} 로그인 완료')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('지피티야'):
        await message.channel.send(assist(message.content))

client.run('디스코드 챗봇 키')