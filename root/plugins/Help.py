from pyrogram import filters
import random 
from root import *
from root.__main__ import *
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup

help = f"""**
🖤 Click Button below To Know My Commands 🖤
**
"""

@Client.on_message(filters.command("help"))
def start(bot, message):
 Client.send_message(message.chat.id, help, reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("Continue ✅", callback_data="help")]]
        ),
                    )
  
