import sqlite3

from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

TOKEN = "8559846254:AAH7WnkqgRTE3HcrnB7qc15Gcgg9eJ5Wrdw"

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

# ПОДКЛЮЧЕНИЕ БАЗЫ ДАННЫХ
conn = sqlite3.connect("music_school.db")
cursor = conn.cursor()

# СОЗДАНИЕ ТАБЛИЦ

cursor.execute("""
CREATE TABLE IF NOT EXISTS teachers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS schedule (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    day TEXT,
    lesson TEXT,
    time TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS announcements (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    text TEXT
)
""")

conn.commit()

# ДОБАВЛЕНИЕ ДАННЫХ

cursor.execute("SELECT COUNT(*) FROM teachers")
if cursor.fetchone()[0] == 0:

    cursor.execute("INSERT INTO teachers (name) VALUES ('Иванова Е.А.')")
    cursor.execute("INSERT INTO teachers (name) VALUES ('Петров А.В.')")

cursor.execute("SELECT COUNT(*) FROM schedule")
if cursor.fetchone()[0] == 0:

    cursor.execute("""
    INSERT INTO schedule (day, lesson, time)
    VALUES ('Понедельник', 'Фортепиано', '15:00')
    """)

    cursor.execute("""
    INSERT INTO schedule (day, lesson, time)
    VALUES ('Понедельник', 'Вокал', '17:00')
    """)

    cursor.execute("""
    INSERT INTO schedule (day, lesson, time)
    VALUES ('Вторник', 'Скрипка', '14:00')
    """)

cursor.execute("SELECT COUNT(*) FROM announcements")
if cursor.fetchone()[0] == 0:

    cursor.execute("""
    INSERT INTO announcements (text)
    VALUES ('20 мая состоится отчетный концерт!')
    """)

conn.commit()

# КНОПКИ

main_menu = ReplyKeyboardMarkup(resize_keyboard=True)

btn1 = KeyboardButton("🎼 Расписание")
btn2 = KeyboardButton("👩‍🏫 Преподаватели")
btn3 = KeyboardButton("📢 Объявления")

main_menu.add(btn1)
main_menu.add(btn2)
main_menu.add(btn3)

# START

@dp.message_handler(commands=['start'])
async def start(message: types.Message):

    await message.answer(
        "🎵 Добро пожаловать в информационную систему музыкальной школы!\n\nВыберите нужный раздел:",
        reply_markup=main_menu
    )

# РАСПИСАНИЕ

@dp.message_handler(lambda message: message.text == "🎼 Расписание")
async def schedule(message: types.Message):

    cursor.execute("SELECT day, lesson, time FROM schedule")

    rows = cursor.fetchall()

    text = "🎼 Расписание занятий\n\n"

    for row in rows:

        text += (
            f"{row[0]}\n"
            f"• {row[1]} — {row[2]}\n\n"
        )

    await message.answer(text)

# ПРЕПОДАВАТЕЛИ

@dp.message_handler(lambda message: message.text == "👩‍🏫 Преподаватели")
async def teachers(message: types.Message):

    cursor.execute("SELECT name FROM teachers")

    rows = cursor.fetchall()

    text = "👩‍🏫 Преподаватели музыкальной школы\n\n"

    for row in rows:

        text += f"• {row[0]}\n"

    await message.answer(text)

# ОБЪЯВЛЕНИЯ

@dp.message_handler(lambda message: message.text == "📢 Объявления")
async def announcements(message: types.Message):

    cursor.execute("SELECT text FROM announcements")

    rows = cursor.fetchall()

    text = "📢 Объявления\n\n"

    for row in rows:

        text += f"• {row[0]}\n"

    await message.answer(text)

# ЗАПУСК БОТА

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
