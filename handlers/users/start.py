from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Salom, {message.from_user.full_name}!")


@dp.message_handler(content_types="photo")
async def text_photo_message(message: types.Message):
    await message.reply("You send photo")


@dp.message_handler(content_types="video")
async def text_photo_message(message: types.Message):
    await message.reply("You send video")


@dp.message_handler(content_types="document")
async def text_photo_message(message: types.Message):
    await message.reply("You send document")


# @dp.message_handler(user_id="")
# async def self_message(message: types.Message):
#     await message.answer(f"Your user_id {}")
