from aiogram.dispatcher.filters.state import StatesGroup, State


class LevelState(StatesGroup):
    level = State()
    answer = State()
