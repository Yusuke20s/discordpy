import discord

from datetime import datetime, timedelta, timezone

intents = discord.Intents.default()
client = discord.Client(intents=intents)

with open("token.txt") as f:
    TOKEN = f.read()

JST = timezone(timedelta(hours=+9), "JST")

prefix = "!"

# value: [prefix, channel_id]
data = {}

@client.event
async def on_ready():
	print("logged in\n")

@client.event
async def on_voice_state_update(member, before, after):

	for guild_id in data:
		if guild_id == member.guild.id:
			try:
				guild_list = data[guild_id]
				channel_id = guild_list[1]
			except:
				pass

	try:
		alert_channel = client.get_channel(channel_id)
	except:
		return

	try:
		afk_channel = member.guild.afk_channel.id
	except:
		afk_channel = 000
	now = datetime.now(JST).strftime("%Y/%m/%d %H:%M:%S")

	if before.channel is None:
		embed = discord.Embed(title="VCに接続しました", description="",color=0x008000)
		embed.set_thumbnail(url=member.avatar_url)
		embed.add_field(name=f"{member.display_name}さん",value=f"{after.channel.name} に参加しました。", inline=False)
		embed.set_footer(text=now)
		await alert_channel.send(embed=embed)
	elif after.channel is None:
		embed = discord.Embed(title="VCから切断しました", description="",color=0xff0000)
		embed.set_thumbnail(url=member.avatar_url)
		embed.add_field(name=f"{member.display_name}さん",value=f"{before.channel.name} から退出しました。", inline=False)
		embed.set_footer(text=now)
		await alert_channel.send(embed=embed)
	elif after.channel.id == afk_channel:
		if before.channel.id == after.channel.id:
			return
		embed = discord.Embed(title="AFKに飛ばされました", description="",color=0x000000)
		embed.set_thumbnail(url=member.avatar_url)
		embed.add_field(name=f"{member.display_name}さん",value="あなたの声は聞こえないよ。", inline=False)
		embed.set_footer(text=now)
		await alert_channel.send(embed=embed)
	elif not after.channel is None:
		if before.channel.id == after.channel.id:
			if not before.self_stream == after.self_stream:
				if after.self_stream is True:
					embed = discord.Embed(title="配信を開始しました", description="",color=0x008000)
					embed.set_thumbnail(url=member.avatar_url)
					embed.add_field(name=f"{member.display_name}さん",value="みんなで見よう！", inline=False)
					embed.set_footer(text=now)
					await alert_channel.send(embed=embed)
				elif after.self_stream is False:
					embed = discord.Embed(title="配信を終了しました", description="",color=0xff0000)
					embed.set_thumbnail(url=member.avatar_url)
					embed.add_field(name=f"{member.display_name}さん",value="またやってね！", inline=False)
					embed.set_footer(text=now)
					await alert_channel.send(embed=embed)
			return
		embed = discord.Embed(title="VCに接続しました", description="",color=0x008000)
		embed.set_thumbnail(url=member.avatar_url)
		embed.add_field(name=f"{member.display_name}さん",value=f"{after.channel.name} に参加しました。", inline=False)
		embed.set_footer(text=now)
		await alert_channel.send(embed=embed)

@client.event
async def on_message(message):

	if message.author.bot:
		return

	# 接頭辞確認
	if message.content == "!!prefix":
		try:
			guild_list = data[message.guild.id]
		except:
			guild_list = ["!", None]
			data[message.guild.id] = guild_list
		try:
			prefix = guild_list[0]
			await message.channel.send(f"このサーバーのPrefixは`{prefix}`です")
		except:
			pass
		return

	# 接頭辞リセット
	elif message.content == "!!!prefix":
		try:
			guild_list = data[message.guild.id]
		except:
			guild_list = ["!", None]
			data[message.guild.id] = guild_list
		try:
			guild_list[0] = "!"
			data[message.guild.id] = guild_list
			await message.channel.send("Prefixを`!`にリセットしました")
		except:
			pass
		return

	# 接頭辞取得
	try:
		guild_list = data[message.guild.id]
	except:
		guild_list = ["!", None]
		data[message.guild.id] = guild_list

	prefix = guild_list[0]

	if not message.content.startswith(prefix):
		return

	content = message.content.lstrip(prefix).strip()

	if content.startswith("setprefix"):
		try:
			new_prefix = content.lstrip("setprefix").strip()
			guild_list[0] = str(new_prefix)
			data[message.guild.id] = guild_list
			await message.channel.send(f"Prefixを`{new_prefix}`に変更しました")
		except:
			pass

	content = content.lower()

	if content == "setchannel":
		try:
			guild_list[1] = message.channel.id
			data[message.guild.id] = guild_list
			await message.channel.send("チャンネルを設定しました")
		except:
			pass

if __name__ == "__main__":
	client.run(TOKEN)