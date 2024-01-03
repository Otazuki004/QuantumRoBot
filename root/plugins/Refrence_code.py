from root.__main__ import bot
from pyrogram import *

TgBotmk0001Hs = """
**Valid Code ✅

Bot Status = Process Started ✅
Estimated Time = 10th January⚡

What Happening Now?
- Currently Its OUR first Url Downloader Project
- Repository Created ✅
- Creating Codes With Gpt-3.5
- Working Hard

Powered by: @Hyper_Speed0**
"""
TgBotmk0002Hsv2 = """
**Valid Code ✅

Bot Status = 40% Done
Estimated time - Jan 3, 10:00PM

What Happening Now?
- Currently Old Codes Not Worked So
- We Created New Code For You
- Chat gpt Helping Us
- Working Hard

Powered by: @Hyper_Speed0**
"""

@bot.on_message(filters.command("refrence"))
async def refrence(_, message):
    query = " ".join(message.command[1:])
    try:
        if query == "TgBotmk0001Hs":
            await bot.send_message(message.chat.id, TgBotmk0001Hs)
        elif query == "TgBotmk0002Hsv2":
            await bot.send_message(message.chat.id, TgBotmk0002Hsv2)
        else:
            await bot.send_message(message.chat.id, "Invalid Code ❌")
    except Exception as e:
        await bot.send_message(message.chat.id, "Went Wrong")
        print(e)
