import requests
import time

COINDESK_API_URL = 'https://api.coindesk.com/v1/bpi'

def get_current_price(currency='USD'):
    try:
        response = requests.get(f"{COINDESK_API_URL}/currentprice/{currency}.json")
        response.raise_for_status()
        return response.json()['bpi'][currency]['rate']
    except requests.exceptions.RequestException as e:
        return f"Error fetching current price: {e}"

def get_historical_data(start_date, end_date, currency='USD'):
    try:
        response = requests.get(f"{COINDESK_API_URL}/historical/close.json", params={
            'start': start_date,
            'end': end_date,
            'currency': currency
        })
        response.raise_for_status()
        return response.json()['bpi']
    except requests.exceptions.RequestException as e:
        return f"Error fetching historical data: {e}"

def convert_currency(price, from_currency, to_currency):
    # Example of using a currency conversion API (exchange rates)
    # Implement actual currency conversion logic here.
    pass
