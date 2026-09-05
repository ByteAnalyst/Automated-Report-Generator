from Services.Data_Fetcher import get_coin_data

data = get_coin_data('bitcoin')

def calculate_summary(coin_dict):

    keys = ['name', 'symbol', 'current_price', 'high_24h', 'low_24h', 'price_change_percentage_24h']

    price_change = coin_dict.get('price_change_percentage_24h')

    if (price_change > 0):
        label = 'Up'
    else:
        label = 'Down'

    summary = {k: coin_dict.get(k) for k in keys}
    summary['trend'] = label

    return summary