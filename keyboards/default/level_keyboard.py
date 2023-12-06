from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def level_button():
    rkm = ReplyKeyboardMarkup(resize_keyboard=True)
    rkm.add("LEVEL 1️⃣", "LEVEL 2️⃣")
    rkm.add("LEVEL 3️⃣", "LEVEL 4️⃣")
    return rkm


def stop_button():
    rkm = ReplyKeyboardMarkup(resize_keyboard=True)
    rkm.add("🛑 Stop")
    return rkm

