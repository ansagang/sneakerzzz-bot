from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from numpy import equal
from create_bot import dp, bot
from aiogram import Dispatcher, types
from aiogram.dispatcher.filters import Text

class FMSAdmin(StatesGroup):
    photo = State()
    name = State()
    description = State()
    price = State()

ID = None

async def make_changes_command(message: types.Message):
    global ID
    ID = message.from_user.id
    await bot.send_message(message.from_user.id, "Что вы хотите сделать?")
    await message.delete()

async def download_command(message: types.Message):
    if message.from_user.id == ID:
        await FMSAdmin.photo.set()
        await message.reply('Загрузи фото')

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

        async with state.proxy() as data:
            await message.reply(str(data))
        await state.finish()

def registerAdminHandlers(dp: Dispatcher):
    dp.register_message_handler(download_command, commands=['Загрузить'], state=None)
    dp.register_message_handler(cancel_handler, state="*", commands='Отменить')
    dp.register_message_handler(cancel_handler, Text(equals="Отменить", ignore_case=True), state="*")
    dp.register_message_handler(load_photo, content_types=['photo'], state=FMSAdmin.photo)
    dp.register_message_handler(load_name, state=FMSAdmin.name)
    dp.register_message_handler(load_description, state=FMSAdmin.description)
    dp.register_message_handler(load_price, state=FMSAdmin.price)
    dp.register_message_handler(make_changes_command, commands=['admin'], is_chat_admin=True)