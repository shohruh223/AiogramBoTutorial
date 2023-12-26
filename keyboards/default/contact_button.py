from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def cont_button():
    rkm = ReplyKeyboardMarkup(resize_keyboard=True)
    button = KeyboardButton(text="📱", request_contact=True)
    rkm.add(button)
    return rkm