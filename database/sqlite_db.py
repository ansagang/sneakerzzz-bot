import sqlite3 as sq
from create_bot import bot
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import configs

def sql_start():
    global base, cur
    base = sq.connect(configs.bot_database)
    cur = base.cursor()
    if base:
        print('Database connected!')
    base.execute('CREATE TABLE IF NOT EXISTS menu(img TEXT, name TEXT PRIMARY KEY, description TEXT, price TEXT)')
    base.commit()

async def sql_add_command(state):
    async with state.proxy() as data:
        cur.execute('INSERT INTO menu VALUES (?, ?, ?, ?)', tuple(data.values()))
        base.commit()
        
async def sql_get(callback_query):
    clientCatalogKeyboard = InlineKeyboardMarkup()
    for ret in cur.execute('SELECT * FROM menu').fetchall():
        clientCatalogKeyboard.add(InlineKeyboardButton(f'{ret[1]} • {ret[3]}', callback_data=f'product_{ret[1]}'))
    clientCatalogKeyboard.add(InlineKeyboardButton('« Назад', callback_data='back'))
    await bot.edit_message_caption(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id, caption='Каталог:', reply_markup=clientCatalogKeyboard)

async def sql_get_one(callback, data):
    for ret in cur.execute('SELECT * FROM menu WHERE name == ?', (data, )).fetchall():
        if callback.from_user.id == configs.admin_id:
            await bot.send_photo(callback.from_user.id, ret[0], f'{ret[1]}\nОписание: {ret[2]}\nЦена: {ret[3]}', reply_markup=InlineKeyboardMarkup().add(InlineKeyboardButton(f'Удалить {ret[1]}', callback_data=f'delete_{ret[1]}')).add(InlineKeyboardButton('🔻', callback_data='remove')))
        else:
             await bot.send_photo(callback.from_user.id, ret[0], f'{ret[1]}\nОписание: {ret[2]}\nЦена: {ret[3]}', reply_markup=InlineKeyboardMarkup().add(InlineKeyboardButton('🔻', callback_data='remove')))

async def sql_get_option():
    return cur.execute('SELECT * from menu').fetchall()

async def sql_search(message):
    clientCatalogKeyboard = InlineKeyboardMarkup()
    for ret in cur.execute(f"SELECT * FROM menu WHERE name like (?)", ('%'+message.text+'%', )).fetchall():
        clientCatalogKeyboard.add(InlineKeyboardButton(f'{ret[1]} • {ret[3]}', callback_data=f'product_{ret[1]}'))
    clientCatalogKeyboard.add(InlineKeyboardButton('« Назад', callback_data='remove'))
    await message.delete()
    await bot.send_message(message.chat.id, f'Поисковой запрос: {message.text}', reply_markup=clientCatalogKeyboard)

async def sql_delete(data):
    cur.execute('DELETE FROM menu WHERE name == ?', (data, ))
    base.commit()