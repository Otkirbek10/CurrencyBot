import requests

url_usd = f"https://v6.exchangerate-api.com/v6/462078e42ed014b981331528/pair/USD/UZS/"
res_usd = requests.get(url_usd).json()
msg_usd = f"{res_usd['conversion_rate']}"

url_rub = f"https://v6.exchangerate-api.com/v6/462078e42ed014b981331528/pair/RUB/UZS/"
res_rub = requests.get(url_rub).json()
msg_rub = f"{res_rub['conversion_rate']}"

url_eur = f"https://v6.exchangerate-api.com/v6/462078e42ed014b981331528/pair/EUR/UZS/"
res_eur = requests.get(url_eur).json()
msg_eur = f"{res_eur['conversion_rate']}"

url_gbp = f"https://v6.exchangerate-api.com/v6/462078e42ed014b981331528/pair/GBP/UZS/"
res_gbp = requests.get(url_gbp).json()
msg_gbp = f"{res_gbp['conversion_rate']}"

url_cny = f"https://v6.exchangerate-api.com/v6/462078e42ed014b981331528/pair/CNY/UZS/"
res_cny = requests.get(url_cny).json()
msg_cny = f"{res_cny['conversion_rate']}"

url_krw = f"https://v6.exchangerate-api.com/v6/462078e42ed014b981331528/pair/KRW/UZS/"
res_krw = requests.get(url_krw).json()
msg_krw = f"{res_krw['conversion_rate']}"

url_try = f"https://v6.exchangerate-api.com/v6/462078e42ed014b981331528/pair/TRY/UZS/"
res_try = requests.get(url_try).json()
msg_try = f"{res_try['conversion_rate']}"

url_kzt = f"https://v6.exchangerate-api.com/v6/462078e42ed014b981331528/pair/KZT/UZS/"
res_kzt = requests.get(url_kzt).json()
msg_kzt = f"{res_kzt['conversion_rate']}"