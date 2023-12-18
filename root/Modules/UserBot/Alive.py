from pyrogram import *
from root.__main__ import *
from root import *

#UBModuleStart
@UB.on_message(filters.command("alive") & filters.prefix(PRE))
def Alive_UB (UB, message):
    UB.send_message(message.chat.id, "I'm Alive")
#UBEND
