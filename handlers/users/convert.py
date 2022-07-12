
import logging
from loader import dp
from aiogram import types
from states.state import Swop
from aiogram.dispatcher import FSMContext
from keyboards.inline.currencies import back
from data.cont import convert_cur


@dp.message_handler(state=Swop.amount)
async def amount(message:types.Message,state:FSMContext):
    try:   
        x = int(message.text)
        data = await state.get_data()
        from_cur = data.get('from_cur')
        to_cur = data.get('to_cur')
        res = convert_cur(from_cur, to_cur, amount=x)
        msg = f"♻️Aylantirildi: {x} {from_cur} ➡️ {res['res']} {to_cur}"
        await message.answer(msg)
    except ValueError:
        await message.answer('uuuuu')
    




