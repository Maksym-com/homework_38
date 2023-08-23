from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

red = KeyboardButton(text="червоний")
yellow = KeyboardButton(text="жовтий")
green = KeyboardButton(text="зелений")

lights_all = ReplyKeyboardMarkup(resize_keyboard=True).row(red, yellow, green)
red_kb = ReplyKeyboardMarkup(resize_keyboard=True).row(red)
yellow_kb = ReplyKeyboardMarkup(resize_keyboard=True).row(yellow)
green_kb = ReplyKeyboardMarkup(resize_keyboard=True).row(green)
