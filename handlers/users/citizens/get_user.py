from aiogram import types
from aiogram.dispatcher import FSMContext

from keyboards.default.user_keyboard import cancel_button
from keyboards.inline.inline_user import show_users, edit_user_check, edit_users
from loader import dp
from states.user import GetUserState, EditUserState
from utils.db_api.user import Database

db = Database()


# @dp.message_handler(state=GetUserState.get)
# async def get_user(message: types.Message, state: FSMContext):
#     user_id = int(message.text.strip())
#     user = db.get_user(id=user_id)
#     if user:
#         await message.answer_photo(photo=user[4],
#                                    caption=f"Foydalanuvchini ismi {user[1]},\n"
#                                            f"yoshi {user[2]}da,\n"
#                                            f"telefon raqami {user[3]}")
#     else:
#         await message.answer("Bunaqa ID tegishli foydalanuvchi yo'q")
#
#     await state.finish()


@dp.callback_query_handler()
async def call(callback: types.CallbackQuery):
    for user in db.all_user():
        if callback.data == f"ID:{user[0]}":
            user = db.get_user(id=user[0])
            await callback.message.answer_photo(photo=user[4],
                                                caption=user[1],
                                                reply_markup=edit_users())
    if callback.data == f"edit user":
        await callback.message.answer(text="Foydalanuvchini ID sini kiriting",
                                      reply_markup=cancel_button())
        await EditUserState.id.set()
    if callback.data == "back":
        await callback.message.answer(text="ortga",
                                      reply_markup=show_users())




