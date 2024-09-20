import plotly.graph_objects as go
import pandas as pd

def create_line_chart(historical_data, ma7, ma30):
    df = pd.DataFrame.from_dict(historical_data, orient='index')
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df.index, y=df['Close'], mode='lines', name='Price'))
    fig.add_trace(go.Scatter(x=ma7.index, y=ma7.values, mode='lines', name='7-day MA'))
    fig.add_trace(go.Scatter(x=ma30.index, y=ma30.values, mode='lines', name='30-day MA'))
    return fig

def create_candlestick_chart(historical_data):
    df = pd.DataFrame.from_dict(historical_data, orient='index')
    fig = go.Figure(data=[go.Candlestick(x=df.index,
                                         open=df['Open'],
                                         high=df['High'],
                                         low=df['Low'],
                                         close=df['Close'])])
    fig.update_layout(title="Candlestick Chart")
    return fig

def create_volume_chart(historical_data):
    df = pd.DataFrame.from_dict(historical_data, orient='index')
    # Simulating volume as random values for demonstration purposes
    df['Volume'] = abs(df['Close'].diff() * 1000)  # Simulated volume
    fig = go.Figure([go.Bar(x=df.index, y=df['Volume'])])
    fig.update_layout(title="Volume")
    return fig

def create_rsi_chart(rsi):
    fig = go.Figure([go.Scatter(x=rsi.index, y=rsi.values, mode='lines', name='RSI')])
    fig.update_layout(title="RSI (Relative Strength Index)")
    return fig

def create_macd_chart(macd_line, signal_line):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=macd_line.index, y=macd_line.values, mode='lines', name='MACD Line'))
    fig.add_trace(go.Scatter(x=signal_line.index, y=signal_line.values, mode='lines', name='Signal Line'))
    fig.update_layout(title="MACD")
    return fig
