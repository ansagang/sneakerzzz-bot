from aiogram import Dispatcher, types
from create_bot import dp, bot
from keyboards import clientBackKeyboard, clientMenuKeyboard, clientAdminMenuKeyboard
from database import sqlite_db
import configs

async def start_command(message: types.Message):
    try:
        if message.from_user.id == configs.admin_id:
            await bot.send_photo(message.from_user.id, open('C:/Users/Ансар/Documents/FBMD/Back-End/telegramBots/SneakerzzzBot/assets/sneakerzzz-logo.jpeg', 'rb'), caption=f'Здравствуйте, сэр {message.from_user.full_name}', reply_markup=clientAdminMenuKeyboard)
        else: 
            await bot.send_photo(message.from_user.id, open('C:/Users/Ансар/Documents/FBMD/Back-End/telegramBots/SneakerzzzBot/assets/sneakerzzz-logo.jpeg', 'rb'), caption=f'Здравствуйте, {message.from_user.full_name}', reply_markup=clientMenuKeyboard)
        await message.delete()
    except:
        await message.reply('Для начала напишите в ЛС: \n https://t.me/SneakerzzzBot')

async def random_handler(message: types.Message):
    try:
        await sqlite_db.sql_random(message)
        await message.delete()
    except:
        await message.reply('Для начала напишите в ЛС: \n https://t.me/SneakerzzzBot')

async def start_handler(callback_query: types.CallbackQuery):
    try:
        if callback_query.from_user.id == configs.admin_id:
            await bot.edit_message_caption(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id, caption=f'Здравствуйте, сэр {callback_query.from_user.full_name}', reply_markup=clientAdminMenuKeyboard)
        else:
            await bot.edit_message_caption(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id, caption=f'Здравствуйте, {callback_query.from_user.full_name}', reply_markup=clientMenuKeyboard)
    except:
        await callback_query.message.reply('Для начала напишите в ЛС: \n https://t.me/SneakerzzzBot')

async def information_handler(callback_query: types.CallbackQuery):
    try:
        await bot.edit_message_caption(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id, caption='Информация:\n\nРежим работы: Вс-Чт с 9:00 до 20:00\nРасположение: Мангилик ел 38', reply_markup=clientBackKeyboard)
    except:
        await callback_query.answer('Для начала напишите в ЛС: \n https://t.me/SneakerzzzBot')

async def capability_handler(callback_query: types.CallbackQuery):
    try:
       await bot.edit_message_caption(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id, caption='Возможности:\n\nКак искать кроссовки❓\n• Напишите название кроссовок.\n\nКак получить случайную пару кроссовок❓\n• Напишите команду /random', reply_markup=clientBackKeyboard)
    except:
        await callback_query.answer('Для начала напишите в ЛС: \n https://t.me/SneakerzzzBot')

async def catalog_handler(callback_query: types.CallbackQuery):
    try:
        await sqlite_db.sql_get(callback_query)
    except:
        await callback_query.answer('Для начала напишите в ЛС: \n https://t.me/SneakerzzzBot')

async def remove_handler(callback_query: types.CallbackQuery):
    try:
        await bot.delete_message(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id)
    except:
        await callback_query.answer('Для начала напишите в ЛС: \n https://t.me/SneakerzzzBot')

async def product_handler(callback_query: types.CallbackQuery):
    try:
        await sqlite_db.sql_get_one(callback_query, callback_query.data.replace('product_', ''))
    except: 
        await callback_query.answer('Для начала напишите в ЛС: \n https://t.me/SneakerzzzBot')

def registerClientHandlers(dp: Dispatcher):
    dp.register_message_handler(start_command, commands=['start'])
    dp.register_message_handler(random_handler, commands=['random'])
    dp.register_callback_query_handler(start_handler, text='back')
    dp.register_callback_query_handler(information_handler, text='information')
    dp.register_callback_query_handler(catalog_handler, text='catalog')
    dp.register_callback_query_handler(capability_handler, text='capability')
    dp.register_callback_query_handler(product_handler, lambda x: x.data and x.data.startswith('product_'))
    dp.register_callback_query_handler(remove_handler, text='remove')