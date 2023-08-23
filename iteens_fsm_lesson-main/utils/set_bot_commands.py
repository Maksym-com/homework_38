from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("start", "Запустити бота"),
            types.BotCommand("register", "Реєстрація"),
            types.BotCommand("view", "Переглянути інформацію про себе"),
            types.BotCommand("change_name", "Змінити ім'я"),
            types.BotCommand("change_email", "Змінити E-mail"),
            types.BotCommand("change_age", "Змінити вік"),
        ]
    )
