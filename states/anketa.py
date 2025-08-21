from aiogram.fsm.state import State, StatesGroup

class Anketa(StatesGroup):
    name = State()
    age = State()
    city = State()
    photo = State()
    intents = State()
    confirm = State()
