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
    button = InlineKeyboardButton(text="edit", callback_data="edit user")
    button2 = InlineKeyboardButton(text="delete", callback_data="delete")
    button3 = InlineKeyboardButton(text="back", callback_data="back")
    ikm.add(button, button2, button3)
    return ikm


def edit_user_check():
    ikm = InlineKeyboardMarkup(row_width=1)
    button = InlineKeyboardButton(text="fullname", callback_data="edit_fullname")
    button2 = InlineKeyboardButton(text="age", callback_data="edit_age")
    button3 = InlineKeyboardButton(text="phone_number", callback_data="edit_phone_number")
    button4 = InlineKeyboardButton(text="photo", callback_data="edit_photo")
    ikm.add(button, button2, button3, button4)
    return ikm