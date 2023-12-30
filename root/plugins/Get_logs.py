from pyrogram import *
from root.__main__ import bot
import traceback
from subprocess import getoutput as run

@bot.on_message(filters.command("logs"))
async def logs(_, m):
    run_logs = run("tail log.txt")
    msg = m.reply_text("Trying to Sending logs...")
    with io.BytesIO(str.encode(run_logs)) as logs:
        logs.name = "log.txt"
        await m.reply_document(
            document=logs,
        )
    await msg.delete()
