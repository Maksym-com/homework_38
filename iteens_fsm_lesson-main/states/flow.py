from aiogram.dispatcher.filters.state import StatesGroup, State

class Flow(StatesGroup):
    Registred = State()
    RegisterOn = State()
    Name = State()
    Name1 = State()
    ChangeName = State()
    Email = State()
    ChangeEmail = State()
    Age = State()
    ChangeAge = State()