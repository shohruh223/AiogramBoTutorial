from aiogram import types
from aiogram.dispatcher.filters import Text
from loader import dp
from utils.service import translate_uz, translate_en


@dp.message_handler(Text(equals="🇬🇧En/Uz🇺🇿"))
async def translate_func(message: types.Message):
    translate = translate_en(text=message.text)
    await message.answer(translate)


@dp.message_handler(Text(equals="Uz🇺🇿/🇬🇧En"))
async def translate_func2(message: types.Message):
    tarjima = translate_uz(text=message.text)
    await message.answer(tarjima)
