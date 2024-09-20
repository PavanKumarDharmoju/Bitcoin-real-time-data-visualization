# Bitcoin Price Analysis Dashboard

## Features
- Fetch real-time and historical Bitcoin price data from the CoinDesk API
- Calculate daily, weekly, and monthly price changes
- Perform moving averages and display price trends
- Interactive dashboard with date and currency selection

## Setup Instructions

1. Clone the repository:
```bash
git clone https://github.com/your-repo/bitcoin_dashboard.git cd bitcoin_dashboard
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
python app.py
```



4. Access the dashboard at `http://127.0.0.1:8050/`.

## Docker Deployment

1. Build the Docker image:
```bash
docker build -t bitcoin-dashboard .
```



2. Run the Docker container:
```bash
docker run -p 8050:8050 bitcoin-dashboard
```


## Available Currencies
- USD
- EUR
- GBP
- JPY