from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp
from keyboards.default import get_phone_kb


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Для користування ботом надішліть ваш контакт", reply_markup=get_phone_kb)
