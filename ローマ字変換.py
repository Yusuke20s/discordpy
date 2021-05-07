import discord

# token.txtファイルからTOKENの読み込み
with open("token.txt") as f:
    TOKEN = f.read()

client = discord.Client()

@client.event
async def on_ready():
    print("logged in\n")

# ローマ字平仮名変換(これですべてではない)
# 重ね文字
hiragana_dict1={"kka":"っか","kki":"っき","kku":"っく","kke":"っけ","kko":"っこ"}
h1d2={"ssa":"っさ","ssi":"っし","ssu":"っす","sse":"っせ","sso":"っそ"}
h1d3={"tta":"った","tti":"っち","ttu":"っつ","tte":"って","tto":"っと"}
h1d4={"hha":"っは","hhi":"っひ","hhu":"っふ","hhe":"っへ","hho":"っほ"}
h1d5={"mma":"っま","mmi":"っみ","mmu":"っむ","mme":"っめ","mmo":"っも"}
h1d6={"rra":"っら","rri":"っり","rru":"っる","rre":"っれ","rro":"っろ"}
h1d6={"yya":"っや","yyi":"っい","yyu":"っゆ","yye":"っいぇ","yyo":"っよ"}
h1d7={"wwa":"っわ","wwi":"っうぃ","wwu":"っう","wwe":"っうぇ","wwo":"っを"}

h1d8={"xtu":"っ","xya":"ゃ","xyu":"ゅ","xyo":"ょ"}
h1d9={"ltu":"っ","lya":"ゃ","lyu":"ゅ","lyo":"ょ"}
h1d10={"xa":"ぁ","xi":"ぃ","xu":"ぅ","xe":"ぇ","xo":"ぉ"}
h1d11={"shi":"し","chi":"ち","tsu":"つ"}

hiragana_dict1.update(**h1d2, **h1d3, **h1d4, **h1d5, **h1d6, **h1d7, **h1d8, **h1d9, **h1d10, **h1d11)

# 基本変換
hiragana_dict2={"ka":"か","ki":"き","ku":"く","ke":"け","ko":"こ"}
h2d2={"sa":"さ","si":"し","su":"す","se":"せ","so":"そ"}
h2d3={"ta":"た","ti":"ち","tu":"つ","te":"て","to":"と"}
h2d4={"nn":"ん"}
h2d5={"ha":"は","hi":"ひ","hu":"ふ","he":"へ","ho":"ほ"}
h2d6={"ma":"ま","mi":"み","mu":"む","me":"め","mo":"も"}
h2d7={"ra":"ら","ri":"り","ru":"る","re":"れ","ro":"ろ"}
h2d8={"wa":"わ","wi":"うぃ","wu":"う","we":"うぇ","wo":"を"}

h2d9={"ga":"が","gi":"ぎ","gu":"ぐ","ge":"げ","go":"ご"}
h2d10={"za":"ざ","zi":"じ","zu":"ず","ze":"ぜ","zo":"ぞ"}
h2d11={"da":"だ","di":"ぢ","du":"づ","de":"で","do":"ど"}
h2d12={"ba":"ば","bi":"び","bu":"ぶ","be":"べ","bo":"ぼ"}
h2d13={"pa":"ぱ","pi":"ぴ","pu":"ぷ","pe":"ぺ","po":"ぽ"}

h2d14={"kya":"きゃ","kyi":"きぃ","kyu":"きゅ","kye":"きぇ","kyo":"きょ"}
h2d15={"sya":"しゃ","syi":"しぃ","syu":"しゅ","sye":"しぇ","syo":"しょ"}
h2d16={"tya":"ちゃ","tyi":"ちぃ","tyu":"ちゅ","tye":"ちぇ","tyo":"ちょ"}
h2d17={"nya":"にゃ","nyi":"にぃ","nyu":"にゅ","nye":"にぇ","nyo":"にょ"}
h2d18={"hya":"ひゃ","hyi":"ひぃ","hyu":"ひゅ","hye":"ひぇ","hyo":"ひょ"}
h2d19={"mya":"みゃ","myi":"みぃ","myu":"みゅ","mye":"みぇ","myo":"みょ"}
h2d20={"rya":"りゃ","ryi":"りぃ","ryu":"りゅ","rye":"りぇ","ryo":"りょ"}
h2d21={"gya":"ぎゃ","gyi":"ぎぃ","gyu":"ぎゅ","gye":"ぎぇ","gyo":"ぎょ"}
h2d22={"zya":"じゃ","zyi":"じぃ","zyu":"じゅ","zye":"じぇ","zyo":"じょ"}
h2d23={"dya":"ぢゃ","dyi":"ぢぃ","dyu":"ぢゅ","dye":"ぢぇ","dyo":"ぢょ"}
h2d24={"bya":"びゃ","byi":"びぃ","byu":"びゅ","bye":"びぇ","byo":"びょ"}
h2d25={"pya":"ぴゃ","pyi":"ぴぃ","pyu":"ぴゅ","pye":"ぴぇ","pyo":"ぴょ"}

h2d26={"ja":"じゃ","ji":"じ","ju":"じゅ","je":"じぇ","jo":"じょ"}
h2d27={"fa":"ふぁ","fi":"ふぃ","fu":"ふ","fe":"ふぇ","fo":"ふぉ"}
h2d28={"va":"ヴぁ","vi":"ヴぃ","vu":"ヴ","ve":"ヴぇ","vo":"ヴぉ"}

hiragana_dict2.update(**h2d2, **h2d3, **h2d4, **h2d5, **h2d6, **h2d7, **h2d8, **h2d9, **h2d10)
hiragana_dict2.update(**h2d11, **h2d12, **h2d13, **h2d14, **h2d15, **h2d16, **h2d17, **h2d18, **h2d19, **h2d20)
hiragana_dict2.update(**h2d21, **h2d22, **h2d23, **h2d24, **h2d25, **h2d26, **h2d27, **h2d28)

# 一部行
hiragana_dict3={"na":"な","ni":"に","nu":"ぬ","ne":"ね","no":"の"}
h3d2={"ya":"や","yi":"い","yu":"ゆ","ye":"いぇ","yo":"よ"}

hiragana_dict3.update(**h3d2)

# 母音字等
hiragana_dict4={"a":"あ","i":"い","u":"う","e":"え","o":"お","n":"ん"}

hiragana_list = []

# メッセージを受けた時の動作
@client.event
async def on_message(message):

    if message.author.bot:
        return

    # 英数字のみ(一部記号ok)かの判定
    if message.content.replace(",", "").replace(".", "").replace("'", "").replace("?", "").replace("!", "").replace("\n", "").replace(" ", "").encode("utf-8").isalnum():
        # 数字のみかの判定
        if message.content.isnumeric():
            return

        global content
        global author
        content = message.content
        author = str(message.author.display_name)
        if not "0" in hiragana_list:
            hiragana_list.append("0")

    if message.content == "--":

        await message.delete()

        if not "0" in hiragana_list:
            return
        new_content = content
        new_content_author = author
            
        new_content = new_content.lstrip()

        for k1 in hiragana_dict1:
            if k1 in new_content:
                v1 = hiragana_dict1[k1]
                new_content = new_content.replace(k1, v1)

        for k2 in hiragana_dict2:
            if k2 in new_content:
                v2 = hiragana_dict2[k2]
                new_content = new_content.replace(k2, v2)

        for k3 in hiragana_dict3:
            if k3 in new_content:
                v3 = hiragana_dict3[k3]
                new_content = new_content.replace(k3, v3)

        for k4 in hiragana_dict4:
            if k4 in new_content:
                v4 = hiragana_dict4[k4]
                new_content = new_content.replace(k4, v4)

        new_content = new_content.replace("'", "")

        await message.channel.send(f"```py\n@{new_content_author} さんのメッセージ\n'{new_content}'\n```")

if __name__ == "__main__":
    client.run(TOKEN)