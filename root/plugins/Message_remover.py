from pyrogram import filters
from root.__main__ import bot

@bot.on_message(filters.text & filters.regex(r"\bpunda\b", re.IGNORECASE))
async def remove_message(_, message):
    try:
        await message.delete()
    except Exception as e:
        print(e)
        await bot.send_message(message.chat.id, f"Error: {e}")
