import discord
from datetime import datetime

#token.txtファイルからTOKENの読み込み
with open("token.txt") as f:
	TOKEN = f.read()

client = discord.Client()

@client.event
async def on_ready():
    print("logged in\n")

@client.event
async def on_message(message):
    
    if message.author.bot:
        return

    #Discordアカウント作成日(世界標準時)
    if message.content == "いつ":
        day = message.author.created_at.strftime("%Y/%m/%d")
        print(f"{message.author.name}のアカウント作成日は{day}")
        embed = discord.Embed(title="あなたのアカウント作成日", description=f"{message.author.mention}さん",color=0x2ECC69)
        embed.add_field(name="世界標準時(UTC)",value=day)
        await message.channel.send(embed=embed)

client.run(TOKEN)