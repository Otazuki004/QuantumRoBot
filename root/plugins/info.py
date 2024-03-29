from pyrogram import filters
from root import prefix as HANDLER
from root import OWN as OWNER_ID
from root.__main__ import bot
from pyrogram import *

@bot.on_message(filters.command("cinfo", prefixes=HANDLER))
async def cinfo(_, m):
    reply = m.reply_to_message
    if not reply:
        await m.reply_text("Bruh! reply to a channel")
        return
    if not reply.sender_chat:
        await m.reply_text("Bruh! reply to a channel")
        return
    if reply.sender_chat:
        message = await m.reply_text("information gathering!!!")
        id = reply.sender_chat.id
        reply.sender_chat.type
        name = reply.sender_chat.title
        username = reply.sender_chat.username
        pfp = reply.sender_chat.photo
    if not pfp:
        text = f"✪ TYPE: Channel\n\n"
        text += f"✪ ID: {id}\n\n"
        text += f"✪ NAME: {name}\n\n"
        text += f"✪ USERNAME: @{username}\n\n"
        text += f"✪ MENTION: [link](t.me/{username})"
        await m.reply_text(text)
        await message.delete()
        return
    image = reply.sender_chat.photo
    if image:
        photo = await bot.download_media(image.big_file_id)
        text = f"✪ TYPE: Channel\n\n"
        text += f"✪ ID: {id}\n\n"
        text += f"✪ NAME: {name}\n\n"
        text += f"✪ USERNAME: @{username}\n\n"
        text += f"✪ MENTION: [link](t.me/{username})"
        await m.reply_photo(photo=photo, caption=(text))
        await message.delete()


no_reply_user = """ ╒═══「 Appraisal results:」

ɪᴅ: `{}`
ᴅᴄ: `{}`
ɴᴀᴍᴇ: {}
ᴜsᴇʀɴᴀᴍᴇ: @{}
ᴘᴇʀᴍᴀʟɪɴᴋ: {}
ᴜsᴇʀʙɪᴏ: `{}`

**Meet Me Here🙈 @FutureCity005 ✨🥀**
"""


@bot.on_message(filters.command("info", prefixes=HANDLER))
async def info(_, m):
    m.reply_to_message
    if len(m.command) < 2:
        await m.reply_text("ɢɪᴠᴇ ᴍᴇ ɪᴅ!")
        return
    id_user = m.text.split(" ")[1]
    msg = await m.reply_text("ɪɴғᴏʀᴍᴀᴛɪᴏɴ ɢᴀᴛʜᴇʀɪɴɢ!")
    info = await bot.get_chat(id_user)
    if info.photo:
        file_id = info.photo.big_file_id
        photo = await bot.download_media(file_id)
        user_id = info.id
        first_name = info.first_name
        username = info.username
        user_bio = info.bio
        dc_id = info.dc_id
        user_link = f"[link](tg://user?id={user_id})"
        await m.reply_photo(
            photo=photo,
            caption=no_reply_user.format(
                user_id, dc_id, first_name, username, user_link, user_bio
            ),
        )
    elif not info.photo:
        user_id = info.id
        first_name = info.first_name
        username = info.username
        user_bio = info.bio
        dc_id = info.dc_id
        user_link = f"[link](tg://user?id={user_id})"
        await m.reply_text(
            text=no_reply_user.format(
                user_id, dc_id, first_name, username, user_link, user_bio
            )
        )
    await msg.delete()
