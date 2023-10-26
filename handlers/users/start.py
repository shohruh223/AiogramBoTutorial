from aiogram import types
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types import ReplyKeyboardRemove

from keyboards.default.button import menu, next_menu
from keyboards.inline.button_inline import next_menu_inline
from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(text=f"Salom, {message.from_user.full_name}!",
                         reply_markup=menu())


@dp.message_handler(Text(equals="next"))
async def next_func(message: types.Message):
    await message.answer(text="Keyingi button",
                         reply_markup=next_menu())
    await message.delete()


@dp.message_handler(Text(equals="next inline"))
async def next_func(message: types.Message):
    await message.answer(text="Keyingi button",
                         reply_markup=next_menu_inline())
    await message.answer(text="button o'chirildi",
                         reply_markup=ReplyKeyboardRemove())
    await message.delete()


@dp.message_handler(Text(equals="back"))
async def next_func(message: types.Message):
    await message.answer(text="Orqaga qaytish",
                         reply_markup=menu())
    await message.delete()


@dp.message_handler(Text(equals="back inline"))
async def next_func(message: types.Message):
    await message.answer(text="Orqaga qaytish",
                         reply_markup=menu())
    await message.delete()
