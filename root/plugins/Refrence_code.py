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
- I am Suffering With Fever So I can't Make 2 days

Powered by: @Hyper_Speed0**
"""

@bot.on_message(filters.command("code"))
async def refrence(_, message):
    query = " ".join(message.command[1:])
    try:
        if query == "TgBotmk0001Hs":
            await message.reply_text(f"{TgBotmk0001Hs}")
        else:
            await message.reply_text("Invalid Code ❌")
    except Exception as e:
        await bot.send_message(message.chat.id, f"Somthing Went Wrong: {e}")
        print(e)
