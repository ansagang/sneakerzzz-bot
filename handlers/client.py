from pydoc import cli
from aiogram import Dispatcher, types
from create_bot import dp, bot
from keyboards import clientKeyboard
from aiogram.types import ReplyKeyboardRemove

async def command_start(message: types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Добрый день!', reply_markup=clientKeyboard)
    except:
        await message.reply('Для начала напишите в ЛС: \n https://t.me/SneakerzzzBot')

async def information_command(message: types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Режим работы: Вс-Чт с 9:00 до 20:00\nРасположение: Мангилик ел 38', reply_markup=ReplyKeyboardRemove())
    except:
        await message.reply('Для начала напишите в ЛС: \n https://t.me/SneakerzzzBot')

def registerClientHandlers(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'help'])
    dp.register_message_handler(information_command, commands=['Информация'])