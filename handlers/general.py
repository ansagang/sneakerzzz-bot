from aiogram import Dispatcher, types
import json, string
from create_bot import dp

async def filter(message: types.Message):
    if {i.lower().translate(str.maketrans('', '', string.punctuation)) for i in message.text.split(' ')}\
        .intersection(set(json.load(open('C:/Users/Ансар/Documents/FBMD/Back-End/SneakerzzzBot/cuss_words.json')))) != set():
        await message.delete()

def registerGeneralHandlers(dp: Dispatcher):
    dp.register_message_handler(filter)