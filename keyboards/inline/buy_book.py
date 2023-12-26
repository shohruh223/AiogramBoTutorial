from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def book_keys():
    ikm = InlineKeyboardMarkup()
    button = InlineKeyboardButton(text="📍 Eng yaqin do'konni topish", callback_data="mylocation")
    button2 = InlineKeyboardButton(text="📱 Kontakt ulashish", callback_data="mycontact")
    ikm.add(button2, button)
    return ikm