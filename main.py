from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from config import TOKEN

import database

from handlers import register_handlers
from admin import register_admin_handlers

bot = Bot(token=TOKEN)

storage = MemoryStorage()

dp = Dispatcher(
    bot,
    storage=storage
)

register_handlers(dp)

register_admin_handlers(dp)

if __name__ == "__main__":

    executor.start_polling(
        dp,
        skip_updates=True
    )
