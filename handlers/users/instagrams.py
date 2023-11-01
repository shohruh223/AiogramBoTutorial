from aiogram import types
from aiogram.dispatcher.filters import Text
from loader import dp
from utils.insta import downloader


@dp.message_handler(Text(startswith="https://www.instagram.com/"))
async def instagram_down(message: types.Message):
    data = downloader(link=message.text)
    if data == "error":
        await message.answer("Bu linkda hech qanday ma'lumot yo'q")
    else:
        if data['type'] == "image":
            await message.answer_photo(photo=data['media'])
        elif data["type"] == "video":
            await message.answer_video(video=data['media'])
        elif data['type'] == 'carousel':
            for i in data["media"]:
                await message.answer_document(document=i)
        else:
            await message.answer("Hech qanday link yo'q")
