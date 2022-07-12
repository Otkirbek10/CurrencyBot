import requests

def convert_cur(from_cur, to_cur, amount=1):
    # url = f"https://v6.exchangerate-api.com/v6/43e9580d1e2a6df2c2a7f467/pair/{from_cur}/{to_cur}/{amount}"
    # url = f"https://v6.exchangerate-api.com/v6/43e9580d1e2a6df2c2a7f467/latest/{from_cur}/{to_cur}/{amount}"
    url = f'https://v6.exchangerate-api.com/v6/43e9580d1e2a6df2c2a7f467/pair/{from_cur}/{to_cur}/{amount}'
    response = requests.get(url)
    data = response.json()
    print(to_cur,from_cur,amount)

    last = data['time_last_update_utc']
    res = data['conversion_result']

    result = {
            'update': last,
            'res': res
        }

    return result