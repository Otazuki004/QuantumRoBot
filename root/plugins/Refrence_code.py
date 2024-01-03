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

Bot Status = Created ✅

Information ✅
- Your Bot Has Been Successfully Created And its Running
- If Any Problems Ask To @Otazuki Else @FutureCity005

Warranty ⚡

- Your Bot Have 1 Month Warranty
- Check About Warrenty [Here](https://t.me/Hyper_Speed0/40).
- Follow That All Rules
- Your Warranty Time Started On [4 January 2024]


Thanks For Using Us

This Code Will Deleted in January 4 12:00PM (INR)
Powered by: @Hyper_Speed0**
"""

@bot.on_message(filters.command("code"))
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
