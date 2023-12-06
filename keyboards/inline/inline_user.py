from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from utils.db_api.user import Database

db = Database()


def show_users():
    ikm = InlineKeyboardMarkup(row_width=2)
    for user in db.all_user():
        button = InlineKeyboardButton(text=f"{user[1]}", callback_data=f"ID:{user[0]}")
        ikm.add(button)
    button1 = InlineKeyboardButton(text="🛒 Back to home",
                                   callback_data="back")
    ikm.add(button1)
    return ikm


def edit_users():
    ikm = InlineKeyboardMarkup(row_width=2)
    button = InlineKeyboardButton(text="edit", callback_data="edit")
    button2 = InlineKeyboardButton(text="delete", callback_data="delete")
    button3 = InlineKeyboardButton(text="back", callback_data="back")
    ikm.add(button, button2, button3)
    return ikm


# def edit_users():
#     ikm = InlineKeyboardMarkup(row_width=2)
#     for user in db.all_user():
#         button = InlineKeyboardButton(text=f"{user[1]}", callback_data=f"Id:{user[0]}")
#         ikm.add(button)
#     button1 = InlineKeyboardButton(text="🛒 Back to home",
#                                    callback_data="back")
#     ikm.add(button1)
#     return ikm
