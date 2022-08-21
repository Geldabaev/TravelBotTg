from aiogram.types import ReplyKeyboardMarkup, KeyboardButton#, ReplyKeyboardRemove
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


add_button = KeyboardButton('Добавить кнопку')
del_button = KeyboardButton('Удалить кнопку')
AddDell = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
AddDell.row(add_button, del_button)
