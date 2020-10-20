import discord
import random

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

    if message.content == "じゃんけん":
        j = await message.channel.send("最初はグー、じゃんけん")
        await j.add_reaction("✊")
        await j.add_reaction("✌️")
        await j.add_reaction("✋")

        jkbot = random.choice(("✊", "✌️", "✋"))
        draw = "あいこ！"
        wn = "あなたの勝ち！"
        lst = "私の勝ち！"

        def checkj(reaction, user):
            emoji = str(reaction.emoji)
            if not user == message.author:
                pass
            else:
                return emoji == "✊" or emoji == "✌️" or emoji == "✋"

        reaction, user= await client.wait_for('reaction_add', check=checkj)
        if str(reaction.emoji) == jkbot:
            judge = draw
        else:
            if str(reaction.emoji) == "✊":
                if jkbot == "✌️":
                    judge = wn
                else:
                    judge = lst

            elif str(reaction.emoji) == "✌️":
                if jkbot == "✋":
                    judge = wn
                else:
                    judge = lst

            else:
                if jkbot == "✊":
                    judge = wn
                else:
                    judge = lst

        embed = discord.Embed(title="じゃんけん", description=f"{message.author.mention}さんとの結果",color=0x93b881)
        embed.add_field(name="結果" ,value=f"あなた {str(reaction.emoji)} × {jkbot} BOT", inline=False)
        embed.add_field(name="一言" ,value=judge, inline=False)

        await j.remove_reaction("✊", client.user)
        await j.remove_reaction("✌️", client.user)
        await j.remove_reaction("✋", client.user)
        await j.remove_reaction(str(reaction.emoji), user)
        await j.edit(embed=embed, content=None)

client.run(TOKEN)