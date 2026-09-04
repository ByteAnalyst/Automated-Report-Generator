import requests
import os 
from dotenv import load_dotenv

load_dotenv()

API_key = os.getenv('api')

def get_coin_data(coin_id: str):

    url = f'https://api.coingecko.com/api/v3/coins/markets'

    parameters = {
        "vs_currency": 'USD',
        'ids': coin_id,
        'x_cg_demo_api_key': API_key
    }


    response = requests.get(url, params = parameters)
    response.raise_for_status()
    data = response.json()
    return data[0] if data else None



