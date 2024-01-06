from root.__main__ import bot 
from pyrogram import *


@bot.on_message(filters.command("repo"))
async def repo(_, message):
    await message.reply_text("""**
Dear Valued User,

We extend our heartfelt gratitude for choosing our services. Your support means the world to us.

Behold, the repository link you've been eagerly waiting for:

Repository Link: __https://github.com/Otazuki004/QuantumRoBot.git__

Should you desire further assistance or wish to be part of our vibrant community, don't hesitate to join our esteemed [FutureCity Support Group.](https://t.me/FutureCity005)

Embark on a journey of technological marvels at Hyper-Speed with us. Explore, engage, and revel in the possibilities that await you.

- Hyper Speed**
""")
