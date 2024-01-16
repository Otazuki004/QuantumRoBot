from pyrogram import *
from root import OWN, FRD_MSG
from root.__main__ import bot

if FRD_MSG == True:
    @bot.on_message(filters.private)
    async def forward(_, message):
        CID = message.chat.id
        MID = message.id
        if CID == OWN:
            return
        try:
            frd = await bot.forward_messages(OWN, CID, MID)
            await frd.reply_text(f"**sender username**: @{message.from_user.username}")
        except Exception:
            print(f"[WARNING] message Forwarding ❌ FAILED ❌") 
