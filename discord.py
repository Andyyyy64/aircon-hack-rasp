import discord
import requests

TOKEN = "" # token for discord bot

client = discord.Client()

@client.event
async def on_ready():
    print("logged in")


@client.event
async def on_message(message):
    if message.author.bot:
        return
    if message.content == "on":
        requests.post("https://ntfy.sh/andy64",
          data="on".encode(encoding='utf-8'))

client.run(TOKEN)




