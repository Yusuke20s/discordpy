import discord
import random

# token.txtファイルからTOKENの読み込み
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
    
    if message.content == "おみくじ":
        stars = ["★★★★★", "★★★★☆", "★★★☆☆", "★★☆☆☆", "★☆☆☆☆"]
        embed = discord.Embed(title="おみくじ", description=f"{message.author.mention}さんの今日の運勢",color=0x03fc90)
        embed.set_thumbnail(url=message.author.avatar_url)
        embed.add_field(name="[運勢]", value=random.choice(("大吉", "中吉", "小吉", "吉", "凶", "大凶")), inline=False)
        embed.add_field(name="[総合運]", value=random.choice(stars), inline=False)
        embed.add_field(name="[恋愛運]", value=random.choice(stars), inline=False)
        embed.add_field(name="[金運]", value=random.choice(stars), inline=False)
        embed.add_field(name="[健康運]", value=random.choice(stars), inline=False)
        #メッセージは適当
        embed.add_field(name="[一言アドバイス]", value=random.choice(("一生懸命頑張ると吉", "無理をしない程度に頑張ると吉", "早く寝ると吉", "一日楽しむと吉", "趣味に没頭すると吉")), inline=False)
        await message.channel.send(embed=embed)

if __name__ == "__main__":
    client.run(TOKEN)