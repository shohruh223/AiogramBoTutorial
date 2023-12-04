from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types import ReplyKeyboardRemove

from keyboards.default.button import youtube_button
from loader import dp
from states.yt import Music, Video


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Salom, {message.from_user.full_name}!",
                         reply_markup=youtube_button())


@dp.message_handler(Text(equals="music"))
async def music_start(message: types.Message):
    await message.answer(f"Yoqtirgan videoyingizni linkini jo'nating!",
                         reply_markup=ReplyKeyboardRemove())
    await Music.link.set()


@dp.message_handler(Text(equals="video"))
async def video_start(message: types.Message):
    await message.answer(f"Yoqtirgan videoyingizni linkini jo'nating!",
                         reply_markup=ReplyKeyboardRemove())
    await Video.link.set()

