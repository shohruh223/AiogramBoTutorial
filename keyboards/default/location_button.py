from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def loc_button():
    rkm = ReplyKeyboardMarkup(resize_keyboard=True)
    button = KeyboardButton(text="📍", request_location=True)
    rkm.add(button)
    return rkm