from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.types import ReplyKeyboardRemove
from keyboards.default.user_keyboard import cancel_button, user_button
from loader import dp
from states.user import AddUserState


@dp.message_handler(Text(equals="✅ Ro'yxatdan o'tish"))
async def register(message: types.Message):
    await message.answer(text="Ismingizni kiriting",
                         reply_markup=cancel_button())
    await AddUserState.fullname.set()


@dp.message_handler(Text(equals="🔙 orqaga qaytish"), state="*")
async def cancel(message: types.Message, state: FSMContext):
    await message.answer(text="Bekor qilindi",
                         reply_markup=user_button())
    await state.finish()