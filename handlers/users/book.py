from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.types import InputFile
from keyboards.inline.buy_book import book_keys
from loader import dp


@dp.message_handler(Command("kitob"))
async def send_book(message: types.Message):
    photo = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTjqVHv9MdkLrT_LjI5NCfQzEejb8_8CPJmGgeJgQZtq9rs8xWgxZuAD1A_bJ42jEdTsRE&usqp=CAU"
    msg = "<b>Pythonda Dasturlash Asoslari</b> kitobi.\n"
    msg += "Narxi: 50000 so'm\n\n"
    msg += "<b>Kitob quyidagi do'konlarda sotiladi:</b>\n👉Akademnashr\n👉Hilol nashr\n👉Azon kitoblar\n👉Kitoblar dunyosi"
    await message.reply_photo(photo=photo,
                              caption=msg,
                              reply_markup=book_keys())


@dp.message_handler(Command("kurslar"))
async def send_courses(message: types.Message):
    album = types.MediaGroup()
    photo1 = "AgACAgUAAxkBAAIHa2ErPWwh50geLqoE4Hn5SGCdi09mAAK8rDEbXltZVUoM_yKC7xVRAQADAgADeQADIAQ"
    photo2 = "https://i0.wp.com/mohirdev.uz/wp-content/uploads/photo1627374915.jpeg"
    photo3 = "https://i1.wp.com/mohirdev.uz/wp-content/uploads/Telegram-bot.png"
    photo4 = InputFile(path_or_bytesio="photos/algoritm.png")
    video1 = "BAACAgUAAxkBAAIHT2ErOXldS7NxbW9mdL4tsI18ZqlvAALdAgACXltZVVoMJafxpb77IAQ"
    album.attach_photo(photo=photo1)
    album.attach_photo(photo=photo2)
    album.attach_photo(photo=photo3)
    album.attach_photo(photo=photo4)
    album.attach_video(video=video1, caption="Bizning online kurslarimiz")
    await message.reply_media_group(media=album)