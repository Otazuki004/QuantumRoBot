from root import *
from root.__main__ import bot
from pyrogram import *
from datetime import *

@bot.on_message(filters.command("timer15"))
def Time15 (_, message):
    bot.send_message(message.chat.id, "Timer Set ✅")
    time.sleep(9)
    message.reply_text("Your Timer Completed ✅")
