from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def user_button():
    rkm = ReplyKeyboardMarkup(resize_keyboard=True)
    button = KeyboardButton(text="✅ Ro'yxatdan o'tish")
    rkm.add(button)
    return rkm


def cancel_button():
    rkm = ReplyKeyboardMarkup(resize_keyboard=True)
    button = KeyboardButton(text="🔙 orqaga qaytish")
    rkm.add(button)
    return rkm