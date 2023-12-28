from aiogram import types
from aiogram.dispatcher import FSMContext
import re
from keyboards.default.user_keyboard import crud_button
from keyboards.inline.inline_user import edit_user_check
from loader import dp
from states.user import EditUserState
from utils.db_api.user import Database

db = Database()


@dp.message_handler(state=EditUserState.id)
async def edit_user(message: types.Message, state: FSMContext):
    try:
        user_id = int(message.text)
        user = db.get_user(id=user_id)

        if user:
            async with state.proxy() as data:
                data['id'] = message.text
            await message.answer_photo(photo=user[4],
                                       caption=f"Foydalanuvchining ismi : {user[1]}\n"
                                               f"Foydalanuvchining yoshi : {user[2]}\n"
                                               f"Foydalanuvchining telefon raqami : {user[3]}\n"
                                               f"\n",
                                       reply_markup=edit_user_check())
        else:
            await message.answer("Bu id raqamga tegishli fuqaro topilmadi . ")
    except:
        await message.answer("Id raqam bo'lsin")


@dp.callback_query_handler(state=EditUserState)
async def call_back(callback: types.CallbackQuery, state: FSMContext):
    if callback.data == "edit_fullname":
        await callback.message.answer("Ismni yangilang ")
        await EditUserState.fullname.set()

    elif callback.data == "edit_age":
        await callback.message.answer("Yoshni yangilang ")
        await EditUserState.age.set()

    elif callback.data == "edit_phone_number":
        await callback.message.answer("Telefon nomerni yangilang ")
        await EditUserState.phone_number.set()

    elif callback.data == "edit_photo":
        await callback.message.answer("Rasmni yuklang ")
        await EditUserState.photo.set()

    elif callback.data == 'back_to_start':
        await callback.message.answer('Tanlang', reply_markup=crud_button())
        await state.finish()


@dp.message_handler(state=EditUserState.fullname)
async def edit_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['fullname'] = message.text
        update_id = data["id"]

        db.update_user_fullname(id=update_id, fullname=data['fullname'])
    user_id = int(data['id'])
    user = db.get_user(id=user_id)
    await message.answer_photo(photo=user[4],
                               caption=f"Foydalanuvchining ismi : {user[1]}\n"
                                       f"Foydalanuvchining yoshi : {user[2]}\n"
                                       f"Foydalanuvchining telefon raqami : {user[3]}\n"
                                       f"\n",
                               reply_markup=edit_user_check())


@dp.message_handler(state=EditUserState.age)
async def edit_age(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        try:
            data['age'] = int(message.text)
            db.update_user_age(id=data['id'],
                               age=data['age'])
            user = db.get_user(data['id'])
            await message.answer_photo(photo=user[4],
                                       caption=f"Foydalanuvchining ismi : {user[1]}\n"
                                               f"Foydalanuvchining yoshi : {user[2]}\n"
                                               f"Foydalanuvchining telefon raqami : {user[3]}\n"
                                               f"\n",
                                       reply_markup=edit_user_check())
        except:
            await message.answer("Yosh butun sonda kiritilmadi !")


@dp.message_handler(state=EditUserState.phone_number)
async def edit_phone_number(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        PHONE_REGEX = r"^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$"
        phone = re.match(PHONE_REGEX, message.text)
        if phone:
            data['phone_number'] = message.text
            db.update_user_phone(id=data['id'],
                                 phone_number=data['phone_number'])
            user = db.get_user(data['id'])
            await message.answer_photo(photo=user[4],
                                       caption=f"Foydalanuvchining ismi : {user[1]}\n"
                                               f"Foydalanuvchining yoshi : {user[2]}\n"
                                               f"Foydalanuvchining telefon raqami : {user[3]}\n"
                                               f"\n",
                                       reply_markup=edit_user_check())

        else:
            await message.answer("Telefon nomer xato kiritildi !")


@dp.message_handler(lambda message: not message.photo, state=EditUserState.photo)
async def check_photo(message: types.Message):
    await message.answer("Bu rasm formatida emas")


@dp.message_handler(state=EditUserState.photo, content_types=['photo'])
async def add_photo(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['photo'] = message.photo[0].file_id

        db.update_user_photo(id=data['id'],
                             photo=data['photo'])
        user = db.get_user(data['id'])
        await message.answer_photo(photo=user[4],
                                   caption=f"Foydalanuvchining ismi : {user[1]}\n"
                                           f"Foydalanuvchining yoshi : {user[2]}\n"
                                           f"Foydalanuvchining telefon raqami : {user[3]}\n"
                                           f"\n",
                                   reply_markup=edit_user_check())
