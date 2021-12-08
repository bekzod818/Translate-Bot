from aiogram.dispatcher.filters.state import StatesGroup, State

class Translate(StatesGroup):
    lang = State()
    trans = State()
    audio = State()