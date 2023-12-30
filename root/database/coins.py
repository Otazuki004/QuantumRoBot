from root import DATABASE


db = DATABASE["MAIN"]


async def get_coins_from_users(user_id: int):
     string = {"user_id": user_id}
     xx = db.find_one(string)
     mm = int(xx["coins"])
     return mm

async def add_coins_to_db(user_id: int, coins: int):
        xx = await get_coins_from_users(user_id)
        total_coins = xx+coins
        filter = {"user_id": user_id}
        update = {"$set": {"coins": total_coins}}
        db.update_one(filter, update)
