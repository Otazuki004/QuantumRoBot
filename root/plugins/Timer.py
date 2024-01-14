import asyncio
from root.__main__ import bot
from pyrogram import *

@bot.on_message(filters.command("timer"))
async def timer(_, message):
    try:
        if len(message.text.split()) <2:
            return await message.reply_text("Please Enter minutes ⚡")
        mins = int(message.text.split()[1])
    except (IndexError, ValueError):
        await message.reply("**SyntaxError**, Use /timer (minutes) ✅")
        return
    if mins <= 0:
        await message.reply("Timer duration should be a positive integer.")
        return
    if mins > 300:
        await message.reply("Maximum Timer Limit Is 300 minutes Please Enter Below 300")
        return
    await message.reply(f"Setting timer for {mins} Minutes ⚡")
    await asyncio.sleep(60 * mins)
    await message.reply("Your Timer has been completed ✅")
