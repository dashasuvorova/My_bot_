from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher import Dispatcher
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from database import cursor, conn
from states import AddAnnouncementState

# ID администратора

ADMINS = [419116810]

# АДМИН КЛАВИАТУРА

admin_keyboard = ReplyKeyboardMarkup(
    resize_keyboard=True
)

btn1 = KeyboardButton("➕ Добавить объявление")
btn2 = KeyboardButton("📢 Все объявления")

admin_keyboard.add(btn1)
admin_keyboard.add(btn2)

def register_admin_handlers(dp: Dispatcher):

    # ПРОВЕРКА АДМИНА

    def is_admin(user_id):

        return user_id in ADMINS

    # КОМАНДА ADMIN

    @dp.message_handler(commands=['admin'])
    async def admin_panel(message: types.Message):

        if not is_admin(message.from_user.id):

            await message.answer(
                "❌ У вас нет доступа."
            )

            return

        await message.answer(
            "⚙️ Панель администратора",
            reply_markup=admin_keyboard
        )

    # КНОПКА ДОБАВИТЬ ОБЪЯВЛЕНИЕ

   @dp.message_handler(
    lambda message: message.text == "➕ Добавить объявление",
    state="*"
)
    async def add_announcement(message: types.Message):

        if not is_admin(message.from_user.id):

            return

        await message.answer(
            "Введите текст объявления:"
        )

        await AddAnnouncementState.waiting_for_text.set()

    # СОХРАНЕНИЕ ОБЪЯВЛЕНИЯ

    @dp.message_handler(
        state=AddAnnouncementState.waiting_for_text
    )
    async def save_announcement(
        message: types.Message,
        state: FSMContext
    ):

        cursor.execute(
            "INSERT INTO announcements (text) VALUES (?)",
            (message.text,)
        )

        conn.commit()

        await message.answer(
            "✅ Объявление добавлено."
        )

        await state.finish()

    # ВСЕ ОБЪЯВЛЕНИЯ

    @dp.message_handler(
    lambda message: message.text == "📢 Все объявления",
    state="*"
)
    async def show_announcements(message: types.Message):

        cursor.execute(
            "SELECT text FROM announcements"
        )

        rows = cursor.fetchall()

        text = "📢 Все объявления\n\n"

        for row in rows:

            text += f"• {row[0]}\n"

        await message.answer(text)
