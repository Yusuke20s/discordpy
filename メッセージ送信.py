import discord
import asyncio

# token.txtファイルからTOKENの読み込み
with open("token.txt") as f:
    TOKEN = f.read()

client = discord.Client()

@client.event
async def on_ready():
    print("logged in\n")
    asyncio.ensure_future(greeting_gm())

async def greeting_gm():
    while True:
        content = input("送信メッセージを入力: ")
        CHANNEL_ID = input("送信チャンネルIDを入力: ")

        try:
            channel = client.get_channel(int(CHANNEL_ID))
            await channel.send(content)
        except:
            pass

        await asyncio.sleep(1)

if __name__ == "__main__":
    client.run(TOKEN)