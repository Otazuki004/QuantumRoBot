from pyrogram import *
from vars import *

print("booting os")

op = "yes"

if op == "yes":
  bot.send_message(OWN, "Lets boot the os")
else:
  exit()

bot.run()
