from dash import Dash, dcc, html, Input, Output
import dash_bootstrap_components as dbc
from flask import Flask, jsonify, request
from utils import get_current_price, get_historical_data
from analysis import calculate_moving_averages, calculate_price_changes, calculate_rsi, calculate_macd
from visualizations import create_line_chart, create_candlestick_chart, create_volume_chart, create_rsi_chart, create_macd_chart

# Setup Flask and Dash
server = Flask(__name__)
app = Dash(__name__, server=server, external_stylesheets=[dbc.themes.CYBORG])

# Layout for the dashboard
app.layout = dbc.Container([
    dbc.Row(dbc.Col(html.H1("Bitcoin Price Analysis Dashboard", className='text-center text-white mt-3'))),
    dbc.Row([
        dbc.Col(html.Div([
            dcc.Dropdown(id='currency-dropdown', options=[{'label': cur, 'value': cur} for cur in ['USD', 'EUR', 'GBP', 'JPY']], value='USD', className='mb-2'),
            dcc.DatePickerRange(id='date-picker', start_date='2021-01-01', end_date='2024-01-01', className='mb-2'),
        ]), width=6),
        dbc.Col(html.Div(id='current-price', className='text-white text-center mb-2'), width=6),
    ]),
    dbc.Row([
        dbc.Col(dcc.Graph(id='line-chart'), width=6),
        dbc.Col(dcc.Graph(id='candlestick-chart'), width=6),
    ]),
    dbc.Row([
        dbc.Col(dcc.Graph(id='volume-chart'), width=6),
        dbc.Col(dcc.Graph(id='rsi-chart'), width=6),
    ]),
    dbc.Row(dbc.Col(dcc.Graph(id='macd-chart'))),
    dcc.Interval(id='interval-component', interval=10*1000, n_intervals=0)  # Real-time updates every 10 seconds
])

@app.callback(
    [Output('current-price', 'children'),
     Output('line-chart', 'figure'),
     Output('candlestick-chart', 'figure'),
     Output('volume-chart', 'figure'),
     Output('rsi-chart', 'figure'),
     Output('macd-chart', 'figure')],
    [Input('currency-dropdown', 'value'),
     Input('date-picker', 'start_date'),
     Input('date-picker', 'end_date'),
     Input('interval-component', 'n_intervals')]
)
def update_dashboard(currency, start_date, end_date, n_intervals):
    # Fetch real-time current price
    current_price = get_current_price(currency)
    # Fetch historical data within the selected date range
    historical_data = get_historical_data(start_date, end_date, currency)

    if not historical_data:
        return "No data available", {}, {}, {}, {}, {}

    # Perform analysis
    ma7, ma30 = calculate_moving_averages(historical_data)
    rsi = calculate_rsi(historical_data)
    macd_line, signal_line = calculate_macd(historical_data)
    daily_changes, _ = calculate_price_changes(historical_data)

    # Create charts
    line_chart = create_line_chart(historical_data, ma7, ma30)
    candlestick_chart = create_candlestick_chart(historical_data)
    volume_chart = create_volume_chart(historical_data)
    rsi_chart = create_rsi_chart(rsi)
    macd_chart = create_macd_chart(macd_line, signal_line)

    return (f"Current Price: {current_price} {currency}", line_chart, candlestick_chart, volume_chart, rsi_chart, macd_chart)

# Flask API endpoints for programmatic access
@server.route('/api/current_price', methods=['GET'])
def api_current_price():
    currency = request.args.get('currency', 'USD')
    return jsonify({"price": get_current_price(currency)})


@server.route('/api/historical_data', methods=['GET'])
def api_historical_data():
    currency = request.args.get('currency', 'USD')
    start_date = request.args.get('start_date', '2021-01-01')
    end_date = request.args.get('end_date', '2024-01-01')
    data = get_historical_data(start_date, end_date, currency)
    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True)
