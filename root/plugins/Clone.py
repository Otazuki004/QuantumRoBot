from pyrogram import Client, filters, idle
from pyrogram.types import Message
from root import a_id as API_ID
from root import a_hash as API_HASH
from root.__main__ import bot

# Assuming bot is defined somewhere else in your code
@bot.on_message(filters.command("clone"))
async def clone(_, message: Message):
    try:
        token = message.text.split(None, 1)[1]
    except IndexError:
        return await message.reply_text("Enter Your Bot Token Is Required!")

    msg = await message.reply_text("Cloning Your Client Please Wait While! 🕛")
    try:
        bot = Client("Clone", api_id=API_ID, api_hash=API_HASH, bot_token=token, plugins={"root": "root/plugins"})
        await bot.start()
        await idle()
    except Exception as e:
        return await message.reply_text("Error: " + str(e))
    await msg.edit_text("Your Client has been Successfully Clone ✅")
