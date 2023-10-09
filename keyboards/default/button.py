from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def menu() -> ReplyKeyboardMarkup:
    rkm = ReplyKeyboardMarkup(resize_keyboard=True)
    button = KeyboardButton("/start")
    button2 = KeyboardButton("/help")
    button3 = KeyboardButton("next")
    rkm.add(button, button2, button3)
    return rkm


def next_menu() -> ReplyKeyboardMarkup:
    rkm = ReplyKeyboardMarkup(resize_keyboard=True)
    button = KeyboardButton("/photo")
    button2 = KeyboardButton("location")
    button3 = KeyboardButton("back")
    rkm.add(button, button2, button3)
    return rkm
