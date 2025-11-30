from aiogram.types import ReplyKeyboardMarkup,KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from json_reader import get_all_ru_diseases

async def add_keyboard(page : int):
    keyboard = ReplyKeyboardBuilder()
    disease_list = await get_all_ru_diseases()

    for i in  range(10):
        try:
            keyboard.add(KeyboardButton(text=disease_list[i+(page*10)]))
        except IndexError:
            keyboard.add(KeyboardButton(text=" "))

    keyboard.add(KeyboardButton(text="<<<"))
    keyboard.add(KeyboardButton(text=">>>"))

    keyboard.adjust(2)
    keyboard = keyboard.as_markup()
    keyboard.resize_keyboard = True

    return keyboard