# START

@dp.message_handler(commands=['start'])
async def start(message: types.Message):

    await message.answer(
        "🎵 Добро пожаловать в информационную систему музыкальной школы!\n\n"
        "Доступные команды:\n"
        "/schedule — расписание\n"
        "/teachers — преподаватели\n"
        "/help — справка",
        reply_markup=main_menu
    )

# HELP

@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):

    text = (
        "📌 Справка по командам:\n\n"
        "/start — запуск бота\n"
        "/schedule — просмотр расписания\n"
        "/teachers — список преподавателей\n"
        "/help — справка"
    )

    await message.answer(text)

# SCHEDULE

@dp.message_handler(commands=['schedule'])
async def schedule_command(message: types.Message):

    cursor.execute("SELECT day, lesson, time FROM schedule")

    rows = cursor.fetchall()

    text = "🎼 Расписание занятий\n\n"

    for row in rows:

        text += (
            f"{row[0]}\n"
            f"• {row[1]} — {row[2]}\n\n"
        )

    await message.answer(text)

# TEACHERS

@dp.message_handler(commands=['teachers'])
async def teachers_command(message: types.Message):

    cursor.execute("SELECT name FROM teachers")

    rows = cursor.fetchall()

    text = "👩‍🏫 Преподаватели музыкальной школы\n\n"

    for row in rows:

        text += f"• {row[0]}\n"

    await message.answer(text)

# КНОПКА РАСПИСАНИЕ

@dp.message_handler(lambda message: message.text == "🎼 Расписание")
async def schedule_button(message: types.Message):

    cursor.execute("SELECT day, lesson, time FROM schedule")

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

    cursor.execute("SELECT name FROM teachers")

    rows = cursor.fetchall()

    text = "👩‍🏫 Преподаватели музыкальной школы\n\n"

    for row in rows:

        text += f"• {row[0]}\n"

    await message.answer(text)

# КНОПКА ОБЪЯВЛЕНИЯ

@dp.message_handler(lambda message: message.text == "📢 Объявления")
async def announcements(message: types.Message):

    cursor.execute("SELECT text FROM announcements")

    rows = cursor.fetchall()

    text = "📢 Объявления\n\n"

    for row in rows:

        text += f"• {row[0]}\n"

    await message.answer(text)
