from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_keyboard = ReplyKeyboardMarkup(
    resize_keyboard=True
)

btn1 = KeyboardButton("📅 Расписание")
btn2 = KeyboardButton("👩‍🏫 Преподаватели")
btn3 = KeyboardButton("🎵 Дисциплины")
btn4 = KeyboardButton("📢 Объявления")
btn5 = KeyboardButton("☎️ Контакты")

# ДНИ НЕДЕЛИ

btn6 = KeyboardButton("Понедельник")
btn7 = KeyboardButton("Вторник")
btn8 = KeyboardButton("Среда")
btn9 = KeyboardButton("Четверг")
btn10 = KeyboardButton("Пятница")

main_keyboard.add(btn1)
main_keyboard.add(btn2)
main_keyboard.add(btn3)
main_keyboard.add(btn4)
main_keyboard.add(btn5)

main_keyboard.add(btn6, btn7)
main_keyboard.add(btn8, btn9)
main_keyboard.add(btn10)
