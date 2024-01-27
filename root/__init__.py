import os
from pyrogram import *
from pymongo import MongoClient

ROOTREPO = "https://github.com/otazuki004/QuantumRoBot.git"#Your Repo Link
REPO = "QuantumRoBot"
prefix = [".","!","?","*","$","#","/"]
a_id = "10187126" # Your Api Id
a_hash = "ff197c0d23d7fe54c89b44ed092c1752" # Your Api Hash 
b_tok = "6910428877:AAFIFbleAgAtf42tNQuty-gRbl4ybWIIPCQ" # Your Bot Token
OWN = 5965055071 #OWNERID
CHAT_S_ID = "-1001859707851" #supportchatid
B_NAME = "QuantumRoBot" #Botname
OWN_NAME = "Otazuki" #Ownername
allowbw = True
FRD_MSG = True # allow Forwarding Privite message from bot
OWN_USRNAMER = "Otazuki" #OwnerUsername
DEV = 5485459348 #Add DEV Id
ODEV = [OWN, DEV]
B_F_N = "𝙌𝙪𝙖𝙣𝙩𝙪𝙢𝙍𝙤𝘽𝙤𝙩" #Bot Name in font
S_URL = "FutureCity005" #Support Group url
B_ID = "" #Botid
data_store_id = "-1002075414845" #Add your Log group ID and Add the bot in that group 
B_US = "Quantum004bot" # Bot Username
PRE = [".","/","$","+"]
ROOTVER = "1.0.2" #Bot Version 
#ImageSection
ST_PIC = "https://te.legra.ph/file/283f5c4ae89078521e0df.jpg" # Start Command Picture

#addclients
bot = Client(f"{B_NAME}", bot_token=b_tok, api_id=a_id, api_hash=a_hash, plugins=dict(root="root/plugins"))
#clientsEND

#Dont Touch This
DIR = f"{os.getcwd()}/"

video_formats = ['mp4', 'avi', 'mkv', 'mov', 'wmv', 'flv', 'webm', '3gp']
audio_formats = ['mp3', 'wav', 'ogg', 'aac', 'flac', 'wma', 'm4a']
text_formats = ['txt', 'csv', 'json', 'xml', 'html', 'md', 'pdf', 'text']
coding_languages = ['py', 'java', 'js', 'c', 'css', 'ruby', 'php', 'swift']
Image_Formats = ['jpeg', 'png', 'gif', 'tiff', 'bmp', 'webp', 'jpg']
other_formats = ['apk', 'bat', 'jar', 'iso', 'rar', '7z', 'tar.gz', 'tar.bz2', 'zip', 'tar']

formats = [video_formats, audio_formats, text_formats, coding_languages, Image_Formats, other_formats]


