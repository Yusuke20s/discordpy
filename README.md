# Discordpyファイル  
discordpyを使っているうえで、できたプログラムファイルを用途別に保存しています。  

## 注意事項  
汚すぎるコードです。  
許してください。　　

## 形式  
TOKENは環境変数ではなく、token.txtから読み込むようにしています。  

テンプレ↓
```py
import discord

#token.txtファイルからTOKENの読み込み
with open("token.txt") as f:
	TOKEN = f.open()

client = discord.Client()

@client.event
async def on_ready():
    print("logged in\n")

@client.event
async def on_message(message):

    if message.author.bot:
        return

client.run(TOKEN)
```