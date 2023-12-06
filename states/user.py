from aiogram.dispatcher.filters.state import StatesGroup, State


class AddUserState(StatesGroup):
    fullname = State()
    age = State()
    phone_number = State()
    photo = State()


class AllUserState(StatesGroup):
    all = State()


class GetUserState(StatesGroup):
    get = State()