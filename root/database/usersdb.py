from root import DATABASE as mongodb


db = mongodb.USERS


def get_users():
    users = []
    for x in db.find():
        users.append(x["user_id"])
    return users

def add_user(user_id: int):
    if user_id in get_users():
         return
    db.insert_one({"user_id": user_id})

def remove_user(user_id: int):
    if not user_id in get_users():
        return
    x = db.find_one({"user_id": user_id})
    db.delete_one(x)
