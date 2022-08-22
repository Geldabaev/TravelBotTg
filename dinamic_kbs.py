from aiogram.types import ReplyKeyboardMarkup, KeyboardButton#, ReplyKeyboardRemove
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import aiogram.utils.markdown as fmt
from kbs import menu

arr = {}

for option in menu:

    _name = option['name']

    arr[_name] = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

    for keyboard in option['keyboards']:

        # _handler = keyboard['handler']

        for button in keyboard['buttons']:

            text = button['text']
            status = button['status']

            button = KeyboardButton(text)
            arr[_name].row(button)