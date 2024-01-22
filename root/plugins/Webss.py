from pyrogram import filters
from root import bot
from root.__main__ import *


@bot.on_message(filters.command("webss"))
async def take_ss(_, message):
    try:
        if len(message.command) != 2:
            return await message.reply_text("» ɢɪᴠᴇ ᴀ ᴜʀʟ ᴛᴏ ғᴇᴛᴄʜ sᴄʀᴇᴇɴsʜᴏᴛ...")
        url = message.text.split(None, 1)[1]
        try:
            if url.startswith("https://"):
                await message.reply_text("» Usᴀɢᴇ /webss ᴡᴡᴡ.(Website Name).(domain)")
            elif url.startswith("www"):
                    m = await message.reply_text("» ᴛʀʏɪɴɢ ᴛᴏ ᴛᴀᴋᴇ sᴄʀᴇᴇɴsʜᴏᴛ...")
                    await m.edit("» ᴜᴩʟᴏᴀᴅɪɴɢ ᴄᴀᴩᴛᴜʀᴇᴅ sᴄʀᴇᴇɴsʜᴏᴛ...")
                    try:
                        await message.reply_photo(
                        photo=f"https://webshot.amanoteam.com/print?q={url}",
                        quote=False)
                        await m.delete()
                    except TypeError:
                        return await m.edit("» ɴᴏ sᴜᴄʜ ᴡᴇʙsɪᴛᴇ.")
                        await m.delete()
                    except Exception as e:
                        if str(e) == """Telegram says: [400 WEBPAGE_CURL_FAILED] - Telegram server could not fetch the provided URL (caused by "messages.SendMedia")""":
                            await m.edit("» ɴᴏ sᴜᴄʜ ᴡᴇʙsɪᴛᴇ.")
                            await m.delete()
                            return
                        await message.reply_text(str(e))
        
            else:
                await message.reply_text("» Usᴀɢᴇ /webss ᴡᴡᴡ.(Website Name).(domain)")
        except Exception as e:
            print(f"Error: {e}")
            await message.reply_text(f"Eʀʀᴏʀ: ", e)
    except Exception as e:
        await message.reply_text(f"Eʀʀᴏʀ: ", e)
