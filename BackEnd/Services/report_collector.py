from Data_Fetcher import get_coin_data

data = get_coin_data()

def calculate_summary(data):

    filtered_keys = ['name', 'symbol', 'current_price', 'high_24h', 'low_24h', 'price_change_percentage_24h']

    return filtered_keys

print(calculate_summary)