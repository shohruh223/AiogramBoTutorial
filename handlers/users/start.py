from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.translate_keyboard import main
from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Welcome to translate bot !!",
                         reply_markup=main())
