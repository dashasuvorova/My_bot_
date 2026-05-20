from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from database import add_homework, get_student

router = Router()

class AddHomeworkStates(StatesGroup):
    waiting_for_subject = State()
    waiting_for_task = State()
    waiting_for_date = State()

@router.message(F.text == "➕ Добавить домашнее задание")
async def cmd_add_hw(message: Message, state: FSMContext):
    student = get_student(message.from_user.id)
    if not student:
        await message.answer("Сначала зарегистрируйся через /start")
        return
    await message.answer("Напиши название предмета (например, Фортепиано):")
    await state.set_state(AddHomeworkStates.waiting_for_subject)

@router.message(AddHomeworkStates.waiting_for_subject)
async def add_hw_subject(message: Message, state: FSMContext):
    await state.update_data(subject=message.text)
    await message.answer("Теперь напиши описание задания (что нужно выучить):")
    await state.set_state(AddHomeworkStates.waiting_for_task)

@router.message(AddHomeworkStates.waiting_for_task)
async def add_hw_task(message: Message, state: FSMContext):
    await state.update_data(task=message.text)
    await message.answer("Введи дату сдачи в формате ДД.ММ.ГГГГ (например, 30.05.2026):")
    await state.set_state(AddHomeworkStates.waiting_for_date)

@router.message(AddHomeworkStates.waiting_for_date)
async def add_hw_date(message: Message, state: FSMContext):
    due_date = message.text
    # Проверка формата и прошедшей даты
    try:
        due_date_obj = datetime.strptime(due_date, "%d.%m.%Y").date()
        if due_date_obj < get_izhevsk_now().date():
            await message.answer("❌ Нельзя добавить задание на прошедшую дату!")
            return
    except ValueError:
        await message.answer("❌ Неверный формат. Используй ДД.ММ.ГГГГ")
        return

    data = await state.get_data()
    student = get_student(message.from_user.id)
    add_homework(student["user_id"], data["subject"], data["task"], due_date)
    await message.answer(f"✅ Задание по {data['subject']} добавлено! Срок: {due_date}")
    await state.clear()
