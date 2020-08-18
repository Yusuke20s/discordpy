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
    
    if message.content == "slot":
        la = [":poop:", ":imp:", ":middle_finger:", ":meat_on_bone:", ":seven:", ":yum:"]
        lb = [":poop:", ":imp:", ":middle_finger:", ":meat_on_bone:", ":seven:", ":yum:"]
        lc = [":poop:", ":imp:", ":middle_finger:", ":meat_on_bone:", ":seven:", ":yum:"]
        sa = str(random.choices(la))
        sb = str(random.choices(lb))
        sc = str(random.choices(lc))

        sa = sa.lstrip("['")
        sa = sa.rstrip("']")

        sb = sb.lstrip("['")
        sb = sb.rstrip("']")

        sc = sc.lstrip("['")
        sc = sc.rstrip("']")

        slot = sa + sb + sc
        embed = discord.Embed(title="スロット", description=f"{message.author.mention}さん 揃うかな？",color=0xffd700)
        #777
        if "seven" in sa and "seven" in sb and "seven" in sc:
            embed.add_field(name="おめでとう！", value=slot)
            embed2 = discord.Embed(title="JACKPOT !!", description=f"{message.author.mention}さん おめでとう！",color=0x31ff12)
            embed2.add_field(name="おめでとう！", value="これが出る確率は 1/91125 です！")
            embed2.add_field(name="すごすぎます！", value="あなたは神です！")
            await message.channel.send(embed=embed)
            await message.channel.send(embed=embed2)
            await message.channel.send(f"@everyone {str(message.author.name)}が7を3つ揃えました！")
            await message.channel.send("これが出る確率は 1/91125 です！")
        #肉*3
        elif "meat_on_bone" in sa and "meat_on_bone" in sb and "meat_on_bone" in sc:
            embed.add_field(name="おめでとう！", value=slot)
            embed2 = discord.Embed(title="おめでとう！", description=f"{message.author.mention}さん おめでとう！",color=0x2cde12)
            embed2.add_field(name="おめでとう！", value="これが出る確率は 64/91125 です！")
            embed2.add_field(name="もっと頑張ろう！", value="1/91125 を目指して頑張ろう！")
            await message.channel.send(embed=embed)
            await message.channel.send(embed=embed2)
            await message.channel.send(f"@everyone {str(message.author.name)}が肉を3つ揃えました！")
            await message.channel.send("これが出る確率は 64/91125 です！")
        #中指*3
        elif "middle_finger" in sa and "middle_finger" in sb and "middle_finger" in sc:
            embed.add_field(name="ドンマイ！", value=slot)
            embed2 = discord.Embed(title="おめでとう？", description=f"{message.author.mention}さん ドンマイ！",color=0xb03c25)
            embed2.add_field(name="もっと頑張ろう！", value="1/91125 を目指して頑張ろう！")
            await message.channel.send(embed=embed)
            await message.channel.send(embed=embed2)
        #poop*3
        elif "poop" in sa and "poop" in sb and "poop" in sc:
            embed.add_field(name="おめでとう！", value=slot)
            embed2 = discord.Embed(title="おめでとう？", description=f"{message.author.mention}さん ﾌﾞﾘﾌﾞﾘﾌﾞﾘﾌﾞﾘｭﾘｭﾘｭﾘｭﾘｭﾘｭ！！！！！！ﾌﾞﾂﾁﾁﾌﾞﾌﾞﾌﾞﾁﾁﾁﾁﾌﾞﾘﾘｲﾘﾌﾞﾌﾞﾌﾞﾌﾞｩｩｩｩｯｯｯ！！！！！！！",color=0xb07a3f)
            embed2.add_field(name="もっと頑張ろう！", value="1/91125 を目指して頑張ろう！")
            await message.channel.send(embed=embed)
            await message.channel.send(embed=embed2)
        #その他のやつ*3
        elif sa == sb == sc:
            embed.add_field(name="おめでとう！", value=slot)
            embed2 = discord.Embed(title="おめでとう！", description=f"{message.author.mention}さん おめでとう！",color=0x05e6ff)
            embed2.add_field(name="もっと頑張ろう！", value="1/91125 を目指して頑張ろう！")
            await message.channel.send(embed=embed)
            await message.channel.send(embed=embed2)
        #なにか*2
        elif sa == sb or sb == sc or sc == sa:
            embed.add_field(name="惜しい！頑張って！", value=slot)
            await message.channel.send(embed=embed)
        else:
            embed.copy()
            embed.add_field(name="揃うまで頑張ろう！", value=slot)
            embed.copy()
            await message.channel.send(embed=embed)

client.run(TOKEN)