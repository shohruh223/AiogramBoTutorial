from aiogram import types
from loader import dp, kurs


@dp.message_handler(commands=['start'])
async def send_wiki(message: types.Message):
    await message.answer(f"Assalamu alaykum {message.from_user.full_name}! \n"
                         f"Men Shohruh Abdurahmon tomonidan yaratilgan UZS-USD kurs botman\n"
                         f"Sizni dollar kursi bo'yicha tanishtirib boraman.\n"
                         f"Ushbu tugmani bosing 👉👉👉 '/dollar' ")


@dp.message_handler(commands=['dollar'])
async def send_wiki(message: types.Message):
    try:
        text = f"Bugungi kurs: 1AQSH dollar = {kurs} so'm"
        await message.answer(text)
    except:
        await message.answer("noto'g'ri urunish")
