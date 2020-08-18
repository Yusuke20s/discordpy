# Discordpyファイル  
discordpyを使っているうえで、できたプログラムを用途別にファイルを保存しています。  

## ファイル形式  
TOKENは環境変数ではなく、token.txtから読み込むようにしています。  

テンプレ↓
```py
import discord

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

client.run(TOKEN)
```