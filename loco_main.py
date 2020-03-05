import requests
import json
import asyncio
from dhooks import Webhook, Embed
from datetime import datetime
from pytz import timezone
import pytz
import time
indianist = timezone('Asia/Kolkata')
global oldata
oldata = None


# input all datas
loco_bearer_token = "oAQ0BjrWzVQqJ5kM7PNQQnvq9coOq1"
webhook_url = "https://discordapp.com/api/webhooks/663377658180141086/Lbdqh_E2Tm0dSs7Lp_gstIznxCEPQahDiqqp-GW5iR-5PSjnkCc34zhZcjTnVp4d1OGT"

#############################

try:
    hook = Webhook(webhook_url)
except:
    print("Wrong WebHook Url!")
def getuser():
    req = requests.get("https://jsonblob.com/api/jsonBlob/5a7661d6-7fd5-11e9-8d0e-6fe578ed4135")
    try:
        data = req.json()
    except:
        data = {
        }
    return data

def fetch_data(oldata):
    print("Auto loco bot connected")
    print("Welcome here! This is an alternative socket of Loco Trivia made by Shivam in Python!")
    while True:
        data = getuser()
        if data != oldata:
           # print(data)
            if data["type"] == "starting":
                print('Game is Starting within 5m!')
                embed = Embed(title="**__READY TO WIN LOCO TRIVIA__**", description="**`GAME STARTS WITHIN 5 MINUTES`**", color=0x58B3F7)
                embed.add_field(name="<a:emoji_22:668119034864336937>**__BOT STATUS__**<a:emoji_22:668119034864336937>", value="**Online**  :red_circle:  **`Auto Run Bot`**")
                embed.add_field(name="**__FAST GUYS & ALSO REACT HERE__**", value="```✴️✴️✴️    💸💸💸💸    ✴️✴️✴️```")
                embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/661100024452743178/668120613101240350/IMG_20200109_213228.jpg")
                embed.set_image(url="https://cdn.discordapp.com/attachments/612849803352604673/666201723341373462/barrr.gif")
                embed.set_footer(text=f"Trivia Nation | Shivam々0001",\
                icon_url="https://cdn.discordapp.com/attachments/661100024452743178/682486812404350976/JPEG_20200222_184202.jpg")
                hook.send("@everyone",embed=embed)
            elif data["type"] == "Question":
                question = data["q"]
                question_no = data["qnum"]
                options = [data["o1"],data["o2"],data["o3"]]
                embed = Embed(title=f"Q{str(question_no)} out of 10", description=question,color=0x58B3F7)
                embed.add_field(name="**__OPTIONS__**", value=f"1. {options[0]}\n2. {options[1]}\n3. {options[2]}")
                embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/661100024452743178/682474021912182795/images_22.jpeg")
                embed.set_footer(text=f"Trivia Nation | Shivam々0001™〢",\
                icon_url="https://cdn.discordapp.com/attachments/661100024452743178/682486812404350976/JPEG_20200222_184202.jpg")
                hook.send(embed=embed) 
                hook.send("-+lo")
            elif data["type"] == "QuestionSummary":
                correct = data["correct"]
                embed = Embed(title="**LOCO TRIVIA**", description="Question Summary",color=0x58B3F7)
                embed.add_field(name="<a:ntsahi:658256244594704397> **__Correct Answer__**", value=correct)
                embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/661100024452743178/682474021912182795/images_22.jpeg")
                embed.set_footer(text=f"Trivia Nation | Shivam々0001™〢",\
                icon_url="https://cdn.discordapp.com/attachments/661100024452743178/682486812404350976/JPEG_20200222_184202.jpg")
                hook.send(embed=embed)
                
            elif data["type"] == "GameSummary":
                number_of_winners = data["winners"]
                payout = data["payout"]
                embed = Embed(title="**__TRIVIA NATION | PRO™__**", description=f"Game Summary ",color=0xFA58AC)
                embed.add_field(name="**__Crowd Accuracy__**", value="**10/10**")              
                embed.add_field(name="**__Total Winners__**", value=number_of_winners)               
                embed.add_field(name="**__Game Payout__** <:paytm:681408218299105280> ", value="**₹**"+str(payout)) 
                embed.add_field(name="**__Post Winning Screenshot Here__**", value="<#657832721481072657>")
                embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/661100024452743178/682474021912182795/images_22.jpeg")
                embed.set_image(url="https://cdn.discordapp.com/attachments/612849803352604673/666201723341373462/barrr.gif")
                embed.set_footer(text=f"Trivia Nation | SHIVAM々0001™",\
                icon_url="https://cdn.discordapp.com/attachments/661100024452743178/682486812404350976/JPEG_20200222_184202.jpg")

                hook.send(embed=embed)                
                break
            elif data["type"] == "waiting":
                title = data["game"]
                hook.send(f"Next game {title}")
        oldata = data
while True:
    response_data = requests.get("http://api.getloconow.com/v1/contests/",headers={'Authorization': f"Bearer {loco_bearer_token}"}).json()
    if "invalid_grant" in response_data:
        print("Bearer token is not Valid!!")
        break
    re_time = indianist.localize(datetime.fromtimestamp(int(response_data['start_time']/1000))).replace(tzinfo=None)-datetime.now().replace(tzinfo=None)    
    sec = re_time.seconds
    if sec <= 600:
        print("Game is Live")
        fetch_data(oldata)
    print("Game not live sleeping for 5 min!")
  
    time.sleep(300)    
