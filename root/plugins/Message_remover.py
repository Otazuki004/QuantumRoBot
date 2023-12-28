from pyrogram import *
from root.__main__ import *
from root import *

@bot.on_message(filters.regex("punda"))
async def remove_message(client, message):
    try:
        await message.delete()
    except Exception as e:
        print(e)
        await bot.send_message("Error", e)
