from aiogram import types
from aiogram.dispatcher import FSMContext
from loader import dp
from states.user import GetUserState
from utils.db_api.user import Database

db = Database()


@dp.callback_query_handler()
async def call_edit(callback: types.CallbackQuery):
    for user in db.all_user():
        if callback.data == f"edit:{user[0]}":
            user = db.get_user(id=user[0])
            await callback.message.answer_photo(photo=user[4],
                                                caption=user[1])