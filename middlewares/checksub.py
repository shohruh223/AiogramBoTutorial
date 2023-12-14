import logging
from aiogram import types
from aiogram.dispatcher.handler import CancelHandler
from aiogram.dispatcher.middlewares import BaseMiddleware
from data.config import CHANNELS
from utils.misc import subscription
from loader import bot


class BigBrother(BaseMiddleware):
    async def on_pre_process_update(self, update: types.Update, data: dict):
        # agar message update bo'lsa userdan message ni olyapmiz
        if update.message:
            user = update.message.from_user.id
            if update.message.text in ['/start', '/help']:
                return
        elif update.callback_query:
            user = update.callback_query.from_user.id
            if update.callback_query.data == "check_subs":
                return
        else:
            return

        result = "Botdan foydalanish uchun quyidagi kanallarga obuna bo'ling:\n"
        final_status = True
        for channel in CHANNELS:
            # bu yerda status True qaytarsa kanalga obuna bo'lgan bo'ladi
            status = await subscription.check(user_id=user,
                                              channel=channel)
            final_status *= status
            channel = await bot.get_chat(channel)
            # agar kanalga obuna bo'lmagan bo'lsa quyigadagi linkni beramiz
            if not status:
                invite_link = await channel.export_invite_link()
                result += (f"👉 <a href='{invite_link}'>{channel.title}</a>\n")

        # agar foydalanuvchi qaysidir kanallarga obuna bo'lmagan bo'lsa
        if not final_status:
            await update.message.answer(result, disable_web_page_preview=True)
            # va bu komandani beramiz, bu komandani afzalligi shundaki agar qaysidir kanalga obuna
            # bo'lmagan bo'lsa message handler larga yetib bormaydi
            raise CancelHandler()
