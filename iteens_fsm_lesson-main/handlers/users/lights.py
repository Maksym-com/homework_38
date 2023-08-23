from aiogram import types

from loader import dp
from keyboards.default import lights_all, red_kb, yellow_kb, green_kb
from states import Lights


@dp.message_handler(commands='trafficlighton', state="*")
async def bot_traffic_light_on(message: types.Message):
    await Lights.StateOn.set()
    await message.answer("Ви увімкнули світлофор 🚦.\n"
                         "Тепер можете увімкнути будь-яке світло:",
                         reply_markup=lights_all)
    
@dp.message_handler(text="червоний", state=(Lights.StateGreen, Lights.StateOn))
async def bot_red_lights_on(message: types.Message):
    await Lights.StateRed.set()
    await message.answer("Ви увімкнули червоне світло 🔴\n"
                         "Тепер можете увімкнути жовте",
                         reply_markup=yellow_kb)


@dp.message_handler(text="жовтий", state=(Lights.StateRed, Lights.StateOn))
async def bot_yellow_light(message: types.Message):
    await Lights.StateYellow.set()
    await message.answer("Ви увімкнули жовте світло 🟡\n"
                         "Тепер можете увімкнути зелене",
                         reply_markup=green_kb)
    
@dp.message_handler(text="зелений", state=(Lights.StateYellow, Lights.StateOn))
async def bot_green_light(message: types.Message):
    await Lights.StateGreen.set()
    await message.answer("Ви увімкнули зелене світло 🟢\n"
                         "Тепер можете увімкнути червоне",
                         reply_markup=red_kb)
    
@dp.message_handler(commands="trafficlightsoff", state=Lights.all_states)
async def bot_light_off(message: types.Message):
    await dp.current_state.reset_state()
    await message.answer("Ви вимкнули світлофор\n"
                         "Для увімкнення натисніть команду /trafficlighton",
                         reply_markup=None)