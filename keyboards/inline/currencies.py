from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton

currency = InlineKeyboardMarkup(row_width=3)
uzs = InlineKeyboardButton(text = '🇺🇿 UZS',callback_data='UZS')
currency.insert(uzs)
rub = InlineKeyboardButton(text = '🇷🇺 RUB',callback_data='RUB')
currency.insert(rub)
usd = InlineKeyboardButton(text = '🇺🇸 USD',callback_data='USD')
currency.insert(usd)
eur = InlineKeyboardButton(text = '🇪🇺 EUR',callback_data='EUR')
currency.insert(eur)
gbp = InlineKeyboardButton(text = '🇬🇧 GBP',callback_data='GBP')
currency.insert(gbp)
jny = InlineKeyboardButton(text = '🇯🇵 JPY',callback_data='JPY')
currency.insert(jny)
irr = InlineKeyboardButton(text = '🇮🇷 IRR',callback_data='IRR')
currency.insert(irr)
aed = InlineKeyboardButton(text = '🇦🇪 AED',callback_data='AED')
currency.insert(aed)
cny = InlineKeyboardButton(text = '🇨🇳 CNY',callback_data='CNY')
currency.insert(cny)
krw = InlineKeyboardButton(text = '🇰🇷 KRW',callback_data='KRW')
currency.insert(krw)
tr = InlineKeyboardButton(text = '🇹🇷 TRY',callback_data='TRY')
currency.insert(tr)
kzt = InlineKeyboardButton(text = '🇰🇿 KZT',callback_data='KZT')
currency.insert(kzt)
bac = InlineKeyboardButton(text = '🔙 Orqaga',callback_data='bak')
currency.insert(bac)

back = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='🔙 Orqaga',callback_data='bak')]
    ]
)

bak = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='🔙 Orqaga',callback_data='back')]
    ]
)