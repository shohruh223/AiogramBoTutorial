from aiogram.dispatcher.filters.state import StatesGroup, State


class Music(StatesGroup):
    link = State()


class Video(StatesGroup):
    link = State()