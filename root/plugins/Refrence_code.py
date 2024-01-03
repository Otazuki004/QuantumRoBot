from root.__main__ import bot
from pyrogram import *
from root import *

TgBotmk0001Hs = """
*"Valid Code ✅**

Bot Status = Process Started ✅
Estimated Time = 5 To 7 Days

What Happening Now?
- Currently Its OUR first Url Downloader Project
- Repository Created ✅
- Creating Codes With Gpt-3.5

**Powered by: @Hyper_Speed0**
"""

@bot.on_message(filters.command("refrence"))
def refrence(_, message):
    query = " ".join(message.command[1:])
    try:
        await bot.send_message(message.chat.id, query)
    except Exception as e:
        await bot.send_message(message.chat.id, "Went Wrong")
        print(e)
