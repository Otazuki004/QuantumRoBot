import requests
from pyrogram import filters, Client
from pyrogram.types import Message
from root.__main__ import bot as app

api_url_chat4 = "https://pervert-api.onrender.com/chatgpt4"

def fetch_data(api_url: str, query: str) -> tuple:
    try:
        response = requests.get(f"{api_url}?query={query}")
        response.raise_for_status()
        data = response.json()
        return data.get("data", "No response from the API."), None
    except requests.exceptions.RequestException as e:
        return None, f"Request error: {e}"
    except Exception as e:
        return None, f"An error occurred: {str(e)}"

@app.on_message()
async def chatgpt4(_: Client, message: Message):
    if len(message.command) < 2:
        return await message.reply_text("Please provide a query.")

    query = " ".join(message.command[1:])
    txt = await message.reply_text("Wait patiently, requesting to API...")
    api_response, error_message = fetch_data(api_url_chat4, query)
    await txt.edit(api_response or error_message)
