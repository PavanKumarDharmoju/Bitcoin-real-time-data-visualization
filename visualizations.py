import plotly.graph_objects as go

def create_line_chart(historical_data, ma7, ma30):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=list(historical_data.keys()), y=list(historical_data.values()), mode='lines', name='Price'))
    fig.add_trace(go.Scatter(x=ma7.index, y=ma7.values, mode='lines', name='7-day MA'))
    fig.add_trace(go.Scatter(x=ma30.index, y=ma30.values, mode='lines', name='30-day MA'))
    return fig

def create_candlestick_chart(historical_data):
    # Use OHLC data for candlestick charts
    pass  # Implement candlestick chart

def create_bar_chart(daily_changes):
    fig = go.Figure([go.Bar(x=daily_changes.index, y=daily_changes.values)])
    return fig
