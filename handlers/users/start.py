from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.level_keyboard import level_button
from loader import dp
from states.level import LevelState


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Salom, {message.from_user.full_name}!",
                         reply_markup=level_button())
    await message.answer_photo("https://telegra.ph/file/8b13919c076e881fde66b.png",
                               caption=f"Hush kelibsiz {message.from_user.first_name}"
                                       f" bilag'on \nsizga bir nechta savolar berib "
                                       f"bilimingizni tekshirib beramiz !")
    await LevelState.level.set()


