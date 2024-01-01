import asyncio
from root.__main__ import bot
from pyrogram import *

@bot.on_message(filters.command("timer"))
async def timer(_, message):
    try:
        mins = int(message.text.split()[1])
    except (IndexError, ValueError):
        await message.reply("Invalid usage ❌. Use /timer (minutes)")
        return
    if mins <= 0:
        await message.reply("Timer duration should be a positive integer.")
        return
    await message.reply(f"Setting timer for {mins} Minutes ⚡")
    await asyncio.sleep(60 * mins)
    await message.reply("Your Timer has completed ✅")
