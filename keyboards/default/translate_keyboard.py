from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def main() -> ReplyKeyboardMarkup:
    rkm = ReplyKeyboardMarkup(resize_keyboard=True)
    button = KeyboardButton("En🇬🇧/🇺🇿Uz")
    button2 = KeyboardButton("Uz🇺🇿/🇬🇧En")
    rkm.add(button, button2)
    return rkm
