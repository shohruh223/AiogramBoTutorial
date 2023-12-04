from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def youtube_button():
    rkm = ReplyKeyboardMarkup(resize_keyboard=True)
    button = KeyboardButton(text="music")
    button2 = KeyboardButton(text="video")
    rkm.add(button, button2)
    return rkm