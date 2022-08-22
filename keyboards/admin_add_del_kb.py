from aiogram.types import ReplyKeyboardMarkup, KeyboardButton#, ReplyKeyboardRemove
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

open_menu = KeyboardButton('Открыть меню')
admin_kb = KeyboardButton('Админ панель')
AdminPanell = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
AdminPanell.add(open_menu).add(admin_kb)



open_file = KeyboardButton('Вывести файл')
add_button = KeyboardButton('Добавить кнопку')
del_button = KeyboardButton('Удалить кнопку')
admin_panell_buttons = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
admin_panell_buttons.row(open_menu).row(add_button, del_button)



