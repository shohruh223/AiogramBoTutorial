from aiogram import types
from loader import dp, bot

image_url = ("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRC9l-185Y2Wy"
             "sKc1QCrck5U54YnbtyQkRXtR2eZ-LiYupI2JGxXWdQpzO9t9MutbAKbKo&usqp=CAU")


@dp.message_handler(commands="photo")
async def photo(message: types.Message):
    await bot.send_photo(chat_id=message.chat.id,
                         photo=image_url)