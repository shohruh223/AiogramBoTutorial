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
    button2 = KeyboardButton("default_location")
    button3 = KeyboardButton(text="location", request_location=True)
    button4 = KeyboardButton(text="contact", request_contact=True)
    button5 = KeyboardButton("back")
    rkm.add(button, button2, button3, button4, button5)
    return rkm
