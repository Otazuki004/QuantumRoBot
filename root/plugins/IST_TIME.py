import datetime
from root.__main__ import bot
from pyrogram import *

@bot.on_message(filters.command("time"))
def time(_, message):
    current_time = datetime.datetime.now()
    # Convert the time to Indian time zone
    indian_time = current_time.astimezone(datetime.timezone(datetime.timedelta(hours=5, minutes=30)))
    # Format the time in 12-hour format with seconds
    formatted_time = indian_time.strftime("%I:%M:%S %p")
    message.reply_text(formatted_time)
