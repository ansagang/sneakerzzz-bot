from aiogram.utils import executor
from create_bot import dp
from handlers import client, admin, general

async def on_startup(_):
    print('Bot is online')

client.registerClientHandlers(dp)
admin.registerAdminHandlers(dp)
general.registerGeneralHandlers(dp)

executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
