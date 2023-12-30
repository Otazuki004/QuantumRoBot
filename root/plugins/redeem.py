from root import bot
from root import prefix
from root import ODEV as DEV_ID
from root.database.redeem import add_redeem_to_db, remove_redeem_to_db, get_redeem_code
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

@bot.on_message(filters.command("generate", prefix) & filters.user(DEV_ID))
async def generate_redeem(_, message):
      username = (await bot.get_me()).username
      try:
          coins = int(message.text.split(None,1)[1])
      except:
          return await message.reply_text("Example: /generate 1000.\n `This case you are creating a redeem token which has 1000 coins`")
      code = await add_redeem_to_db(coins)
      return await message.reply_text(f"🎊 New Redeem Token Arrived! 🎊\n💰 coins: `{coins}`",
           reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(text=f"💰 {coins} ⬅️", url=f"t.me/{username}/?start={code}")]]),quote=True)

@bot.on_message(filters.command("clear", prefix) & filters.user(DEV_ID))
async def clear_redeem(_, message):
       try:
          code = message.text.split(None,1)[1]
       except:
          return await message.reply_text("Example: /clear code.\n`Thid case your are deleting that redeem code.`")
       kk = await remove_redeem_to_db(code)
       if kk:
           return await message.reply_text("Successfully redeem token Removed! 🧑‍🏫", quote=True)
       else:
           return await message.reply_text(f"🚫 No Redeem Tokens Has: `{code}`", quote=True)


@bot.on_message(filters.command("redeems", prefix) & filters.user(DEV_ID))
async def get_redeems(_, message):
       code = await get_redeem_code()
       string = ""
       for user in code:
            string += "💰 {coins}: `{token}`\n".format(coins=user["coins"], token=user["code"])
       string += "\nCurrentl Available Tokens ✅"
       return await message.reply_text(string)
