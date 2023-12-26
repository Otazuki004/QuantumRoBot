from pyrogram import filters
from root import *
from root.__main__ import *

HANDLER = ["~", ".", "!", "/"]

@Client.on_message(filters.command("id", prefixes=HANDLER))
async def id(_, m):
    reply = m.reply_to_message
    _reply = ""
    if not reply:
        no_reply = f"Your Id: {m.from_user.id}\n"
        no_reply += f"Chat ID: {m.chat.id}\n"
        no_reply += f"Message Id: {m.id}"
        await m.reply_text(text=(no_reply))
    if reply.from_user:
        _reply += f"Your Id: {m.from_user.id}\n"
        _reply += f"Replied User Id: {reply.from_user.id}\n"
        _reply += f"Chat ID: {m.chat.id}\n\n"
        _reply += f"Replied Message Id: {reply.id}\n"
    if reply.sender_chat:
        _reply += f"Channel Id: {reply.sender_chat.id}\n"
    if reply.sticker:
        _reply += f"Sticker Id: {reply.sticker.file_id}"
    elif reply.animation:
        _reply += f"Animation Id: {reply.animation.file_id}"
    elif reply.document:
        _reply += f"Document Id: {reply.document.file_id}"
    elif reply.audio:
        _reply += f"Audio Id: {reply.audio.file_id}"
    elif reply.video:
        _reply += f"Video Id: {reply.video.file_id}"
    elif reply.photo:
        _reply += f"Photo Id: {reply.photo.file_id}"
    await reply.reply_text(_reply)
    await m.delete()
