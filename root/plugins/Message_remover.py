from pyrogram import *
from root.__main__ import *
from root import *

@bot.on_message(filters.regex("punda"))
async def remove_message(client, message):
    await message.delete()
