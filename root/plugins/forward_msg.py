from pyrogram import *
from root import OWN, FRD_MSG
from root.__main__ import bot

if FRD_MSG == True: #You can off this In __init__.py
    @bot.on_message(filters.private & filters.all)
    async def forward(_, message):
        CID = message.chat.id
        MID = message.id
        if CID == OWN:
            return
        try:
            frd = await bot.forward_messages(OWN, CID, MID)
            await frd.reply_text(f"**Sender Username**: @{message.from_user.username}\n**Sender Id**: {message.from_user.id}")
        except Exception as e:
            print(f"[WARNING] Message Forwarding is FAILED ")
            print(e)
