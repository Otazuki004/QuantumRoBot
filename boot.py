from pyrogram import Client, filters
from vars import bot
from vars import *
import subprocess

print("booting os")

op = "yes"

if op == "yes":
  bot.send_message(OWN, "Lets boot the os")
  command = "python3 -m bot"
  result = subprocess.run(command, shell=True, capture_output=True, text=True)

  print("Output:", result.stdout)
  print("Error:", result.stderr)
  print("Return code:", result.returncode)
else:
  exit()



