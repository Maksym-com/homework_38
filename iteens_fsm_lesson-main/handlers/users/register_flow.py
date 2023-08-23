from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.dispatcher.filters.state import StatesGroup, State
from loader import dp
from states.flow import Flow

# register
@dp.message_handler(commands='register')
async def register_start(message: types.Message, state:FSMContext):
        await message.answer(text="Введіть ваше ім'я")
        await Flow.Name.set()

@dp.message_handler(state=Flow.Name)
async def register_name(message: types.Message, state:FSMContext):
    username = message.text
    async with state.proxy() as data:
        data["name"] = username
    await message.answer("Введіть ваш Email")
    await Flow.Email.set()

@dp.message_handler(state=Flow.Email)
async def register_email(message: types.Message, state:FSMContext):
    user_email = message.text
    async with state.proxy() as data:
        data["email"] = user_email
    await message.answer(text="Введіть ваш вік")
    await Flow.Age.set()

@dp.message_handler(state=Flow.Age)
async def register_age(message: types.Message, state:FSMContext):
    user_age = message.text
    async with state.proxy() as data:
        data["age"] = user_age
    await Flow.Registred.set()
    await message.answer(text="Реєстрацію пройдено!")

# view
@dp.message_handler(commands="view", state=Flow.Registred)
async def view_workers(message: types.Message, state: FSMContext):
    # await message.answer(text=f"{'Name':<15}{'Salary (USD)':<20}{'Position':20}{'Started to work':>20}\n\n")
    async with state.proxy() as data:
        await message.answer(text=f'''<b>Name: </b><u>{data['name']}</u>\n
<b>Email: </b>{data["email"]}
<b>Age: </b>{data["age"]}
''', parse_mode='html')

# change_name
@dp.message_handler(commands="change_name", state=Flow.Registred)
async def change_name_1(message: types.Message, state:FSMContext):
    async with state.proxy() as data:
        await message.answer(text=f"На даний момент ваше ім'я - {data['name']}.")
    await message.answer(text="Введіть нове ім'я")
    await Flow.ChangeName.set()

@dp.message_handler(state=Flow.ChangeName)
async def change_name_2(message: types.Message, state:FSMContext):
    new_name = message.text
    async with state.proxy() as data:
        data["name"] = new_name 
    await Flow.Registred.set()
    await message.answer(text=f"Успішно змінено! Тепер ваше ім'я - {new_name}.")

# change_email
@dp.message_handler(commands="change_email", state=Flow.Registred)
async def change_email_1(message: types.Message, state:FSMContext):
    async with state.proxy() as data:
        await message.answer(text=f"На даний момент ваш Email - {data['email']}.")
    await message.answer(text="Введіть новий Email")
    await Flow.ChangeEmail.set()

@dp.message_handler(state=Flow.ChangeEmail)
async def change_email_2(message: types.Message, state:FSMContext):
    new_email = message.text
    async with state.proxy() as data:
        data["email"] = new_email
    await Flow.Registred.set()
    await message.answer(text=f"Успішно змінено! Тепер ваш email - {new_email}.")

# change_age
@dp.message_handler(commands="change_age", state=Flow.Registred)
async def change_age_1(message: types.Message, state:FSMContext):
    async with state.proxy() as data:
        await message.answer(text=f"На даний момент ваш вік - {data['age']}.")
    await message.answer(text="Введіть новий вік")
    await Flow.ChangeAge.set()

@dp.message_handler(state=Flow.ChangeAge)
async def change_age_2(message: types.Message, state:FSMContext):
    new_age = message.text
    async with state.proxy() as data:
        data["age"] = new_age
    await Flow.Registred.set()
    await message.answer(text=f"Успішно змінено! Тепер ваш вік - {new_age}.")

# Якщо користувач вже зареєстрований - тоді він не зможе зареєструватись знову
@dp.message_handler(commands='register', state=Flow.Registred)
async def register_finish(message: types.Message):
        await message.answer(text="Ви вже зареєстровані")



