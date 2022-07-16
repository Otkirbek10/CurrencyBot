import sqlite3

from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from data.url import *
from data.config import ADMINS
from keyboards.inline.exchenge import exchenge
from loader import dp, db, bot


@dp.message_handler(CommandStart(),state='*')
async def bot_start(message: types.Message):
    name = message.from_user.full_name
    # Foydalanuvchini bazaga qo'shamiz
    try:
        db.add_user(id=message.from_user.id,
                    name=name)
        await message.answer(f"🤗 Xush kelibsiz {name}\n\nMa'lumot olish uchun /help buyrug'ini bosing")
        await message.answer( f"🤖 Men sizga yordam beruvchi botman ....\n\n"
                              f"🤝 Shunga o'xshash yoki umuman boshqacha bot buyurtma berishni xoxlaysizmi? <a href='https://t.me/Unstoppable_stranger'>O'tkirbek</a>")
        await message.answer(f"🇺🇸 1 AQSH dollari (USD) - {msg_usd} so'm\n🇷🇺 1 Rossiya rubli (RUB) - {msg_rub} so'm\n🇨🇳 1 Xitoy yuani (CNY) - {msg_cny} so'm\n🇪🇺 1 Yevro (EUR) - {msg_eur} so'm\n🇬🇧 1 Angliya funt sterlingi (GBP) - {msg_gbp} so'm\n🇯🇵 1 Yaponiya iyenasi (JPY) - {msg_jpy} so'm\n🇮🇷 1 Eron riali (IRR) - {msg_irr} so'm\n🇦🇪 1 BAA dirhami (AED) - {msg_aed} so'm\n🇰🇷 1 Koreya respublikasi voni (KRW) - {msg_krw} so'm\n🇹🇷 1 Turkiya lirasi (TRY) - {msg_try} so'm\n🇰🇿 1 Qozog‘iston tengesi (KZT) -  {msg_kzt} so'm",reply_markup=exchenge)
        # Adminga xabar beramiz
        count = db.count_users()[0]
        msg = f"{message.from_user.full_name} bazaga qo'shildi.\nBazada {count} ta foydalanuvchi bor."
        await bot.send_message(chat_id=ADMINS[0], text=msg)

    except sqlite3.IntegrityError as err:
        await bot.send_message(chat_id=ADMINS[0], text=f"{name} bazaga oldin qo'shilgan")
        await message.answer(f"🤗 Xush kelibsiz {name}\n\nMa'lumot olish uchun /help buyrug'ini bosing")
        await message.answer( f"🤖 Я бот который поможет ....\n\n"
                              f"🤝 Shunga o'xshash yoki umuman boshqacha bot buyurtma berishni xoxlaysizmi? <a href='https://t.me/Unstoppable_stranger'>O'tkirbek</a>")
        await message.answer(f"🇺🇸 1 AQSH dollari (USD) - {msg_usd} so'm\n🇷🇺 1 Rossiya rubli (RUB) - {msg_rub} so'm\n🇨🇳 1 Xitoy yuani (CNY) - {msg_cny} so'm\n🇪🇺 1 Yevro (EUR) - {msg_eur} so'm\n🇬🇧 1 Angliya funt sterlingi (GBP) - {msg_gbp} so'm\n🇯🇵 1 Yaponiya iyenasi (JPY) - {msg_jpy} so'm\n🇮🇷 1 Eron riali (IRR) - {msg_irr} so'm\n🇦🇪 1 BAA dirhami (AED) - {msg_aed} so'm\n🇰🇷 1 Koreya respublikasi voni (KRW) - {msg_krw} so'm\n🇹🇷 1 Turkiya lirasi (TRY) - {msg_try} so'm\n🇰🇿 1 Qozog‘iston tengesi (KZT) -  {msg_kzt} so'm",reply_markup=exchenge)