from root.__main__ import bot
from pyrogram import *
import random


Dare = ['Take a screenshot and send it', 'Send Your Browser History Screenshot', 'Tell your Favourite Song Name', 'Send Your Phone Number']

@Client.on_message(filters.command("dare"))
def dare(_, message):
    DareR = random.choice(Dare)
    message.reply_text(DareR)
