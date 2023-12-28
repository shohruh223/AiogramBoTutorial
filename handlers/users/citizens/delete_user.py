from aiogram import types
from aiogram.dispatcher import FSMContext
from loader import dp
from states.user import DeleteUserState
from utils.db_api.user import Database

db = Database()


@dp.message_handler(state=DeleteUserState.id)
async def delete_user(message: types.Message, state: FSMContext):
    try:
        user_id = int(message.text)
        user = db.get_user(user_id)
        if user:
            db.delete_user(user_id)
            await message.answer("Bu fuqaro o'chirildi")
            await state.finish()
        else:
            await message.answer("Bu id ga tegishli fuqaro topilmadi ")
    except:
        await message.answer("Id raqam bo'lsin")
