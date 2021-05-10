import discord
import os

intents = discord.Intents.default()
intents.members = True

client = discord.Client(intents=intents)

with open("token.txt") as f:
    TOKEN = f.read()

@client.event
async def on_ready():
    print("logged in\n")

# 削除メッセージ復元
@client.event
async def on_message_delete(message):
    m = str(message.content)
    m = m.replace("```", "")

    if message.author.bot:
        return
    
    if m == "":
        pass
    else:
        await message.channel.send(f"```py\n@{str(message.author.display_name)} さんのメッセージ\n'{m}'\n```")
    
    for attachment in message.attachments:
        URL = attachment.proxy_url
        embed = discord.Embed(title="削除された画像", url=f"{URL}", description="", color=0x3260a8)
        embed.set_author(name=f"{str(message.author.display_name)} さんが送信した画像", url=f"{URL}", icon_url=message.author.avatar_url)
        embed.set_image(url=f"{URL}")
        embed.set_footer(text="動画の場合や, 画像が表示されない場合はタイトルのURLから飛んでください")
        await message.channel.send(embed=embed)

# 編集メッセージ復元
@client.event
async def on_message_edit(before, after):
	b = str(before.content)
	b = b.replace("```", "")
	a = str(after.content)
	a = a.replace("```", "")

	if before.author.bot:
		return

	await before.channel.send(f"```diff\n{str(before.author.display_name)} さんのメッセージ\n- {b}\n+ {a}\n```")

@client.event
async def on_message(message):

    if message.author.bot:
        return
    
    if message.content == "!ping":
        await message.channel.send("pong!")

if __name__ == "__main__":
    client.run(TOKEN)