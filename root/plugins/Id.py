from pyrogram import filters
from root import *
from root.__main__ import *

HANDLER = ["~", ".", "!", "/"]

@Client.on_message(filters.command("id", prefixes=HANDLER))
async def id(_, m):
    reply = m.reply_to_message
    _reply = ""
    if not reply:
        no_reply = f"Yᴏᴜʀ ɪᴅ: {m.from_user.id}\n"
        no_reply += f"Tʜɪs ᴄʜᴀᴛ ɪᴅ: {m.chat.id}\n"
        no_reply += f"Mᴇssᴀɢᴇ ɪᴅ: {m.id}"
        await m.reply_text(text=(no_reply))
    if reply.from_user:
        _reply += f"Yᴏᴜʀ ɪᴅ: {m.from_user.id}\n"
        _reply += f"Rᴇᴘʟɪᴇᴅ Usᴇʀ ɪᴅ: {reply.from_user.id}\n"
        _reply += f"Tʜɪs Cʜᴀᴛ ɪᴅ: {m.chat.id}\n\n"
        _reply += f"ʀᴇᴘʟɪᴇᴅ ᴍᴇssᴀɢᴇ ɪᴅ: {reply.id}\n"
    if reply.sender_chat:
        _reply += f"Cʜᴀɴɴᴇʟ  ɪᴅ: {reply.sender_chat.id}\n"
    if reply.sticker:
        _reply += f"Sᴛɪᴄᴋᴇʀ ɪᴅ: {reply.sticker.file_id}"
    elif reply.animation:
        _reply += f"Aɴɪᴍᴀᴛɪᴏɴ ɪᴅ: {reply.animation.file_id}"
    elif reply.document:
        _reply += f"Dᴏᴄᴜᴍᴇɴᴛ ɪᴅ: {reply.document.file_id}"
    elif reply.audio:
        _reply += f"Aᴜᴅɪᴏ ɪᴅ: {reply.audio.file_id}"
    elif reply.video:
        _reply += f"Vɪᴅᴇᴏ ɪᴅ: {reply.video.file_id}"
    elif reply.photo:
        _reply += f"Pʜᴏᴛᴏ ɪᴅ: {reply.photo.file_id}"    
    await reply.reply_text(_reply)
    await m.delete()
