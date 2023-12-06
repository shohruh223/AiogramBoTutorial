from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def register_button():
    rkm = ReplyKeyboardMarkup(resize_keyboard=True)
    button = KeyboardButton(text="✅ Ro'yxatdan o'tish")
    rkm.add(button)
    return rkm


def user_button():
    rkm = ReplyKeyboardMarkup(resize_keyboard=True)
    button = KeyboardButton(text="User")
    rkm.add(button)
    return rkm


def cancel_button():
    rkm = ReplyKeyboardMarkup(resize_keyboard=True)
    button = KeyboardButton(text="🔙 orqaga qaytish")
    rkm.add(button)
    return rkm


def is_and_cancel_button():
    rkm = ReplyKeyboardMarkup(resize_keyboard=True)
    button = KeyboardButton(text="Yes")
    button2 = KeyboardButton(text="🔙 orqaga qaytish")
    rkm.add(button, button2)
    return rkm


def crud_button():
    rkm = ReplyKeyboardMarkup(resize_keyboard=True)
    button = KeyboardButton(text="View users")
    button2 = KeyboardButton(text="Get user")
    button3 = KeyboardButton(text="Add user")
    button4 = KeyboardButton(text="Edit user")
    button5 = KeyboardButton(text="Delete user")
    rkm.add(button, button2, button3, button4, button5)
    return rkm