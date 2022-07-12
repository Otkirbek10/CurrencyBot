from aiogram.dispatcher.filters.state import State,StatesGroup

class Swop(StatesGroup):
    from_cur = State()
    to_cur = State()
    amount = State()