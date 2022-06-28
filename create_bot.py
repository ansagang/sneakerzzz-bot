from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage()

bot = Bot(token='5567852491:AAFiGxVORrcPV1R3P53Hkxu8WkAA1IFFSTk')
dp = Dispatcher(bot, storage=storage)