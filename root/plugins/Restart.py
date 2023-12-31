from root import REPO
from root.__main__ import bot
from pyrogram import *
from root import OWN
from root.plugins.code import RUN

@bot.on_message(filters.command("restart") & filters.user(OWN))
def RESTART(_, message):
    bot.send_message(message.chat.id, "Restarting Your Bot..")
    RUN(f"cd {REPO} && python3 -m root")
    exit()
