import random
from root import bot
from root import prefix 
from root.plugins.main import ask_to_dm_first
from root.database.main import get_users_list
from root.database.coins import add_coins_to_db, get_coins_from_users
from root.database.count_won_lose import add_won_count, add_lose_count, get_bet_count
from root.database.level import add_level_to_db, get_users_level, level_system
from pyrogram import filters


won_users = []

async def winners_coins(user_id: int, coins_spend: int):
      count = won_users.count(user_id)
      coins = coins_spend*int(count)+2
      return coins

@bot.on_message(filters.command("bet", prefix))
async def bet(_, message): 
    user_id = message.from_user.id
    if user_id not in (await get_users_list()):
          return await ask_to_dm_first(message)
    bet_count = await get_bet_count(user_id)
    kk = await level_system(bet_count)
    mm = await get_users_level(user_id)
    if mm != kk:
         await add_level_to_db(user_id, level=kk)
         await message.reply_text(f"⬆️ You Have Reached Level {kk}.")
    try:
          coins_spend = int(message.text.split(None,1)[1])
    except:
          return await message.reply_text("🆘 Example: /bet 100", quote=True)
    if message.text.split(None,1)[1][0] == "-":
        return await message.reply_text("No!", quote=True)
    coins_balance = await get_coins_from_users(user_id)
    if coins_balance > coins_spend or coins_balance == coins_spend:
        mm = ["lose","won","lose","pro","lose"]
        key = random.choice(mm)
        if key.casefold() == "lose":
              await add_lose_count(user_id=user_id, lose_count=+1)
              await add_coins_to_db(user_id, -coins_spend)
              coins = await get_coins_from_users(user_id)
              await message.reply_text(f"🚫 You Lose {coins_spend}. Your Current coins Balance `{coins}`.")
              x = [m for m in won_users if m!= user_id]
              won_users.clear()
              cc = won_users + x
              return 
        elif key.casefold() == "pro":
               won_coins = coins_spend*10
               await add_coins_to_db(user_id=user_id, coins=won_coins)
               coins = await get_coins_from_users(user_id)
               return await message.reply_text(f"🎊 Pro Bet UwU 🎊. 🎊 You Won {won_coins}, ✨ Your Current coins Balance `{coins}`.", quote=True)
        elif key.casefold() == "won":
              await add_won_count(user_id=user_id, won_count=+1)
              won_users.append(user_id)
              won_coins = await winners_coins(user_id=user_id, coins_spend=coins_spend)
              await add_coins_to_db(user_id=user_id, coins=won_coins)
              coins = await get_coins_from_users(user_id)
              count = won_users.count(user_id)
              return await message.reply_text(f"🎊 You Won [`{count}`x]: {won_coins}, ✨ Your Current Balance coins {coins}.", quote=True)
    else:
        return await message.reply_text("You Don't Have This Much coins, Check Current coins Balance by Tap /profile.")
