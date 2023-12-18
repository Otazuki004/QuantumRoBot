from pyrogram import *
from root.bot import *
from root import *

#UBModuleStart
@UB.on_message(filters.regex(".alive"))
def Alive_UB (UB, message):
    UB.send_message(message.chat.id, "I'm Alive")
#UBEND
UB.run()
