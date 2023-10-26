from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def next_menu_inline() -> InlineKeyboardMarkup:
    ikm = InlineKeyboardMarkup()
    button = InlineKeyboardButton(text="photo", callback_data="photo")
    button2 = InlineKeyboardButton(text="default location", callback_data="default_location")
    button3 = InlineKeyboardButton(text="back", callback_data="back inline")
    ikm.add(button, button2, button3)
    return ikm