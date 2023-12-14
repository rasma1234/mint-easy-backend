import requests
from datetime import datetime
from .models import ForexData


def fetch_forex_data(api_key, symbol):
    api_endpoint = f'https://api.twelvedata.com/time_series?symbol={symbol}&interval=1d&apikey={api_key}'
    
    try:
        # Make a GET request to the Twelve Data API
        response = requests.get(api_endpoint)
        response.raise_for_status()  # Raise an HTTPError for bad responses

        # Parse the API response (assuming it's in JSON format)
        forex_data_list = response.json()
        print(forex_data_list)

        # Check if 'values' key exists in the response
        if 'values' in forex_data_list:
            # Save data to the database using the Django model
            for forex_data in forex_data_list['values']:
                ForexData.objects.create(
                    symbol=forex_data['symbol'],
                    datetime=datetime.utcfromtimestamp(forex_data['datetime']),
                    current_price=forex_data['close'],
                    open_price=forex_data['open'],
                    close_price=forex_data['close'],
                    high_price=forex_data['high'],
                    low_price=forex_data['low'],
                    percent_change=forex_data['percent_change'],
                )

            print('Data successfully fetched and stored in the database.')
        else:
            print('Unexpected API response format. Missing "values" key.')

    except requests.RequestException as e:
        print(f'Error fetching data from the API: {e}')

api_key = 'b6e55de583394e2b97799f6a82e3156a'
symbol = 'EUR/USD'

fetch_forex_data(api_key, symbol)
