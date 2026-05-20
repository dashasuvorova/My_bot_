from aiogram.dispatcher.filters.state import State, StatesGroup

class AddAnnouncementState(StatesGroup):

    waiting_for_text = State()
