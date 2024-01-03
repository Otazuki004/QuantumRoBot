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
Ht = "tst"

Code = [TgBotmk0001Hs, Ht]

@bot.on_message(filters.command("refrence"))
async def refrence(_, message):
    query = " ".join(message.command[1:])
    try:
        if query == Code:
            await bot.send_message(message.chat.id, Code)
        else:
            await bot.send_message(message.chat.id, "Invalid Code ❌")
    except Exception as e:
        await bot.send_message(message.chat.id, "Went Wrong")
        print(e)
