from aiogram import types
from aiogram.dispatcher import FSMContext
from loader import dp, bot
from states.user import AddUserState
import re


@dp.message_handler(state=AddUserState.fullname)
async def add_fullname(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["name"] = message.text

    await message.answer("Yoshingizni kiriting")
    await AddUserState.next()


@dp.message_handler(state=AddUserState.age)
async def add_age(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        try:
            data["age"] = int(message.text)
            await message.answer("Telefon raqamingizni kiriting")
            await AddUserState.next()
        except:
            await message.answer("Butun son kiriting")


@dp.message_handler(state=AddUserState.phone_number)
async def add_phone_number(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        PHONE_REGEX = r"^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$"
        phone_number = re.match(PHONE_REGEX, message.text)
        if phone_number:
            data["phone_number"] = message.text
            await AddUserState.next()
            await message.answer("Rasmingizni jo'nating")
        else:
            await message.answer("Telefon raqam xato kiritildi, iltimos to'g'ri kiriting")


@dp.message_handler(state=AddUserState.photo, content_types="photo")
async def add_photo(message: types.Message, state: FSMContext):
    photo = message.photo[-1]
    file_id = photo.file_id
    async with state.proxy() as data:
        data["photo"] = file_id
        await state.finish()

        await bot.send_photo(chat_id=message.chat.id,
                             photo=data["photo"],
                             caption=f"Ismingiz: <b>{data['name'].title()}</b>,\n"
                             f"Yoshingiz: <b>{data['age']}</b>da,\n"
                             f"Telefon raqamingiz: <b>{data['phone_number']}</b>",
                             parse_mode="HTML")