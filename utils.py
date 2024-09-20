import requests
from datetime import datetime

COINDESK_API_URL = 'https://api.coindesk.com/v1/bpi'

def get_current_price(currency='USD'):
    """Fetches the current Bitcoin price in the specified currency."""
    try:
        response = requests.get(f"{COINDESK_API_URL}/currentprice/{currency}.json")
        response.raise_for_status()
        return response.json()['bpi'][currency]['rate']
    except requests.exceptions.RequestException as e:
        return f"Error fetching current price: {e}"

def get_historical_data(start_date, end_date, currency='USD'):
    """Fetches historical Bitcoin price data between two dates for a specific currency."""
    try:
        response = requests.get(f"{COINDESK_API_URL}/historical/close.json", params={
            'start': start_date,
            'end': end_date,
            'currency': currency
        })
        response.raise_for_status()
        data = response.json()['bpi']
        # Simulate OHLC (Open, High, Low, Close) for demonstration; real data should be fetched from a different API
        ohlc_data = {date: {'Open': price, 'High': price * 1.02, 'Low': price * 0.98, 'Close': price} 
                     for date, price in data.items()}
        return ohlc_data
    except requests.exceptions.RequestException as e:
        print(f"Error fetching historical data: {e}")
        return {}
