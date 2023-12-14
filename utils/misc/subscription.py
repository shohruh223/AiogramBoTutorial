from typing import Union
from aiogram import Bot


async def check(user_id, channel: Union[int, str]):
    # botimizni chaqirib oldik
    bot = Bot.get_current()
    # foydalanuvchini id si va kanalning username yoki id sini get qilib oldik
    member = await bot.get_chat_member(user_id=user_id, chat_id=channel)
    # va bu yerda esa o'sha foydalanuvchi kanalga obuna bo'lganmi yo'qmi
    return member.is_chat_member()