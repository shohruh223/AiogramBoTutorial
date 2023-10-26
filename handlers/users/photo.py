from aiogram import types
from aiogram.types import ReplyKeyboardRemove

from keyboards.default.button import menu
from loader import dp, bot

image_url = ("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRC9l-185Y2Wy"
             "sKc1QCrck5U54YnbtyQkRXtR2eZ-LiYupI2JGxXWdQpzO9t9MutbAKbKo&usqp=CAU")


@dp.message_handler(commands="photo")
async def photo(message: types.Message):
    await bot.send_photo(chat_id=message.chat.id,
                         photo=image_url)


@dp.callback_query_handler()
async def photo_callback(callback: types.CallbackQuery):
    if callback.data == "photo":
        await callback.message.answer_photo(photo=image_url)
    elif callback.data == "default_location":
        await callback.message.answer_location(latitude=41.325824,
                                               longitude=69.2405464)
    elif callback.data == "back inline":
        await callback.message.answer(text="Back",
                                      reply_markup=menu())
