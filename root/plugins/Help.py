from pyrogram import filters
import random 
from root import *
from root.__main__ import *
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup

help = f"""**
🖤 Click Button below To Know My Commands 🖤
**
"""

@bot.on_message(filters.command("help"))
def start(bot, message):
 bot.send_message(message.chat.id, help, reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("Continue ✅", callback_data="help")]]
        ),
                    )
  
