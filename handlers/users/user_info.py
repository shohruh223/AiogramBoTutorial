from aiogram.dispatcher import FSMContext
from loader import dp, bot
from aiogram import types
from states.user import UserState
import re


@dp.message_handler(commands="user", state=None)
async def enter_info_user(message: types.Message):
    await message.answer("Ismingizni kiriting")
    await UserState.name.set()


@dp.message_handler(state=UserState.name)
async def add_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["name"] = message.text

    await message.answer("Yoshingizni kiriting")
    await UserState.next()


@dp.message_handler(lambda message: message.text.isdigit(), state=UserState.age)
async def add_age(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        try:
            data["age"] = message.text
            await message.answer("Telefon raqamingizni kiriting")
            await UserState.next()
        except:
            await message.answer("Butun son kiriting")


@dp.message_handler(state=UserState.phone_number)
async def add_phone_number(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        PHONE_REGEX = r"^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$"
        phone_number = re.match(PHONE_REGEX, message.text)
        if phone_number:
            data["phone_number"] = message.text
            await message.answer("Emailingizni kiriting")
            await UserState.next()
        else:
            await message.answer("Telefon raqam xato kiritildi")


@dp.message_handler(state=UserState.email)
async def add_email(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        EMAIL_REGEX = r'[^@ \t\r\n]+@[^@ \t\r\n]+\.[^@ \t\r\n]+'
        email = re.match(EMAIL_REGEX, message.text)
        if email:
            data["email"] = message.text
            await message.answer("Rasmingizni kiriting")
            await UserState.next()
        else:
            await message.answer("Email xato kiritildi")


@dp.message_handler(content_types="photo", state=UserState.photo)
async def add_photo(message: types.Message, state: FSMContext):
    photo_id = message.photo[-1].file_id
    async with state.proxy() as data:
        data["photo"] = photo_id
        await message.answer("Ma'lumotlaringiz saqlandi")
        await bot.send_photo(chat_id=message.from_user.id,
                             caption=f"Foydalanuvchini ismi: <b>{data['name']}</b>,\n"
                                f"Yoshi: <b>{data['age']}</b>,\n"
                                f"Telefon raqami: <b>{data['phone_number']}</b>,\n"
                                f"Emaili: <b>{data['email']}</b>",
                             photo=data['photo'])
        await state.finish()


