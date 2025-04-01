from aiogram.dispatcher.filters.state import State, StatesGroup

class Lang(StatesGroup):
    choose_lang = State()