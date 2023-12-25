from aiogram import types
from loader import dp, bot
from utils import remove_background
from utils.photograph import photo_link


# rasmlarimizni to'g'ridan to'g'ri internetda saqlash funksiyasi
# @dp.message_handler(content_types='photo')
# async def photo_handler(message: types.Message):
#     photo = message.photo[-1]
#     link = await photo_link(photo)
#     await message.answer(link)


@dp.message_handler(content_types='photo')
async def photo_handler(message: types.Message):
    photo = message.photo[-1]
    link = await photo_link(photo)
    await message.answer(link)
    new_photo = await remove_background(link)
    await message.reply_document(document=new_photo, caption="Bu fayl")
    # await message.reply_photo(new_photo, caption="Bu rasm")
