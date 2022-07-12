
import logging
from loader import dp
from aiogram import types
from states.state import Swop
from aiogram.dispatcher import FSMContext
from keyboards.inline.currencies import bak,currency
from data.cont import convert_cur


@dp.message_handler(state=Swop.amount)
async def amount(message:types.Message,state:FSMContext):
    try:   
        x = float(message.text)
        data = await state.get_data()
        from_cur = data.get('from_cur')
        to_cur = data.get('to_cur')
        res = convert_cur(from_cur, to_cur, amount=x)
        msg = f"♻️Aylantirildi: {x} {from_cur} ➡️ {res['res']} {to_cur}"
        await message.answer(msg,reply_markup=bak)
    except ValueError:
        await message.answer('Faqat 1 yoki 1.1 tarzida kiriting!')

@dp.callback_query_handler(text_contains="back",state=Swop.amount)
async def from_to(call: types.CallbackQuery):
    await call.answer(cache_time=20)
    callback_data = call.data
    logging.info(f"{callback_data=}")
    logging.info(f"{call.from_user.username=}")
    await call.message.edit_text("🔄Qaysi valyutani ayirboshlamoqchisiz?", reply_markup=currency)
    await Swop.from_cur.set()
    




