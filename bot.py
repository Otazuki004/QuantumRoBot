#Main Codes
from pyrogram import Client

#variables
from vars import *
#END


#helper
import asyncio

async def aexec(code, client, message):
    exec(
        f'async def __ex(client, message): ' +
        ''.join(f'\n {l}' for l in code.split('\n'))
    )
    return await locals()['__ex'](client, message)
#helperEND
#Imports
import subprocess
from datetime import datetime
import io
import os
import sys
import requests
import wget
import random
import yt_dlp
from pyrogram import filters, enums
from youtube_search import YoutubeSearch
from yt_dlp import YoutubeDL
from pyrogram.errors import MessageTooLong
import pyscreenshot
from subprocess import getoutput as run
import traceback
from contextlib import redirect_stdout
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup

#MainCodesEND-------

#Codedown

#NewModuleSongVideo↓
@bot.on_message(filters.command("video"))
async def video(client, message):
    ydl_opts = {
        "format": "best",
        "keepvideo": True,
        "prefer_ffmpeg": False,
        "geo_bypass": True,
        "outtmpl": "%(title)s.%(ext)s",
        "quite": True,
    }
    query = " ".join(message.command[1:])
    print(query)
    await bot.send_message(OWN, f"Query Type Video '{query}'")
    try:
        results = YoutubeSearch(query, max_results=1).to_dict()
        link = f"https://youtube.com{results[0]['url_suffix']}"
        title = results[0]["title"][:40]
        thumbnail = results[0]["thumbnails"][0]
        thumb_name = f"{title}.jpg"
        thumb = requests.get(thumbnail, allow_redirects=True)
        open(thumb_name, "wb").write(thumb.content)
        results[0]["duration"]
        results[0]["url_suffix"]
        results[0]["views"]
        message.from_user.mention
    except Exception as e:
        print(e)
        await bot.send_message(OWN, e)
    try:
        msg = await message.reply("Video Processing..")
        with YoutubeDL(ydl_opts) as ytdl:
            ytdl_data = ytdl.extract_info(link, download=True)
            file_name = ytdl.prepare_filename(ytdl_data)
    except Exception as e:
        return await msg.edit(f"🚫 Error: {e}")
    preview = wget.download(thumbnail)
    await msg.edit("Process Complete.\n Now Uploading.")
    title = ytdl_data["title"]
    await message.reply_video(
        file_name,
        duration=int(ytdl_data["duration"]),
        thumb=preview,
        caption=f"**{title}**",
    )

    await msg.delete()
    try:
        os.remove(file_name)
        await bot.send_message(OWN, "New success")
    except Exception as e:
        print(e)
        await bot.send_message(OWN, f"Failed To remove File '{query}' Error = '{e}'")


flex = {}
chat_watcher_group = 3

ydl_opts = {
    "format": "best",
    "keepvideo": True,
    "prefer_ffmpeg": False,
    "geo_bypass": True,
    "outtmpl": "%(title)s.%(ext)s",
    "quite": True,
}


@bot.on_message(filters.command("song"))
def song(_, message):
    query = " ".join(message.command[1:])
    print(query)
    bot.send_message(OWN, f"New Query Type Audio '{query}'")
    m = message.reply("🔄 Searching....")
    ydl_ops = {"format": "bestaudio[ext=m4a]"}
    try:
        results = YoutubeSearch(query, max_results=1).to_dict()
        link = f"https://youtube.com{results[0]['url_suffix']}"
        title = results[0]["title"][:40]
        thumbnail = results[0]["thumbnails"][0]
        thumb_name = f"{title}.jpg"
        thumb = requests.get(thumbnail, allow_redirects=True)
        open(thumb_name, "wb").write(thumb.content)
        duration = results[0]["duration"]

    except Exception as e:
        m.edit(
            "⚠️ No results were found. Make sure you typed the information correctly"
        )
        print(str(e))
        bot.send_message(OWN, e)
        return
    m.edit("📥 Downloading ..")
    try:
        with yt_dlp.YoutubeDL(ydl_ops) as ydl:
            info_dict = ydl.extract_info(link, download=False)
            audio_file = ydl.prepare_filename(info_dict)
            ydl.process_info(info_dict)
        secmul, dur, dur_arr = 1, 0, duration.split(":")
        for i in range(len(dur_arr) - 1, -1, -1):
            dur += int(float(dur_arr[i])) * secmul
            secmul *= 60
        m.edit("📤 Uploading ..")

        message.reply_audio(
            audio_file,
            thumb=thumb_name,
            title=title,
            caption=f"**{title}**",
            duration=dur,
        )
        m.delete()
    except Exception as e:
        m.edit(f"**Error:**{e} ")
        print(e)
        bot.send_message(OWN, e)

    try:
        os.remove(audio_file)
        os.remove(thumb_name)
        bot.send_message(OWN, "new success")
    except Exception as e:
        print(e)
        bot.send_message(OWN, "Failed To remove File '{query}' Error = '{e}'")
        
print("success")
#song and video module complete

#NewModuleDEV
@bot.on_message(filters.command("developer"))
def dev(client, message):
	bot.send_message(message.chat.id, f"Please Send Like `/developerequest [your userid] [your username]`")
	
@bot.on_message(filters.command("developerequest"))
def devreq(client, message):
    query = " ".join(message.command[1:])
    print(query)
    bot.send_message(OWN, f"New Developer Request = {query}")
    bot.send_message(message.chat.id, "Request Send")
	
#DEVEND




#AliveModule

@bot.on_message(filters.command("alive"))
def Alive(client, message):
	print("hm")
	bot.send_message(message.chat.id, "Alive")
	
#AliveModuleEND




#RestartProgramModule
def restart_program():
    python = sys.executable
    os.execl(python, python, *sys.argv)
    exit()

@bot.on_message(filters.command("restart") & filters.user(OWN))
def restartbot(client, message):
    print ("Restarting")
    bot.send_message(message.chat.id, "restarting")
    restart_program()
    
    
    
#restartProgramEND


#NewModulesEvalCode

@bot.on_message(filters.command(["run","eval"],["?","!",".","*","/","$"]) & filters.user(ODEV))
async def eval(client, message):
    if len(message.text.split()) <2:
          return await message.reply_text("`No input?`")
    status_message = await message.reply_text("Processing ...")
    cmd = message.text.split(None, 1)[1]
    start = datetime.now()
    reply_to_ = message
    if message.reply_to_message:
        reply_to_ = message.reply_to_message

    old_stderr = sys.stderr
    old_stdout = sys.stdout
    redirected_output = sys.stdout = io.StringIO()
    redirected_error = sys.stderr = io.StringIO()
    stdout, stderr, exc = None, None, None

    try:
        await aexec(cmd, client, message)
    except Exception:
        exc = traceback.format_exc()

    stdout = redirected_output.getvalue()
    stderr = redirected_error.getvalue()
    sys.stdout = old_stdout
    sys.stderr = old_stderr

    evaluation = ""
    if exc:
        evaluation = exc
    elif stderr:
        evaluation = stderr
    elif stdout:
        evaluation = stdout
    else:
        evaluation = "Success"
    end = datetime.now()
    ping = (end-start).microseconds / 1000
    final_output = "<b>📎 Input</b>: "
    final_output += f"<code>{cmd}</code>\n\n"
    final_output += "<b> ⚙️ Output</b>:\n"
    final_output += f"<code>{evaluation.strip()}</code> \n\n"
    final_output += f"<b>✨ Time</b>: {ping}<b>ms</b>"
    if len(final_output) > 4096:
        with io.BytesIO(str.encode(final_output)) as out_file:
            out_file.name = "eval.text"
            await reply_to_.reply_document(
                document=out_file, caption=cmd, disable_notification=True
            )
    else:
        await status_message.edit_text(final_output)

#EvalCodeEND


#NewModuleShell


@bot.on_message(filters.command(["sh","shell"],["?","!",".","*","/","$"])& filters.user(ODEV))
async def sh(client, message):
    code = message.text.replace(message.text.split(" ")[0], "")
    x = run(code)
    string = f"**📎 Input**: `{code}`\n\n**📒 Output **:\n`{x}`"
    try:
        await message.reply_text(string)        
    except Exception as e:
        with io.BytesIO(str.encode(string)) as out_file:
            out_file.name = "shell.text"
            await message.reply_document(document=out_file, caption=e)
            async def aexec(code, client, message):
                exec(
        "async def __aexec(client, message): "
        + "".join(f"\n {l_}" for l_ in code.split("\n"))
    )
    return await locals()["__aexec"](client, message)
#ShellEND

#EnhanceStartModule from vexera-


tate = [
    [
InlineKeyboardButton("Developer Commands", 
callback_data="dhelp"),
    ],
    [

InlineKeyboardButton("Administrator Commands", 
callback_data="adminp"),
    ],
]

@bot.on_callback_query(filters.regex("dhelp"))
async def cbbasic(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""**
/eval - To run A Code
/restart - Restart The While Bot (Owner Only)
/sh - To Run Shell Codes
**
""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Go Back", callback_data="help")]]
        ),
    )


@bot.on_callback_query(filters.regex("help"))
async def cbbasic(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""**
/song - To Get what song you want 
/video - To Get What Video you Want 
/alive - To Check bot alive or not
/id - Get a User Id/Chat ID
/help - To Check a Bot Commands
/tm - Reply a media To Get telegra.ph link
/dice - Bot send you random dice
/ping - To Check ping
**
""",
        reply_markup=InlineKeyboardMarkup (tate),
    )

ADM = f"""**
/admins - To Get Admin list in your group 
/ban - Reply to ban Anyone (Admin)
/unban - Reply to Unban Anyone (Admin)
/pin - To Pin a any message (Admin)
/unpin - To unpin a any message (Admin)
/del - To Delete a any message (admin)
/promote - To promote Anyone (Admin)
/setgtitle - To Change Group Title (Admin)
/setgpic - To Change Group pic (Admin)
**
"""

START = f"""**
────「 [{B_F_N}](https://graph.org//file/3650014818cd34600f408.jpg) 」────
Hᴇʏ, User!!
I ᴀᴍ {B_NAME} I Hᴀᴠᴇ Cᴏᴏʟ Fᴇᴀᴛᴜʀᴇs
➖➖➖➖➖➖➖➖➖➖➖➖➖
[Pᴀᴛᴄʜ Uᴘᴅᴀᴛᴇ Dᴇᴛᴀɪʟs]
➖➖➖➖➖➖➖➖➖➖
Lᴀsᴛ Uᴘᴅᴀᴛᴇ : --:--:--
Pᴀᴛᴄʜ Nᴀᴍᴇ : Under Devlopment
➖➖➖➖➖➖➖➖➖➖➖➖➖
Nᴇxᴛ Pᴀᴛᴄʜ Dᴀᴛᴇ : 1:1:24
Nᴇxᴛ Pᴀᴛᴄʜ Nᴀᴍᴇ : Release (ᴠ1)

Click Help To know My Magical Powers⚡**
"""
buttons = [
    [
        InlineKeyboardButton(
            text=f"[► Add {B_NAME} In Your Group ◄]",
            url=f"https://telegram.dog/Quantum004Bot?startgroup=true",
        )
    ],
    [
        InlineKeyboardButton("📚 Help 📚", 
callback_data="help"),
    ],
    [
        InlineKeyboardButton(
            text="[► Support ◄]", url=f"https://telegram.dog/{S_URL}"
        ),
        InlineKeyboardButton(text="📢 Updates", url="https://telegram.dog/Hyper_Speed0"),
    ],
]


@bot.on_message(filters.command("start") & filters.private)
def start(bot, message):
    text = START
    reply_markup = InlineKeyboardMarkup (buttons)
    message.reply(
    text=text,
    reply_markup=reply_markup,
    disable_web_page_preview=False
)

@bot.on_callback_query(filters.regex("adminp"))
async def cbbasic(_, query: CallbackQuery):
    await query.edit_message_text(
    text = ADM,
    reply_markup = InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Back", callback_data="help")]]
        ),
    )



#StartEND
#GroupStartModule

STA1= f"""**
── {B_F_N} ──

۞ I'ᴍ ᴀɴɪᴍᴇ ʙᴀsᴇᴅ Pᴏᴡᴇʀғᴜʟ Bᴏᴛ ᴘᴏᴡᴇʀᴇᴅ ʙʏ 𝗛ʏᴘᴇʀ 𝗦ᴘᴇᴇᴅ™
.
۞ I'ᴍ Aʟᴡᴀʏs Wᴏʀᴋ & Uʟᴛʀᴀ Sᴘᴇᴇᴅ & Hᴇʟᴘ Tᴏ ᴍᴀɴɢᴇ Yᴏᴜʀ ɢʀᴏᴜᴘ ♡
۞ Usᴇ ᴍᴇ ᴛᴏ Kɴᴏᴡ Wʜᴀᴛ ɪs Mᴀɢɪᴄ!
"""
PIC = (
 "https://telegra.ph/file/c4b5257049c672290306e.jpg", "https://telegra.ph/file/4135682365c0754618cf5.jpg", "https://telegra.ph/file/1dcfff90307b6f45de00e.jpg"

)

@bot.on_message(filters.command("start") & filters.group)
def start(bot, message):
        P = random.choice(PIC)
        bot.send_photo(message.chat.id, photo=P, caption=STA1, reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("📚 Help", callback_data="help")]]
        ),
    )

#GroupStartEND

#NewModuleAdmins


#AdminsEND

#NewModuleWebSS
# Define a handler function for /webss command
@bot.on_message(filters.command("webss"))
def webss(client, message):
    # Get the url from the command argument
    url = message.command[1]
    # Check if the url is valid
    if url.startswith("http://") or url.startswith("https://"):
        # Take a screenshot of the web page using pyscreenshot
        img = pyscreenshot.grab(url=url)
        # Save the image as a temporary file
        name = "temp.png"
        img.save(name)
        # Send the image as a document to the chat
        message.reply_document(document=open(name, "rb"))
    else:
        # Send an error message if the url is invalid
        message.reply("Please provide a valid url.")
	   
#WebSSEND
#NewModuleStopBot
def kill():
    exit()

@bot.on_message(filters.regex("/stop") & filters.user(OWN))
def killbot(client, message):
    print ("Force Stoping bot..")
    bot.send_message(message.chat.id, "success")
    kill()
#Exprementsss




bot.run()
