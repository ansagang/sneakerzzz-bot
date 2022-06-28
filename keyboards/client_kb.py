import re
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

btn1 = KeyboardButton('/Информация')
btn2 = KeyboardButton('/Меню')
# btn3 = KeyboardButton('Поделиться номером', request_contact=True)
# btn4 = KeyboardButton('Поделиться локацией', request_location=True)

clientKeyboard = ReplyKeyboardMarkup(resize_keyboard=True)

clientKeyboard.add(btn1).add(btn2)