from root import *
from root.__main__ import bot
from pyrogram import *
from datetime import datetime
import time

ff = 900

@bot.on_message(filters.command("timer15"))
async def Time15 (_, message):
    await bot.send_message(message.chat.id, "Timer Set ✅")
    time.sleep(ff)
    await message.reply_text("Your Timer Completed ✅")

@bot.on_message(filters.command("timer30"))
async def Time30 (_, message):
    await bot.send_message(message.chat.id, "Timer Set ✅")
    time.sleep(ff*2)
    await message.reply_text("Your Timer Completed ✅")

@bot.on_message(filters.command("timer45"))
async def Time45 (_, message):
    await bot.send_message(message.chat.id, "Timer Set ✅")
    time.sleep(ff*3)
    await message.reply_text("Your Timer Completed ✅")

@bot.on_message(filters.command("timer60"))
async def Time60 (_, message):
    await bot.send_message(message.chat.id, "Timer Set ✅")
    time.sleep(ff*4)
    await message.reply_text("Your Timer Completed ✅")
    
