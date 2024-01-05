import io
from pyrogram import *
from root.__main__ import bot
import traceback
from subprocess import getoutput as run
from pyrogram.enums import ChatAction

@bot.on_message(filters.command("logs"))
async def logs(_, message):
    run_logs = run("cat log.txt")
    text = message.reply_text("Trying to Sending logs...")
    await bot.send_chat_action(message.chat.id, ChatAction.UPLOAD_DOCUMENT)
    with io.BytesIO(str.encode(run_logs)) as logs:
        logs.name = "log.txt"
        await message.reply_document(
            document=logs,
        )
    await text.delete()
