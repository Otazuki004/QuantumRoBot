import uuid
from root import DATABASE

db = DATABASE["REDEEM"]



async def add_redeem_to_db(coins: int): 
    code = str(uuid.uuid4().hex)
    string = {"code": code, "coins": coins}
    db.insert_one(string)
    return code

async def remove_redeem_to_db(code: str):
      string = {"code": code}
      find = db.find_one(string)
      if find:
          db.delete_one(find)
          return True 
      else: 
         return False


async def get_redeem_code():
      code = [x for x in db.find()]
      return code
    


async def get_redeem_coins(code, user_id: int):
     if db.find_one({"code": code}):
          xx = db.find_one({"code": code})
          try:
             xx["user_ids"]
          except:
               filter = {"code": code}
               update = {"$set": {"user_ids": [100]}}
               db.update_one(filter, update)
          vv = db.find_one({"code": code})
          USER_IDS = vv["user_ids"]
          if user_id not in USER_IDS:
               USER_IDS.append(user_id)
               filter = {"code": code}
               update = {"$set": {"user_ids": USER_IDS}}
               db.update_one(filter, update)
               coins = db.find_one({"code": code})
               return coins["coins"]
          else: return False
