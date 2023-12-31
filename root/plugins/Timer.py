from root import *
from root.__main__ import bot
from pyrogram import *
from datetime import *

@bot.on_message(filters.command("timer15"))
async def Time15 (_, message):
    await bot.send_message(message.chat.id, "Timer Set ✅")
    await time.sleep(900)
    await bot.send_message(message.chat.id, "Your Timer Completed ✅")
