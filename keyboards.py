from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_keyboard = ReplyKeyboardMarkup(
    resize_keyboard=True
)

btn1 = KeyboardButton("🎼 Расписание")
btn2 = KeyboardButton("👩‍🏫 Преподаватели")
btn3 = KeyboardButton("🎵 Дисциплины")
btn4 = KeyboardButton("📢 Объявления")
btn5 = KeyboardButton("☎️ Контакты")

main_keyboard.add(btn1)
main_keyboard.add(btn2)
main_keyboard.add(btn3)
main_keyboard.add(btn4)
main_keyboard.add(btn5)
