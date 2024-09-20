import pandas as pd

def calculate_moving_averages(historical_data):
    df = pd.DataFrame.from_dict(historical_data, orient='index')
    ma7 = df['Close'].rolling(window=7).mean()
    ma30 = df['Close'].rolling(window=30).mean()
    return ma7, ma30

def calculate_rsi(historical_data, period=14):
    df = pd.DataFrame.from_dict(historical_data, orient='index')['Close']
    delta = df.diff()
    gain = (delta.where(delta > 0, 0)).fillna(0)
    loss = (-delta.where(delta < 0, 0)).fillna(0)

    avg_gain = gain.rolling(window=period).mean()
    avg_loss = loss.rolling(window=period).mean()

    rs = avg_gain / avg_loss
    rsi = 100 - (100 / (1 + rs))
    return rsi

def calculate_macd(historical_data, short_period=12, long_period=26, signal_period=9):
    df = pd.DataFrame.from_dict(historical_data, orient='index')['Close']
    short_ema = df.ewm(span=short_period, adjust=False).mean()
    long_ema = df.ewm(span=long_period, adjust=False).mean()

    macd_line = short_ema - long_ema
    signal_line = macd_line.ewm(span=signal_period, adjust=False).mean()

    return macd_line, signal_line

def calculate_price_changes(historical_data):
    df = pd.DataFrame.from_dict(historical_data, orient='index')['Close']
    daily_changes = df.diff()
    weekly_changes = df.diff(7)
    return daily_changes, weekly_changes
