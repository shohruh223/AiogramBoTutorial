from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from keyboards.default.user_keyboard import cancel_button, user_button, crud_button, is_and_cancel_button
from loader import dp
from states.user import AddUserState, AllUserState, GetUserState, EditUserState, DeleteUserState


# @dp.message_handler(Text(equals="✅ Ro'yxatdan o'tish"))
# async def register(message: types.Message):
#     await message.answer(text="Ismingizni kiriting",
#                          reply_markup=cancel_button())
#     await AddUserState.fullname.set()


@dp.message_handler(Text(equals="User"))
async def register(message: types.Message):
    await message.answer(text="Foydalanuvchilar haqida",
                         reply_markup=crud_button())


@dp.message_handler(Text(equals="Add user"))
async def register_user(message: types.Message):
    await message.answer(text="Ro'yhatdan o'tish",
                         reply_markup=cancel_button())
    await message.answer(text="Ismingizni kiriting", )
    await AddUserState.fullname.set()


@dp.message_handler(Text(equals="View users"))
async def view_user(message: types.Message):
    await message.answer(text="Hamma foydalanuvchilarni ko'rinishini tasdiqlaysizmi ?",
                         reply_markup=is_and_cancel_button())
    await AllUserState.all.set()


@dp.message_handler(Text(equals="Get user"))
async def view_user(message: types.Message):
    await message.answer(text="Foydalanuvchini ID sini kiriting",
                         reply_markup=cancel_button())
    await GetUserState.get.set()


@dp.message_handler(Text(equals="Edit user"))
async def edit_user(message: types.Message):
    await message.answer(text="Foydalanuvchini ID sini kiriting",
                         reply_markup=cancel_button())
    await EditUserState.id.set()


@dp.message_handler(Text(equals="Delete user"))
async def delete_user(message: types.Message):
    await message.answer(text="Foydalanuvchini ID sini kiriting",
                         reply_markup=cancel_button())
    await DeleteUserState.id.set()


@dp.message_handler(Text(equals="🔙 orqaga qaytish"), state="*")
async def cancel(message: types.Message, state: FSMContext):
    await message.answer(text="Bekor qilindi",
                         reply_markup=user_button())
    await state.finish()
