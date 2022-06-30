from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import configs

storage = MemoryStorage()

bot = Bot(token=configs.bot_token)
dp = Dispatcher(bot, storage=storage)