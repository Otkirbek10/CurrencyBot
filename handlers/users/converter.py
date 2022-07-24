from email import message
import logging
from loader import dp
from aiogram import types
from states.state import Swop
from keyboards.inline.exchenge import exchenge
from keyboards.inline.currencies import currency,back
from data.url import *
from aiogram.dispatcher import FSMContext

@dp.callback_query_handler(text="air",state="*")
async def converter_cur(call: types.CallbackQuery):
    await call.answer(cache_time=20)
    callback_data = call.data
    logging.info(f"{callback_data=}")
    logging.info(f"{call.from_user.username=}")
    await call.message.delete()
    await call.message.answer("<b>🔄Qaysi valyutani ayirboshlamoqchisiz?</b>", reply_markup=currency)
    await Swop.from_cur.set()

@dp.callback_query_handler(text_contains='UZS',state=Swop.from_cur)
async def uzs(call:types.CallbackQuery,state:FSMContext):    
    callback_data = call.data
    logging.info(f"{callback_data=}")
    logging.info(f"{call.from_user.username=}")
    await state.update_data(
       {"from_cur": callback_data},
    )
    await call.message.edit_text("<b>🔄Tanlagan valyutangizni qaysi valyuta bilan ayirboshlamoqchisiz?</b>", reply_markup=currency)
    await Swop.next()
    


@dp.callback_query_handler(text_contains='RUB',state=Swop.from_cur)
async def rus(call:types.CallbackQuery,state:FSMContext):
    callback_data = call.data
    logging.info(f"{callback_data=}")
    logging.info(f"{call.from_user.username=}")
    await state.update_data(
        {"from_cur": callback_data},
    )
    await call.message.edit_text("🔄Tanlagan valyutangizni qaysi valyuta bilan ayirboshlamoqchisiz?", reply_markup=currency)
    await Swop.next()

@dp.callback_query_handler(text_contains='USD',state=Swop.from_cur)
async def usa(call:types.CallbackQuery,state:FSMContext):
    callback_data = call.data
    logging.info(f"{callback_data=}")
    logging.info(f"{call.from_user.username=}")
    await state.update_data(
        {"from_cur": callback_data},
    )
    await call.message.edit_text("🔄Tanlagan valyutangizni qaysi valyuta bilan ayirboshlamoqchisiz?", reply_markup=currency)
    await Swop.next()  

@dp.callback_query_handler(text_contains='EUR',state=Swop.from_cur)
async def usa(call:types.CallbackQuery,state:FSMContext):
    callback_data = call.data
    logging.info(f"{callback_data=}")
    logging.info(f"{call.from_user.username=}")
    await state.update_data(
        {"from_cur": callback_data},
    )
    await call.message.edit_text("🔄Tanlagan valyutangizni qaysi valyuta bilan ayirboshlamoqchisiz?", reply_markup=currency)
    await Swop.next()

@dp.callback_query_handler(text_contains='GBP',state=Swop.from_cur)
async def uk(call:types.CallbackQuery,state:FSMContext):
    callback_data = call.data
    logging.info(f"{callback_data=}")
    logging.info(f"{call.from_user.username=}")
    await state.update_data(
        {"from_cur": callback_data},
    )
    await call.message.edit_text("🔄Tanlagan valyutangizni qaysi valyuta bilan ayirboshlamoqchisiz?", reply_markup=currency)
    await Swop.next()

@dp.callback_query_handler(text_contains='JPY',state=Swop.from_cur)
async def uk(call:types.CallbackQuery,state:FSMContext):
    callback_data = call.data
    logging.info(f"{callback_data=}")
    logging.info(f"{call.from_user.username=}")
    await state.update_data(
        {"from_cur": callback_data},
    )
    await call.message.edit_text("🔄Tanlagan valyutangizni qaysi valyuta bilan ayirboshlamoqchisiz?", reply_markup=currency)
    await Swop.next()

@dp.callback_query_handler(text_contains='IRR',state=Swop.from_cur)
async def uk(call:types.CallbackQuery,state:FSMContext):
    callback_data = call.data
    logging.info(f"{callback_data=}")
    logging.info(f"{call.from_user.username=}")
    await state.update_data(
        {"from_cur": callback_data},
    )
    await call.message.edit_text("🔄Tanlagan valyutangizni qaysi valyuta bilan ayirboshlamoqchisiz?", reply_markup=currency)
    await Swop.next()

@dp.callback_query_handler(text_contains='AED',state=Swop.from_cur)
async def uk(call:types.CallbackQuery,state:FSMContext):
    callback_data = call.data
    logging.info(f"{callback_data=}")
    logging.info(f"{call.from_user.username=}")
    await state.update_data(
        {"from_cur": callback_data},
    )
    await call.message.edit_text("🔄Tanlagan valyutangizni qaysi valyuta bilan ayirboshlamoqchisiz?", reply_markup=currency)
    await Swop.next()

@dp.callback_query_handler(text_contains='CNY',state=Swop.from_cur)
async def yuan(call:types.CallbackQuery,state:FSMContext):
    callback_data = call.data
    logging.info(f"{callback_data=}")
    logging.info(f"{call.from_user.username=}")
    await state.update_data(
        {"from_cur": callback_data},
    )
    await call.message.edit_text("🔄Tanlagan valyutangizni qaysi valyuta bilan ayirboshlamoqchisiz?", reply_markup=currency)
    await Swop.next()

@dp.callback_query_handler(text_contains='KRW',state=Swop.from_cur)
async def won(call:types.CallbackQuery,state:FSMContext):
    callback_data = call.data
    logging.info(f"{callback_data=}")
    logging.info(f"{call.from_user.username=}")
    await state.update_data(
        {"from_cur": callback_data},
    )
    await call.message.edit_text("🔄Tanlagan valyutangizni qaysi valyuta bilan ayirboshlamoqchisiz?", reply_markup=currency)
    await Swop.next()

@dp.callback_query_handler(text_contains='TRY',state=Swop.from_cur)
async def tr(call:types.CallbackQuery,state:FSMContext):
    callback_data = call.data
    logging.info(f"{callback_data=}")
    logging.info(f"{call.from_user.username=}")
    await state.update_data(
        {"from_cur": callback_data},
    )
    await call.message.edit_text("🔄Tanlagan valyutangizni qaysi valyuta bilan ayirboshlamoqchisiz?", reply_markup=currency)
    await Swop.next()

@dp.callback_query_handler(text_contains='KZT',state=Swop.from_cur)
async def tr(call:types.CallbackQuery,state:FSMContext):
    callback_data = call.data
    logging.info(f"{callback_data=}")
    logging.info(f"{call.from_user.username=}")
    await state.update_data(
        {"from_cur": callback_data},
    )
    await call.message.edit_text("🔄Tanlagan valyutangizni qaysi valyuta bilan ayirboshlamoqchisiz?", reply_markup=currency)
    await Swop.next()

@dp.callback_query_handler(text_contains='UZS',state=Swop.to_cur)
async def uzs(call:types.CallbackQuery,state:FSMContext):
    callback_data = call.data
    logging.info(f"{callback_data=}")
    logging.info(f"{call.from_user.username=}")
    await state.update_data(
        {'to_cur':callback_data}
    )
    data = await state.get_data()
    from_cur = data.get('from_cur')
    to_cur = data.get('to_cur')
    if from_cur == to_cur:
        await call.answer('🚫 Kechirasiz bir xil valyutalar o\'rtasida airboshlash mumkin emas',show_alert=True)
    else:
        await call.message.edit_text("<b>🔄Ayirboshlash uchun son kiriting:Masalan: 1 yoki 1.1</b>",reply_markup=back)
        await Swop.next()
        
    

@dp.callback_query_handler(text_contains='RUB',state=Swop.to_cur)
async def ru(call:types.CallbackQuery,state:FSMContext):
    callback_data = call.data
    logging.info(f"{callback_data=}")
    logging.info(f"{call.from_user.username=}")
    await state.update_data(
        {'to_cur':callback_data}
    )
    data = await state.get_data()
    from_cur = data.get('from_cur')
    to_cur = data.get('to_cur')
    if from_cur == to_cur:
        await call.answer('🚫 Kechirasiz bir xil valyutalar o\'rtasida airboshlash mumkin emas',show_alert=True)
    else:
        await call.message.edit_text("<b>🔄Ayirboshlash uchun son kiriting:Masalan: 1 yoki 1.1</b>",reply_markup=back)
        await Swop.next()
        

@dp.callback_query_handler(text_contains='USD',state=Swop.to_cur)
async def u(call:types.CallbackQuery,state:FSMContext):
    callback_data = call.data
    logging.info(f"{callback_data=}")
    logging.info(f"{call.from_user.username=}")
    await state.update_data(
        {'to_cur':callback_data}
    )
    data = await state.get_data()
    from_cur = data.get('from_cur')
    to_cur = data.get('to_cur')
    if from_cur == to_cur:
        await call.answer('🚫 Kechirasiz bir xil valyutalar o\'rtasida airboshlash mumkin emas',show_alert=True)
    else:
        await call.message.edit_text("<b>🔄Ayirboshlash uchun son kiriting:Masalan: 1 yoki 1.1</b>",reply_markup=back)
        await Swop.next()
        

@dp.callback_query_handler(text_contains='EUR',state=Swop.to_cur)
async def eu(call:types.CallbackQuery,state:FSMContext):
    callback_data = call.data
    logging.info(f"{callback_data=}")
    logging.info(f"{call.from_user.username=}")
    await state.update_data(
        {'to_cur':callback_data}
    )
    data = await state.get_data()
    from_cur = data.get('from_cur')
    to_cur = data.get('to_cur')
    if from_cur == to_cur:
        await call.answer('🚫 Kechirasiz bir xil valyutalar o\'rtasida airboshlash mumkin emas',show_alert=True)
    else:
        await call.message.edit_text("<b>🔄Ayirboshlash uchun son kiriting:Masalan: 1 yoki 1.1</b>",reply_markup=back)
        await Swop.next()
        

@dp.callback_query_handler(text_contains='GBP',state=Swop.to_cur)
async def gb(call:types.CallbackQuery,state:FSMContext):
    callback_data = call.data
    logging.info(f"{callback_data=}")
    logging.info(f"{call.from_user.username=}")
    await state.update_data(
        {'to_cur':callback_data}
    )
    data = await state.get_data()
    from_cur = data.get('from_cur')
    to_cur = data.get('to_cur')
    if from_cur == to_cur:
        await call.answer('🚫 Kechirasiz bir xil valyutalar o\'rtasida airboshlash mumkin emas',show_alert=True)
    else:
        await call.message.edit_text("<b>🔄Ayirboshlash uchun son kiriting:Masalan: 1 yoki 1.1</b>",reply_markup=back)
        await Swop.next()

@dp.callback_query_handler(text_contains='JPY',state=Swop.to_cur)
async def gb(call:types.CallbackQuery,state:FSMContext):
    callback_data = call.data
    logging.info(f"{callback_data=}")
    logging.info(f"{call.from_user.username=}")
    await state.update_data(
        {'to_cur':callback_data}
    )
    data = await state.get_data()
    from_cur = data.get('from_cur')
    to_cur = data.get('to_cur')
    if from_cur == to_cur:
        await call.answer('🚫 Kechirasiz bir xil valyutalar o\'rtasida airboshlash mumkin emas',show_alert=True)
    else:
        await call.message.edit_text("<b>🔄Ayirboshlash uchun son kiriting:Masalan: 1 yoki 1.1</b>",reply_markup=back)
        await Swop.next()

@dp.callback_query_handler(text_contains='IRR',state=Swop.to_cur)
async def gb(call:types.CallbackQuery,state:FSMContext):
    callback_data = call.data
    logging.info(f"{callback_data=}")
    logging.info(f"{call.from_user.username=}")
    await state.update_data(
        {'to_cur':callback_data}
    )
    data = await state.get_data()
    from_cur = data.get('from_cur')
    to_cur = data.get('to_cur')
    if from_cur == to_cur:
        await call.answer('🚫 Kechirasiz bir xil valyutalar o\'rtasida airboshlash mumkin emas',show_alert=True)
    else:
        await call.message.edit_text("<b>🔄Ayirboshlash uchun son kiriting:Masalan: 1 yoki 1.1</b>",reply_markup=back)
        await Swop.next()
        
@dp.callback_query_handler(text_contains='AED',state=Swop.to_cur)
async def gb(call:types.CallbackQuery,state:FSMContext):
    callback_data = call.data
    logging.info(f"{callback_data=}")
    logging.info(f"{call.from_user.username=}")
    await state.update_data(
        {'to_cur':callback_data}
    )
    data = await state.get_data()
    from_cur = data.get('from_cur')
    to_cur = data.get('to_cur')
    if from_cur == to_cur:
        await call.answer('🚫 Kechirasiz bir xil valyutalar o\'rtasida airboshlash mumkin emas',show_alert=True)
    else:
        await call.message.edit_text("<b>🔄Ayirboshlash uchun son kiriting:Masalan: 1 yoki 1.1</b>",reply_markup=back)
        await Swop.next()

@dp.callback_query_handler(text_contains='CNY',state=Swop.to_cur)
async def cn(call:types.CallbackQuery,state:FSMContext):
    callback_data = call.data
    logging.info(f"{callback_data=}")
    logging.info(f"{call.from_user.username=}")
    await state.update_data(
        {'to_cur':callback_data}
    )
    data = await state.get_data()
    from_cur = data.get('from_cur')
    to_cur = data.get('to_cur')
    if from_cur == to_cur:
        await call.answer('🚫 Kechirasiz bir xil valyutalar o\'rtasida airboshlash mumkin emas',show_alert=True)
    else:
        await call.message.edit_text("<b>🔄Ayirboshlash uchun son kiriting:Masalan: 1 yoki 1.1</b>",reply_markup=back)
        await Swop.next()
        

@dp.callback_query_handler(text_contains='KRW',state=Swop.to_cur)
async def kr(call:types.CallbackQuery,state:FSMContext):
    callback_data = call.data
    logging.info(f"{callback_data=}")
    logging.info(f"{call.from_user.username=}")
    await state.update_data(
        {'to_cur':callback_data}
    )
    data = await state.get_data()
    from_cur = data.get('from_cur')
    to_cur = data.get('to_cur')
    if from_cur == to_cur:
        await call.answer('🚫 Kechirasiz bir xil valyutalar o\'rtasida airboshlash mumkin emas',show_alert=True)
    else:
        await call.message.edit_text("<b>🔄Ayirboshlash uchun son kiriting:Masalan: 1 yoki 1.1</b>",reply_markup=back)
        await Swop.next()
        

@dp.callback_query_handler(text_contains='TRY',state=Swop.to_cur)
async def kz(call:types.CallbackQuery,state:FSMContext):
    callback_data = call.data
    logging.info(f"{callback_data=}")
    logging.info(f"{call.from_user.username=}")
    await state.update_data(
        {'to_cur':callback_data}
    )
    data = await state.get_data()
    from_cur = data.get('from_cur')
    to_cur = data.get('to_cur')
    if from_cur == to_cur:
        await call.answer('🚫 Kechirasiz bir xil valyutalar o\'rtasida airboshlash mumkin emas',show_alert=True)
    else:
        await call.message.edit_text("<b>🔄Ayirboshlash uchun son kiriting:Masalan: 1 yoki 1.1</b>",reply_markup=back)
        await Swop.next()
        

@dp.callback_query_handler(text_contains='KZT',state=Swop.to_cur)
async def kz(call:types.CallbackQuery,state:FSMContext):
    callback_data = call.data
    logging.info(f"{callback_data=}")
    logging.info(f"{call.from_user.username=}")
    await state.update_data(
        {'to_cur':callback_data}
    )
    data = await state.get_data()
    from_cur = data.get('from_cur')
    to_cur = data.get('to_cur')
    if from_cur == to_cur:
        await call.answer('🚫 Kechirasiz bir xil valyutalar o\'rtasida airboshlash mumkin emas',show_alert=True)
    else:
        await call.message.edit_text("<b>🔄Ayirboshlash uchun son kiriting:Masalan: 1 yoki 1.1</b>",reply_markup=back)
        await Swop.next()
        

@dp.callback_query_handler(text_contains='bak',state=Swop.from_cur)
async def kz(call:types.CallbackQuery,state:FSMContext):
    callback_data = call.data
    logging.info(f"{callback_data=}")
    logging.info(f"{call.from_user.username=}")
    await call.message.delete()
    await call.message.answer(f"🇺🇸 1 AQSH dollari (USD) - {msg_usd} so'm\n🇷🇺 1 Rossiya rubli (RUB) - {msg_rub} so'm\n🇨🇳 1 Xitoy yuani (CNY) - {msg_cny} so'm\n🇪🇺 1 Yevro (EUR) - {msg_eur} so'm\n🇬🇧 1 Angliya funt sterlingi (GBP) - {msg_gbp} so'm\n🇯🇵 1 Yaponiya iyenasi (JPY) - {msg_jpy} so'm\n🇮🇷 1 Eron riali (IRR) - {msg_irr} so'm\n🇦🇪 1 BAA dirhami (AED) - {msg_aed} so'm\n🇰🇷 1 Koreya respublikasi voni (KRW) - {msg_krw} so'm\n🇹🇷 1 Turkiya lirasi (TRY) - {msg_try} so'm\n🇰🇿 1 Qozog‘iston tengesi (KZT) -  {msg_kzt} so'm",reply_markup=exchenge)
    await state.finish()



@dp.callback_query_handler(text_contains="bak", state=Swop.to_cur)
async def from_to(call: types.CallbackQuery):
    callback_data = call.data
    logging.info(f"{callback_data=}")
    logging.info(f"{call.from_user.username=}")
    await call.message.edit_text("🔄Qaysi valyutani ayirboshlamoqchisiz?", reply_markup=currency)
    await Swop.from_cur.set()


@dp.callback_query_handler(text_contains="bak", state=Swop.amount)
async def from_to(call: types.CallbackQuery):
    callback_data = call.data
    logging.info(f"{callback_data=}")
    logging.info(f"{call.from_user.username=}")
    await call.message.edit_text("🔄Qaysi valyutani ayirboshlamoqchisiz?", reply_markup=currency)
    await Swop.from_cur.set()


