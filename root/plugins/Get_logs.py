import io
from pyrogram import *
from root.__main__ import bot
import traceback
from subprocess import getoutput as run
from pyrogram.enums import ChatAction

@bot.on_message(filters.command("logs"))
async def logs(_, message):
    run_logs = run("tail log.txt")
    text = await message.reply_text("`Getting logs...`")
    await bot.send_chat_action(message.chat.id, ChatAction.TYPING)
    await message.reply_text(f"```shell\n{run_logs}```")
    await text.delete()




@bot.on_message(filters.command("flogs"))
async def logs(_, message):
    run_logs = run("cat log.txt")
    text = await message.reply_text("Sending Full logs...")
    await bot.send_chat_action(message.chat.id, ChatAction.UPLOAD_DOCUMENT)
    with io.BytesIO(str.encode(run_logs)) as logs:
        logs.name = "log.txt"
        await message.reply_document(
            document=logs,
        )
    await text.delete()
