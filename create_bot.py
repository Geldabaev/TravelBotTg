"""Промежуточный файл"""
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage


# для хранения данных из fsm
storage = MemoryStorage()

TOKEN = '5319442368:AAH1oCQqFQ4hDghrJj2Bawqtyf_K-k54DD4'

bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=storage)