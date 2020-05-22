#-*- coding: utf-8 -*-

try: 
    from googlesearch import search 
except ImportError:  
    print("No module named 'google' found") 

# Cantonese tokens for query 
query = "啲哋嘢咩靚呢嗰唔佢你我係嘅咗咁架冇同咩哋幾啦畀俾啩啫嗱喇掂啫話睇喺咪喎仲揾哂囉啦呀諗吖埋咋蚊晝瞓嘥佬拎舊攰啱噚叻吓冧呃"
 
# https://core.ac.uk/download/pdf/48548269.pdf
# YEUNG, Yu Ting 
# Language Modeling for Speech Recognition of Spoken Cantonese 
# 啲 哋 嘢 咩 靚 呢 嗰 唔 佢 你 我 係 嘅 咗 咁 
# 架 冇 同 咩 哋 幾 啦 畀 俾 啩 啫 嗱 喇 掂 啫 
# 話 睇 喺 咪 喎 仲 揾 哂 囉 啦 呀 諗 吖 埋 咋
# 蚊 晝 瞓 嘥 佬 拎 舊 攰 啱 噚 叻 吓 冧 呃
# 的 們 那 這 哪 在 不 是 了 些 他 她

webs = []

for keyword in query:
    print(f"Searching {keyword}")
    for web in search(keyword, tld='com', num=1, start=0, stop=None, pause=5): 
        webs.append(web)
        with open("websites.txt", "a") as f:
            print(webs, file=f) 
            webs = []
