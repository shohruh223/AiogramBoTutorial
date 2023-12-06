from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from keyboards.inline.inline_user import show_users
from loader import dp
from states.user import AllUserState
from utils.db_api.user import Database


db = Database()


# @dp.message_handler(Text(equals="Yes"), state=AllUserState.all)
# async def all_user(message: types.Message, state: FSMContext):
#     users = db.all_user()
#     for user in users:
#         await message.answer_photo(photo=user[4],
#                                    caption=f"Foydalanuvchini ismi {user[1]},\n"
#                                            f"yoshi {user[2]}da,\n"
#                                            f"telefon raqami {user[3]}",
#                                    reply_markup=cancel_button())
#     await state.finish()


@dp.message_handler(Text(equals="Yes"), state=AllUserState.all)
async def all_user(message: types.Message, state: FSMContext):
    await message.answer("ok",
                         reply_markup=show_users())
    await state.finish()