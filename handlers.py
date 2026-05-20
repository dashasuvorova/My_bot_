from aiogram import types
from aiogram.dispatcher import Dispatcher

from keyboards import main_keyboard
from database import cursor

def register_handlers(dp: Dispatcher):

    # START

    @dp.message_handler(commands=['start'])
    async def start(message: types.Message):

        text = (
            "🎵 Добро пожаловать в информационную систему музыкальной школы!\n\n"
            "Основные команды:\n"
            "/start — запуск бота\n"
            "/schedule — расписание\n"
            "/teachers — преподаватели\n"
            "/admin — панель администратора\n"
            "/help — помощь"
            
        )

        await message.answer(
            text,
            reply_markup=main_keyboard
        )

    # HELP

    @dp.message_handler(commands=['help'])
    async def help_command(message: types.Message):

        text = (
            "📌 Команды бота:\n\n"
            "/start — запуск бота\n"
            "/schedule — расписание\n"
            "/teachers — преподаватели\n"
            "/subjects — дисциплины\n"
            "/help — помощь"
        )

        await message.answer(text)

    # РАСПИСАНИЕ КОМАНДА

    @dp.message_handler(commands=['schedule'])
    async def schedule_command(message: types.Message):

        cursor.execute(
            "SELECT day, lesson, time FROM schedule"
        )

        rows = cursor.fetchall()

        text = "🎼 Расписание занятий\n\n"

        for row in rows:

            text += (
                f"{row[0]}\n"
                f"• {row[1]} — {row[2]}\n\n"
            )

        await message.answer(text)

    # ПРЕПОДАВАТЕЛИ КОМАНДА

    @dp.message_handler(commands=['teachers'])
    async def teachers_command(message: types.Message):

        cursor.execute(
            "SELECT name FROM teachers"
        )

        rows = cursor.fetchall()

        text = "👩‍🏫 Преподаватели\n\n"

        for row in rows:

            text += f"• {row[0]}\n"

        await message.answer(text)

    # ДИСЦИПЛИНЫ

    @dp.message_handler(commands=['subjects'])
    async def subjects_command(message: types.Message):

        cursor.execute(
            "SELECT name FROM subjects"
        )

        rows = cursor.fetchall()

        text = "🎵 Музыкальные дисциплины\n\n"

        for row in rows:

            text += f"• {row[0]}\n"

        await message.answer(text)

    # КНОПКА РАСПИСАНИЕ

    @dp.message_handler(lambda message: message.text == "🎼 Расписание")
    async def schedule_button(message: types.Message):

        cursor.execute(
            "SELECT day, lesson, time FROM schedule"
        )

        rows = cursor.fetchall()

        text = "🎼 Расписание занятий\n\n"

        for row in rows:

            text += (
                f"{row[0]}\n"
                f"• {row[1]} — {row[2]}\n\n"
            )

        await message.answer(text)

    # КНОПКА ПРЕПОДАВАТЕЛИ

    @dp.message_handler(lambda message: message.text == "👩‍🏫 Преподаватели")
    async def teachers_button(message: types.Message):

        cursor.execute(
            "SELECT name FROM teachers"
        )

        rows = cursor.fetchall()

        text = "👩‍🏫 Преподаватели\n\n"

        for row in rows:

            text += f"• {row[0]}\n"

        await message.answer(text)

    # КНОПКА ДИСЦИПЛИНЫ

    @dp.message_handler(lambda message: message.text == "🎵 Дисциплины")
    async def subjects_button(message: types.Message):

        cursor.execute(
            "SELECT name FROM subjects"
        )

        rows = cursor.fetchall()

        text = "🎵 Музыкальные дисциплины\n\n"

        for row in rows:

            text += f"• {row[0]}\n"

        await message.answer(text)

    # КНОПКА ОБЪЯВЛЕНИЯ

    @dp.message_handler(lambda message: message.text == "📢 Объявления")
    async def announcements(message: types.Message):

        cursor.execute(
            "SELECT text FROM announcements"
        )

        rows = cursor.fetchall()

        text = "📢 Объявления\n\n"

        for row in rows:

            text += f"• {row[0]}\n"

        await message.answer(text)

    # КОНТАКТЫ

    @dp.message_handler(lambda message: message.text == "☎️ Контакты")
    async def contacts(message: types.Message):

        text = (
            "☎️ Контакты музыкальной школы\n\n"
            "📍 Адрес: ул. Центральная, 15\n"
            "📞 Телефон: +7 (900) 123-45-67\n"
            "✉️ Email: music_school@mail.ru"
        )

        await message.answer(text)
    # РАСПИСАНИЕ ПО ДНЯМ

    @dp.message_handler(
        lambda message: message.text in [
            "Понедельник",
            "Вторник",
            "Среда",
            "Четверг",
            "Пятница"
        ]
    )
    async def weekday_schedule(message: types.Message):

        day = message.text

        cursor.execute(
            "SELECT lesson, time FROM schedule WHERE day=?",
            (day,)
        )

        rows = cursor.fetchall()

        text = f"📅 Расписание на {day}\n\n"

        if rows:

            for row in rows:

                text += (
                    f"• {row[0]} — {row[1]}\n"
                )

        else:

            text += "Занятий нет."

        await message.answer(text)
