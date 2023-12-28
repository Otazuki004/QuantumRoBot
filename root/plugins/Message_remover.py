import re
from pyrogram import filters
from root.__main__ import bot

# List of words to filter
bad_words = [
    "fuck", "Kena", "Mairu", "Sex", "Girlfriendsex", "Mf", "Tf", "Wtf", "Ass", 
    "Boobs", "Kunji", "Punda", "Otha", "Umbu", "Coolip", "Drugs", "Saaraku", 
    "Ponnupunda", "Motherfucker", "Fucker", "Fuckers", "Pundaboys", "Sunni", 
    "MadanGowri", "AdamGaming", "Ff", "Mr"
]

# Build a regex pattern with variations
pattern = r"\b(?:{})\b".format('|'.join(map(re.escape, bad_words)))

@bot.on_message(filters.text & filters.regex(pattern, re.IGNORECASE))
async def remove_message(_, message):
    try:
        await message.delete()
    except Exception as e:
        print(e)
        await bot.send_message(message.chat.id, f"Error: {e}")
