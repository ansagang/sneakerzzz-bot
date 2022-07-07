from aiogram.utils import executor
from create_bot import dp
from handlers import client, admin, general
from database import sqlite_db

async def on_startup(_):
    sqlite_db.sql_start()
    print('Bot is online')

client.registerClientHandlers(dp)
admin.registerAdminHandlers(dp)
general.registerGeneralHandlers(dp)

executor.start_polling(dp, skip_updates=True, on_startup=on_startup)