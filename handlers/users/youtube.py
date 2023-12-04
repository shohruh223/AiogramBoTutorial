from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from loader import dp
from io import BytesIO
from pytube import YouTube
from states.yt import Music, Video


@dp.message_handler(Text(startswith="https"), state=Music.link)
async def get_audio(message: types.Message, state: FSMContext):
    # BytesIO obyekti yaratiladi, bu orqali audio faylini yuklab olish uchun xotira bo'sh joy yaratiladi
    buffer = BytesIO()
    # Foydalanuvchi tomonidan jo'natilgan YouTube video havolasidan obyekt yaratiladi
    url = YouTube(url=message.text)
    # Agar video yuklab olinishi mumkin bo'lsa
    if url.check_availability() is None:
        # Eng yaxshi sifatli audio stream tanlanadi
        audio = url.streams.get_audio_only()
        # Audio fayli xotiraga yuklanadi
        audio.stream_to_buffer(buffer=buffer)
        buffer.seek(0)
        filename = url.title
        await message.answer_audio(audio=buffer,
                                   caption=filename)
        await state.finish()
    else:
        await message.answer("Xatolik")


@dp.message_handler(Text(startswith="https"), state=Video.link)
async def get_video(message: types.Message, state: FSMContext):
    # BytesIO obyekti yaratiladi, bu orqali video faylini yuklab olish uchun xotira bo'sh joy yaratiladi
    buffer = BytesIO()
    # Foydalanuvchi tomonidan jo'natilgan YouTube video havolasidan obyekt yaratiladi
    url = YouTube(url=message.text)
    # Agar video yuklab olinishi mumkin bo'lsa
    if url.check_availability() is None:
        # Eng yaxshi sifatli video stream tanlanadi
        video = url.streams.get_highest_resolution()
        # Video fayli xotiraga yuklanadi
        video.stream_to_buffer(buffer=buffer)
        buffer.seek(0)
        filename = url.title
        await message.answer_video(video=buffer,
                                   caption=filename)
        await state.finish()
    else:
        await message.answer("Video yuklab olinmadi yoki xato ro'y berdi.")