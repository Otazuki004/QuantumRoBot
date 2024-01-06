from pyrogram import *
from root.__main__ import *
from root import OWN, ROOTREPO, REPO
import subprocess

@Client.on_message(filters.command("update") & filters.user(OWN))
async def updaterepo(_, message):
    await message.reply_text("`Updating your bot..`")
    try:
        command = f"cd && rm -rf {REPO} && git clone {ROOTREPO} && cd {REPO} && ls && python3 -m root"
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        print("Output:", result.stdout)
        print("Error:", result.stderr)
        print("Return code:", result.returncode)
        exit()
    except Exception as e:
        await message.reply_text("Update Failed ", e)
        print("Error", e)
    
