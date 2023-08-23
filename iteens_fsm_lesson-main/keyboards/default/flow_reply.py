from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

get_phone_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Share your phone number", request_contact=True),]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)