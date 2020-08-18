import discord
import random

#token.txtファイルからTOKENの読み込み
f = open("token.txt")
TOKEN = f.read()
f.close()

client = discord.Client()

@client.event
async def on_ready():
    print("logged in")
    print("")


@client.event
async def on_message(message):

    if message.author.bot:
        return
    
    if message.content == "おみくじ":
        embed2 = discord.Embed(title="おみくじ", description=f"{message.author.mention}さんの今日の運勢",color=0x03fc90)
        embed2.set_thumbnail(url=message.author.avatar_url)
        embed2.add_field(name="[運勢]", value=random.choice(("大吉", "中吉", "小吉", "吉", "凶", "大凶")), inline=False)
        embed2.add_field(name="[総合運]", value=random.choice(("★★★★★", "★★★★☆", "★★★☆☆", "★★☆☆☆", "★☆☆☆☆")), inline=False)
        embed2.add_field(name="[恋愛運]", value=random.choice(("★★★★★", "★★★★☆", "★★★☆☆", "★★☆☆☆", "★☆☆☆☆")), inline=False)
        embed2.add_field(name="[金運]", value=random.choice(("★★★★★", "★★★★☆", "★★★☆☆", "★★☆☆☆", "★☆☆☆☆")), inline=False)
        embed2.add_field(name="[健康運]", value=random.choice(("★★★★★", "★★★★☆", "★★★☆☆", "★★☆☆☆", "★☆☆☆☆")), inline=False)
        #メッセージは適当
        embed2.add_field(name="[一言アドバイス]", value=random.choice(("一生懸命頑張ると吉", "無理をしない程度に頑張ると吉", "早く寝ると吉", "一日楽しむと吉", "趣味に没頭すると吉")), inline=False)
        await message.channel.send(embed=embed2)

client.run(TOKEN)