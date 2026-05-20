from aiogram import Bot, Dispatcher, executor

from config import TOKEN

import database

from handlers import register_handlers

bot = Bot(token=TOKEN)

dp = Dispatcher(bot)

register_handlers(dp)

if __name__ == "__main__":

    executor.start_polling(
        dp,
        skip_updates=True
    )
