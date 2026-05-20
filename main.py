from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

TOKEN = "8559846254:AAH7WnkqgRTE3HcrnB7qc15Gcgg9eJ5Wrdw"

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

main_menu = ReplyKeyboardMarkup(resize_keyboard=True)

btn1 = KeyboardButton("Расписание")
btn2 = KeyboardButton("Преподаватели")
btn3 = KeyboardButton("Объявления")

main_menu.add(btn1)
main_menu.add(btn2)
main_menu.add(btn3)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):

    await message.answer(
        "🎵 Добро пожаловать в информационную систему музыкальной школы!\n\nВыберите нужный раздел:",
        reply_markup=main_menu
    )

@dp.message_handler(lambda message: message.text == "Расписание")
async def schedule(message: types.Message):

    text = (
        "🎼 Расписание занятий\n\n"
        "Понедельник\n"
        "• Фортепиано — 15:00\n"
        "• Вокал — 17:00\n\n"
        "Вторник\n"
        "• Скрипка — 14:00\n"
        "• Сольфеджио — 16:00\n\n"
        "Среда\n"
        "• Гитара — 15:30\n"
    )

    await message.answer(text)

@dp.message_handler(lambda message: message.text == "Преподаватели")
async def teachers(message: types.Message):

    await message.answer(
        "👩‍🏫 Преподаватели:\n\nИванова Е.А.\nПетров А.В."
    )

@dp.message_handler(lambda message: message.text == "Объявления")
async def news(message: types.Message):

    await message.answer(
        "📢 20 мая состоится отчетный концерт!"
    )

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
