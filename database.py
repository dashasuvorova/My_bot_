import sqlite3

conn = sqlite3.connect(
    "music_school.db",
    check_same_thread=False
)
cursor = conn.cursor()

# ТАБЛИЦА ПРЕПОДАВАТЕЛЕЙ

cursor.execute("""
CREATE TABLE IF NOT EXISTS teachers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT
)
""")

# ТАБЛИЦА РАСПИСАНИЯ

cursor.execute("""
CREATE TABLE IF NOT EXISTS schedule (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    day TEXT,
    lesson TEXT,
    time TEXT
)
""")

# ТАБЛИЦА ОБЪЯВЛЕНИЙ

cursor.execute("""
CREATE TABLE IF NOT EXISTS announcements (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    text TEXT
)
""")

# ТАБЛИЦА ДИСЦИПЛИН

cursor.execute("""
CREATE TABLE IF NOT EXISTS subjects (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT
)
""")

conn.commit()

# ДОБАВЛЕНИЕ ДАННЫХ

cursor.execute("SELECT COUNT(*) FROM teachers")

if cursor.fetchone()[0] == 0:

    teachers = [
        ("Иванова Е.А.",),
        ("Петров А.В.",),
        ("Смирнова О.И.",)
    ]

    cursor.executemany(
        "INSERT INTO teachers (name) VALUES (?)",
        teachers
    )

cursor.execute("SELECT COUNT(*) FROM subjects")

if cursor.fetchone()[0] == 0:

    subjects = [
        ("Фортепиано",),
        ("Вокал",),
        ("Скрипка",),
        ("Гитара",),
        ("Сольфеджио",)
    ]

    cursor.executemany(
        "INSERT INTO subjects (name) VALUES (?)",
        subjects
    )

cursor.execute("SELECT COUNT(*) FROM schedule")

if cursor.fetchone()[0] == 0:

    lessons = [
        ("Понедельник", "Фортепиано", "15:00"),
        ("Понедельник", "Вокал", "17:00"),
        ("Вторник", "Скрипка", "14:00"),
        ("Среда", "Гитара", "16:00"),
        ("Четверг", "Вокал", "12:00"),
        ("Четверг", "Скрипка", "14:00"),
        ("Пятница", "Фортепиано", "15:00")
    ]

    cursor.executemany(
        "INSERT INTO schedule (day, lesson, time) VALUES (?, ?, ?)",
        lessons
    )

cursor.execute("SELECT COUNT(*) FROM announcements")

if cursor.fetchone()[0] == 0:

    announcements = [
        ("20 мая состоится отчетный концерт!",),
        ("25 мая пройдет конкурс пианистов.",)
    ]

    cursor.executemany(
        "INSERT INTO announcements (text) VALUES (?)",
        announcements
    )

conn.commit()
