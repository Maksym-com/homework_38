from aiogram.dispatcher.filters.state import StatesGroup, State


class Lights(StatesGroup):
    StateOn = State()
    StateRed = State()
    StateYellow = State()
    StateGreen = State()
    StateOff = State()