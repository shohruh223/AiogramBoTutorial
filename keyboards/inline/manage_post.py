from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.callback_data import CallbackData

post_callback = CallbackData("create_post", "action")


def confirmation_keyboard():
    ikm = InlineKeyboardMarkup()
    button = InlineKeyboardButton(text="🆗 Chop etish",
                                  callback_data=post_callback.new(action="post"))
    button2 = InlineKeyboardButton(text="❌ Rad etish",
                                   callback_data=post_callback.new(action="cancel"))
    ikm.add(button, button2)
    return ikm
