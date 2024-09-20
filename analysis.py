import pandas as pd

def calculate_moving_averages(historical_data):
    df = pd.Series(historical_data)
    ma7 = df.rolling(window=7).mean()
    ma30 = df.rolling(window=30).mean()
    return ma7, ma30

def calculate_price_changes(historical_data):
    df = pd.Series(historical_data)
    daily_changes = df.diff()
    weekly_changes = df.diff(7)
    return daily_changes, weekly_changes
