from aiogram import types
from loader import dp, bot
import os
from utils.convert_to_pdf import convert_image_to_pdf


# pip install fpdf
# Rasm yuborilganda PDF-ga o'tkazadi
@dp.message_handler(content_types=types.ContentTypes.PHOTO)
async def convert_to_pdf(message: types.Message):
    # Rasmni yuklab olish
    file_id = message.photo[-1].file_id
    file = await bot.get_file(file_id)
    file_path = file.file_path

    # Rasmni yuklab olish
    file_extension = os.path.splitext(file_path)[1]
    image_path = f'input{file_extension}'
    await file.download(image_path)

    # PDF-ga o'tkazish
    pdf_path = 'output.pdf'
    convert_image_to_pdf(image_path, pdf_path)

    # PDF-ni foydalanuvchiga yuborish
    with open(pdf_path, 'rb') as pdf_file:
        await bot.send_document(message.from_user.id, pdf_file)
