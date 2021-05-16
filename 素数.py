import discord

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

    if message.content.endswith("までの素数"):
        x = message.content

        number_dict={"０":"0","１":"1","２":"2","３":"3","４":"4","５":"5","６":"6","７":"7","８":"8","９":"9"}
        number_dict2={"0":"0","1":"1","2":"2","3":"3","4":"4","5":"5","6":"6","7":"7","8":"8","9":"9"}
        number_dict.update(**number_dict2)

        x = x.rstrip("までの素数")

        if not x.isdigit():
            await message.channel.send("自然数を入力してください")
            return

        number_list = list(x)
        number_list2 = []

        for val in number_list:
            #print(number_dict[val], end="")
            number_list2.append(number_dict[val])

        number = "".join(number_list2)

        if 1 == int(number):
            embed = discord.Embed(title=f"{number}までの素数", description=" ", color=0xf54242)
            embed.add_field(name="なし", value="1は素数ではありません")
            await message.channel.send(embed=embed)
            return

        if 2400 < int(number):
            embed = discord.Embed(title=f"{number}までの素数", description=" ", color=0xdb0909)
            embed.add_field(name="エラー", value="送信量の上限を越えてしまうため送信できません.")
            await message.channel.send(embed=embed)
            return

        if 1 < int(number):
            i = 2
            sosu_list = []
            while i <= int(number):
                j = 2
                while not ( i % j ==0):
                    j = j + 1
                if i == j:
                    sosu_list.append(i)
                i = i + 1

            i = 2
            sosu_list1 = []
            while i <= int(number) and i <= 1240:
                j = 2
                while not ( i % j ==0):
                    j = j + 1
                if i == j:
                    sosu_list1.append(i)
                i = i + 1
        
            sosu1 = str(sosu_list1)
            sosu1 = sosu1.lstrip("[")
            sosu1 = sosu1.rstrip("]")
            embed1 = discord.Embed(title=f"{number}までの素数", description=" ", color=0xf58742)
            embed1.add_field(name=str(len(sosu_list)) + "個の素数があります", value=sosu1)
            await message.channel.send(embed=embed1)

            if 1248 < int(number):
                i = 1240
                sosu_list2 = []
                while i <= int(number):
                    j = 2
                    while not ( i % j ==0):
                        j = j + 1
                    if i == j:
                        sosu_list2.append(i)
                    i = i + 1

                sosu2 = str(sosu_list2)
                sosu2 = sosu2.lstrip("[")
                sosu2 = sosu2.rstrip("]")
                embed2 = discord.Embed(title=f"{number}までの素数(2)", description=" ", color=0xf58742)
                embed2.add_field(name="2ページ目", value=sosu2)
                await message.channel.send(embed=embed2)

if __name__ == "__main__":
    client.run(TOKEN)