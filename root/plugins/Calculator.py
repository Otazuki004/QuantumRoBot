# AN A HYPER SPEED PROJECT

import re
import asyncio
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from root.__main__ import bot

# Dictionary to store user inputs
user_inputs = {}

async def calculate_expression(expression):
    try:
        await bot.send_message(message.chat.id, expression)
        output = eval(expression)
        return f"Result: {output}"
    except Exception as e:
        return f"Error: {e}"

@bot.on_message(filters.command("calculator"))
def start_calculator(_, message):
    user_id = message.from_user.id
    user_inputs[user_id] = {"numbers": [], "operator": None}

    keyboard = [
        [InlineKeyboardButton(str(i), callback_data=str(i)) for i in range(1, 10)],
        [InlineKeyboardButton("0", callback_data="0"),
         InlineKeyboardButton("9", callback_data="9")],
        [InlineKeyboardButton("+", callback_data="+"),
         InlineKeyboardButton("-", callback_data="-"),
         InlineKeyboardButton("x", callback_data="*"),
         InlineKeyboardButton("Ã·", callback_data="/"),
         InlineKeyboardButton("%", callback_data="%")],
        [InlineKeyboardButton("Enter", callback_data="enter"),
         InlineKeyboardButton("Finish", callback_data="finish")]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)
    message.reply_text("Choose a number:", reply_markup=reply_markup)

@bot.on_callback_query()
async def calculator_callback(_, query):
    user_id = query.from_user.id

    if query.data.isdigit() or query.data in ["+", "-", "*", "/", "%"]:
        user_inputs[user_id]["numbers"].append(query.data)
    elif query.data == "enter":
        if user_inputs[user_id]["numbers"]:
            user_inputs[user_id]["operator"] = None  # Reset operator after each number
            await query.answer("Number added successfully!", show_alert=True)
        else:
            await query.answer("Please select a number first.", show_alert=True)
            return
    elif query.data == "finish":
        if user_inputs[user_id]["numbers"]:
            expression = ''.join(user_inputs[user_id]["numbers"])
            result_message = await calculate_expression(expression)
            await query.answer(result_message, show_alert=True)
        else:
            await query.answer("No numbers selected.", show_alert=True)
            return

    # Update inline keyboard
    keyboard = [
        [InlineKeyboardButton(str(i), callback_data=str(i)) for i in range(1, 10)],
        [InlineKeyboardButton("0", callback_data="0"),
         InlineKeyboardButton("9", callback_data="9")],
        [InlineKeyboardButton("+", callback_data="+"),
         InlineKeyboardButton("-", callback_data="-"),
         InlineKeyboardButton("x", callback_data="*"),
         InlineKeyboardButton("Ã·", callback_data="/"),
         InlineKeyboardButton("%", callback_data="%")],
        [InlineKeyboardButton("Enter", callback_data="enter"),
         InlineKeyboardButton("Finish", callback_data="finish")]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text("Current Expression: " + ''.join(user_inputs[user_id]["numbers"]), reply_markup=reply_markup)
