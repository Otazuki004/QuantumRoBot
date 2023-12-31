from root import REPO
from root.__main__ import bot
from pyrogram import *
from root import OWN
from root.plugins.code import SRUN
import subprocess

@bot.on_message(filters.command("restart") & filters.user(OWN))
def RESTART(_, message):
    bot.send_message(message.chat.id, "Restarting Your Bot..")
    CO = f"rm -rf {REPO} && cd {REPO} && python3 -m root"
    result = subprocess.run(CO, shell=True, capture_output=True, text=True)
    print("Output:", result.stdout)
    print("Error:", result.stderr)
    exit()
