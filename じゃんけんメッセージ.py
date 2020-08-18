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

    if message.content == "じゃんけん":
        await message.channel.send("最初はグー、じゃんけん")

        jkbot = random.choice(("グー", "チョキ", "パー"))
        draw = "あいこ！"
        wn = "あなたの勝ち！"
        lst = "私の勝ち！"

        def jankencheck(m):
            return (m.author == message.author) and (m.content in ['グー', 'チョキ', 'パー'])

        reply = await client.wait_for("message", check=jankencheck)
        if reply.content == jkbot:
            judge = draw
        else:
            if reply.content == "グー":
                if jkbot == "チョキ":
                    judge = wn
                else:
                    judge = lst

            elif reply.content == "チョキ":
                if jkbot == "パー":
                    judge = wn
                else:
                    judge = lst

            else:
                if jkbot == "グー":
                    judge = wn
                else:
                    judge = lst

        await message.channel.send(judge)

client.run(TOKEN)