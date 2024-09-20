from dash import Dash, dcc, html, Input, Output
import dash_bootstrap_components as dbc
from flask import Flask, jsonify, request
import plotly.graph_objects as go
from utils import get_current_price, get_historical_data, convert_currency
from analysis import calculate_moving_averages, calculate_price_changes
from visualizations import create_line_chart, create_candlestick_chart, create_bar_chart

server = Flask(__name__)
app = Dash(__name__, server=server, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Currency options
currencies = ['USD', 'EUR', 'GBP', 'JPY']

# Dashboard layout
app.layout = dbc.Container([
    dbc.Row(dbc.Col(html.H1("Bitcoin Price Analysis Dashboard"))),
    dbc.Row([
        dbc.Col(html.Div([
            dcc.Dropdown(id='currency-dropdown', options=[{'label': cur, 'value': cur} for cur in currencies], value='USD'),
            dcc.DatePickerRange(id='date-picker', start_date='2021-01-01', end_date='2024-01-01'),
        ])),
        dbc.Col(html.Div(id='current-price')),
    ]),
    dbc.Row([
        dbc.Col(dcc.Graph(id='line-chart')),
        dbc.Col(dcc.Graph(id='candlestick-chart')),
    ]),
    dbc.Row([
        dbc.Col(dcc.Graph(id='bar-chart')),
    ])
])

# Callbacks for interactive elements
@app.callback(
    [Output('current-price', 'children'),
     Output('line-chart', 'figure'),
     Output('candlestick-chart', 'figure'),
     Output('bar-chart', 'figure')],
    [Input('currency-dropdown', 'value'),
     Input('date-picker', 'start_date'),
     Input('date-picker', 'end_date')]
)
def update_dashboard(currency, start_date, end_date):
    # Fetch data
    current_price = get_current_price(currency)
    historical_data = get_historical_data(start_date, end_date, currency)
    
    # Analysis
    ma7, ma30 = calculate_moving_averages(historical_data)
    daily_changes, weekly_changes = calculate_price_changes(historical_data)
    
    # Create charts
    line_chart = create_line_chart(historical_data, ma7, ma30)
    candlestick_chart = create_candlestick_chart(historical_data)
    bar_chart = create_bar_chart(daily_changes)

    return (f"Current Price: {current_price} {currency}", line_chart, candlestick_chart, bar_chart)


# API Endpoints
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
