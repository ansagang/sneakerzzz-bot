from aiogram import Dispatcher, types
import json, string
from create_bot import dp
from database import sqlite_db

async def filter(message: types.Message):
    if {i.lower().translate(str.maketrans('', '', string.punctuation)) for i in message.text.split(' ')}\
        .intersection(set(json.load(open('C:/Users/Ансар/Documents/FBMD/Back-End/telegramBots/SneakerzzzBot/cuss_words.json')))) != set():
        await message.delete()
    else:
        await sqlite_db.sql_search(message)

def registerGeneralHandlers(dp: Dispatcher):
    dp.register_message_handler(filter)