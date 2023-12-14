import logging
from aiogram import types
from data.config import CHANNELS
from keyboards.inline.subscriptions import check_button
from loader import bot, dp
from utils.misc import subscription


@dp.message_handler(commands=['start'])
async def show_channels(message: types.Message):
    # string formatda bo'sh variable yaratdik
    channels_format = str()
    # har bir kanalni for da aylanamiz
    for channel in CHANNELS:
        chat = await bot.get_chat(channel)
        # kanaldagi obuna bo'ladigan linkni olyapmiz
        invite_link = await chat.export_invite_link()
        # logging.info(invite_link)
        # kanalni linkini chiroyli formatda chiqarib beramiz
        channels_format += f"👉 <a href='{invite_link}'>{chat.title}</a>\n"

    await message.answer(f"Quyidagi kanallarga obuna bo'ling: \n"
                         f"{channels_format}",
                         reply_markup=check_button(),
                         disable_web_page_preview=True)


@dp.callback_query_handler(text="check_subs")
async def checker(callback: types.CallbackQuery):
    await callback.answer()
    result = str()
    # endi biz har bir kanalda user obuna bo'lganmi yo'qmi shuni tekshiramiz
    for channel in CHANNELS:
        # endi user obuna bo'lganini check qilyapmiz
        status = await subscription.check(user_id=callback.from_user.id,
                                          channel=channel)
        # kanalni get qilib oldik
        channel = await bot.get_chat(channel)
        # agarda kanalga obuna bo'lsa
        if status:
            result += f"✅<b>{channel.title}</b> kanaliga obuna bo'lgansiz!\n\n"
        else:
            invite_link = await channel.export_invite_link()
            result += (f"❌<b>{channel.title}</b> kanaliga obuna bo'lmagansiz. "
                       f"<a href='{invite_link}'>Obuna bo'ling</a>\n\n")

    await callback.message.answer(result, disable_web_page_preview=True)