from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from database import sqlite_db
from create_bot import dp, bot
from aiogram import Dispatcher, types
from aiogram.dispatcher.filters import Text
import configs

class FMSAdmin(StatesGroup):
    photo = State()
    name = State()
    description = State()
    price = State()

ID = configs.admin_id

async def download_command(callback_query: types.CallbackQuery):
    if callback_query.from_user.id == ID:
        await FMSAdmin.photo.set()
        await callback_query.message.reply('Загрузи фото')

async def cancel_handler(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        current_state = await state.get_state()
        if current_state is None:
            return
        await state.finish()
        await message.reply('Хорошо!')

async def load_photo(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['photo'] = message.photo[0].file_id
        await FMSAdmin.next()
        await message.reply('Теперь введите название')

async def load_name(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['name'] = message.text
        await FMSAdmin.next()
        await message.reply('Теперь введите описание')

async def load_description(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['description'] = message.text
        await FMSAdmin.next()
        await message.reply('Теперь введите цену')

async def load_price(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['price'] = float(message.text)

        await sqlite_db.sql_add_command(state)
        await state.finish()

async def delete_handler(callback_query: types.CallbackQuery):
    await sqlite_db.sql_delete(callback_query.data.replace('delete_', ''))
    await callback_query.answer(text=f"{callback_query.data.replace('delete_', '')} удалена", show_alert=True)


def registerAdminHandlers(dp: Dispatcher):
    dp.register_callback_query_handler(download_command, text='post', state=None)
    dp.register_message_handler(cancel_handler, state="*", commands='Отменить')
    dp.register_message_handler(cancel_handler, Text(equals="Отменить", ignore_case=True), state="*")
    dp.register_message_handler(load_photo, content_types=['photo'], state=FMSAdmin.photo)
    dp.register_message_handler(load_name, state=FMSAdmin.name)
    dp.register_message_handler(load_description, state=FMSAdmin.description)
    dp.register_message_handler(load_price, state=FMSAdmin.price)
    dp.register_callback_query_handler(delete_handler, lambda x: x.data and x.data.startswith('delete_'))