import discord
import os
import server
from discord.ext import tasks

intents = discord.Intents.default()
intents.members = True
intents.presences = True

client = discord.Client(intents=intents)

# token.txtファイルからTOKENの読み込み
with open("token.txt") as f:
    TOKEN = f.read()

@client.event
async def on_ready():
	print("logged in\n")
	loop.start()

GUILD_ID = 000000000000000000
CHANNEL_ID = 000000000000000000

bot_id = [000000000000000000]

@tasks.loop(seconds=60)
async def loop():
    guild = client.get_guild(GUILD_ID)
    channel = client.get_channel(CHANNEL_ID)
    for member in guild.members:
        if "online" in member.status:
            pass
        else:
            if member.id in bot_id:
                await channel.send(f"{member.display_name}がオフラインです")

@client.event
async def on_message(message):

	if message.author.bot:
		return

	if message.content == "!ping":
		await message.channel.send("pong!")

if __name__ == "__main__":
    client.run(TOKEN)