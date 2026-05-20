import sqlite3

DB_NAME = "music_school_bot.db"

def init_db():
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        # Таблица учеников
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS students (
                user_id INTEGER PRIMARY KEY AUTOINCREMENT,
                telegram_id INTEGER UNIQUE,
                full_name TEXT,
                group_name TEXT,
                instrument TEXT
            )
        ''')
        # Таблица преподавателей
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS teachers (
                teacher_id INTEGER PRIMARY KEY AUTOINCREMENT,
                full_name TEXT,
                specialization TEXT,
                telegram_id INTEGER UNIQUE
            )
        ''')
        # Таблица расписания
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS schedule (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                group_name TEXT,
                teacher_id INTEGER,
                day_of_week TEXT,
                lesson_number INTEGER,
                subject TEXT,
                room TEXT
            )
        ''')
        # Таблица домашних заданий
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS homework (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                student_id INTEGER,
                subject TEXT,
                task_text TEXT,
                due_date TEXT,
                is_done INTEGER DEFAULT 0
            )
        ''')
        # Таблица администраторов
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS admins (
                admin_id INTEGER PRIMARY KEY AUTOINCREMENT,
                telegram_id INTEGER UNIQUE,
                teacher_id INTEGER
            )
        ''')
        conn.commit()
