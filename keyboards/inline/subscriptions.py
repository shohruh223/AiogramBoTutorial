from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def check_button():
    ikm = InlineKeyboardMarkup()
    button = InlineKeyboardButton(text="Obunani tekshirish",
                                  callback_data="check_subs")
    ikm.add(button)
    return ikm
