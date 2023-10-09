from aiogram import types
from aiogram.dispatcher.filters import Text
from loader import dp, bot


@dp.message_handler(Text(equals="default_location"))
async def location(message: types.Message):
    await bot.send_location(chat_id=message.chat.id,
                            latitude=41.323417,
                            longitude=69.242648)
    await message.delete()
