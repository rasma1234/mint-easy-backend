import requests
from datetime import datetime
from .models import ForexData 
from celery import shared_task
from datetime import datetime
from .models import ForexData, CryptoData
import pytz
#import finnhub

@shared_task
def fetch_forex_data(api_key='4649b1264fd241779aadd41843580216', symbol='EUR/USD', interval='1min', outputsize=1):
    api_endpoint = f'https://api.twelvedata.com/time_series?symbol={symbol}&interval={interval}&apikey={api_key}&outputsize={outputsize}'
    try:
        response = requests.get(api_endpoint)
        forex_data_list = response.json()
        #print(forex_data_list)
        if 'values' in forex_data_list:
            berlin_tz = pytz.timezone('Europe/Berlin')
            for forex_data in forex_data_list['values']:
                datetime_str = forex_data['datetime']
                forex_datetime = datetime.strptime(datetime_str, '%Y-%m-%d %H:%M:%S')
                forex_datetime_utc = pytz.utc.localize(forex_datetime) 
                forex_datetime_berlin = forex_datetime_utc.astimezone(berlin_tz)
                
                ForexData.objects.create(
                    symbol=symbol,
                    datetime=forex_datetime_berlin,
                    current_price=float(forex_data['close']),
                    open_price=float(forex_data['open']),
                    close_price=float(forex_data['close']),
                    high_price=float(forex_data['high']),
                    low_price=float(forex_data['low']),
                    percent_change=float((float(forex_data['close']) - float(forex_data['open'])) / float(forex_data['open']) * 100),
                )
            print('Data successfully fetched and stored in the database.')
        else:
            print('Unexpected API response format. Missing "values" key.')
    except requests.RequestException as e:
        print(f'Error fetching data from the API: {e}')

@shared_task
def fetch_forex_data1(api_key='25979cee57c94c3d830d9ec7d81b66b4', symbol='USD/CAD', interval='1min', outputsize=1):
    api_endpoint = f'https://api.twelvedata.com/time_series?symbol={symbol}&interval={interval}&apikey={api_key}&outputsize={outputsize}'
    try:
        response = requests.get(api_endpoint)
        forex_data_list = response.json()
        #print(forex_data_list)
        if 'values' in forex_data_list:
            berlin_tz = pytz.timezone('Europe/Berlin')
            for forex_data in forex_data_list['values']:
                datetime_str = forex_data['datetime']
                forex_datetime = datetime.strptime(datetime_str, '%Y-%m-%d %H:%M:%S')
                forex_datetime_utc = pytz.utc.localize(forex_datetime) 
                forex_datetime_berlin = forex_datetime_utc.astimezone(berlin_tz)
                
                ForexData.objects.create(
                    symbol=symbol,
                    datetime=forex_datetime_berlin,
                    current_price=float(forex_data['close']),
                    open_price=float(forex_data['open']),
                    close_price=float(forex_data['close']),
                    high_price=float(forex_data['high']),
                    low_price=float(forex_data['low']),
                    percent_change=float((float(forex_data['close']) - float(forex_data['open'])) / float(forex_data['open']) * 100),
                )
            print('Data successfully fetched and stored in the database.')
        else:
            print('Unexpected API response format. Missing "values" key.')
    except requests.RequestException as e:
        print(f'Error fetching data from the API: {e}')


@shared_task
def fetch_forex_data2(api_key='a2375ed749b24365b68f80f615205219', symbol='USD/JPY', interval='1min', outputsize=1):
    api_endpoint = f'https://api.twelvedata.com/time_series?symbol={symbol}&interval={interval}&apikey={api_key}&outputsize={outputsize}'
    try:
        response = requests.get(api_endpoint)
        forex_data_list = response.json()
        #print(forex_data_list)
        if 'values' in forex_data_list:
            berlin_tz = pytz.timezone('Europe/Berlin')
            for forex_data in forex_data_list['values']:
                datetime_str = forex_data['datetime']
                forex_datetime = datetime.strptime(datetime_str, '%Y-%m-%d %H:%M:%S')
                forex_datetime_utc = pytz.utc.localize(forex_datetime) 
                forex_datetime_berlin = forex_datetime_utc.astimezone(berlin_tz)
                
                ForexData.objects.create(
                    symbol=symbol,
                    datetime=forex_datetime_berlin,
                    current_price=float(forex_data['close']),
                    open_price=float(forex_data['open']),
                    close_price=float(forex_data['close']),
                    high_price=float(forex_data['high']),
                    low_price=float(forex_data['low']),
                    percent_change=float((float(forex_data['close']) - float(forex_data['open'])) / float(forex_data['open']) * 100),
                )
            print('Data successfully fetched and stored in the database.')
        else:
            print('Unexpected API response format. Missing "values" key.')
    except requests.RequestException as e:
        print(f'Error fetching data from the API: {e}')


@shared_task
def fetch_forex_data3(api_key='01f82aa7a681472d86ddf857caa90c0a', symbol='USD/CHF', interval='1min', outputsize=1):
    api_endpoint = f'https://api.twelvedata.com/time_series?symbol={symbol}&interval={interval}&apikey={api_key}&outputsize={outputsize}'
    try:
        response = requests.get(api_endpoint)
        forex_data_list = response.json()
        #print(forex_data_list)
        if 'values' in forex_data_list:
            berlin_tz = pytz.timezone('Europe/Berlin')
            for forex_data in forex_data_list['values']:
                datetime_str = forex_data['datetime']
                forex_datetime = datetime.strptime(datetime_str, '%Y-%m-%d %H:%M:%S')
                forex_datetime_utc = pytz.utc.localize(forex_datetime) 
                forex_datetime_berlin = forex_datetime_utc.astimezone(berlin_tz)
                
                ForexData.objects.create(
                    symbol=symbol,
                    datetime=forex_datetime_berlin,
                    current_price=float(forex_data['close']),
                    open_price=float(forex_data['open']),
                    close_price=float(forex_data['close']),
                    high_price=float(forex_data['high']),
                    low_price=float(forex_data['low']),
                    percent_change=float((float(forex_data['close']) - float(forex_data['open'])) / float(forex_data['open']) * 100),
                )
            print('Data successfully fetched and stored in the database.')
        else:
            print('Unexpected API response format. Missing "values" key.')
    except requests.RequestException as e:
        print(f'Error fetching data from the API: {e}')


@shared_task
def fetch_forex_data4(api_key='87dfcae512444ed194e2052f6ac353ca', symbol='GBP/USD', interval='1min', outputsize=1):
    api_endpoint = f'https://api.twelvedata.com/time_series?symbol={symbol}&interval={interval}&apikey={api_key}&outputsize={outputsize}'
    try:
        response = requests.get(api_endpoint)
        forex_data_list = response.json()
        #print(forex_data_list)
        if 'values' in forex_data_list:
            berlin_tz = pytz.timezone('Europe/Berlin')
            for forex_data in forex_data_list['values']:
                datetime_str = forex_data['datetime']
                forex_datetime = datetime.strptime(datetime_str, '%Y-%m-%d %H:%M:%S')
                forex_datetime_utc = pytz.utc.localize(forex_datetime) 
                forex_datetime_berlin = forex_datetime_utc.astimezone(berlin_tz)
                
                ForexData.objects.create(
                    symbol=symbol,
                    datetime=forex_datetime_berlin,
                    current_price=float(forex_data['close']),
                    open_price=float(forex_data['open']),
                    close_price=float(forex_data['close']),
                    high_price=float(forex_data['high']),
                    low_price=float(forex_data['low']),
                    percent_change=float((float(forex_data['close']) - float(forex_data['open'])) / float(forex_data['open']) * 100),
                )
            print('Data successfully fetched and stored in the database.')
        else:
            print('Unexpected API response format. Missing "values" key.')
    except requests.RequestException as e:
        print(f'Error fetching data from the API: {e}')

@shared_task
def fetch_crypto_data(api_key='8ee57089310043829e1143076678af65', symbol='BTC/USD', interval='1min', outputsize=1):
    api_endpoint = f'https://api.twelvedata.com/time_series?symbol={symbol}&interval={interval}&apikey={api_key}&outputsize={outputsize}'
    try:
        response = requests.get(api_endpoint)
        crypto_data_list = response.json()
        #print(crypto_data_list)
        if 'values' in crypto_data_list:
            berlin_tz = pytz.timezone('Europe/Berlin')
            for crypto_data in crypto_data_list['values']:
                datetime_str = crypto_data['datetime']
                crypto_datetime = datetime.strptime(datetime_str, '%Y-%m-%d %H:%M:%S')
                crypto_datetime_utc = pytz.utc.localize(crypto_datetime) 
                crypto_datetime_berlin = crypto_datetime_utc.astimezone(berlin_tz)
                
                CryptoData.objects.create(
                    symbol=symbol,
                    datetime=crypto_datetime_berlin,
                    current_price=float(crypto_data['close']),
                    open_price=float(crypto_data['open']),
                    close_price=float(crypto_data['close']),
                    high_price=float(crypto_data['high']),
                    low_price=float(crypto_data['low']),
                    percent_change=float((float(crypto_data['close']) - float(crypto_data['open'])) / float(crypto_data['open']) * 100),
                )
            print('Data successfully fetched and stored in the database.')
        else:
            print('Unexpected API response format. Missing "values" key.')
    except requests.RequestException as e:
        print(f'Error fetching data from the API: {e}')

@shared_task
def fetch_crypto_data1(api_key='5607c990906143b4a804c8adedfcb092', symbol='ETH/USD', interval='1min', outputsize=1):
    api_endpoint = f'https://api.twelvedata.com/time_series?symbol={symbol}&interval={interval}&apikey={api_key}&outputsize={outputsize}'
    try:
        response = requests.get(api_endpoint)
        crypto_data_list = response.json()
        #print(crypto_data_list)
        if 'values' in crypto_data_list:
            berlin_tz = pytz.timezone('Europe/Berlin')
            for crypto_data in crypto_data_list['values']:
                datetime_str = crypto_data['datetime']
                crypto_datetime = datetime.strptime(datetime_str, '%Y-%m-%d %H:%M:%S')
                crypto_datetime_utc = pytz.utc.localize(crypto_datetime) 
                crypto_datetime_berlin = crypto_datetime_utc.astimezone(berlin_tz)
                
                CryptoData.objects.create(
                    symbol=symbol,
                    datetime=crypto_datetime_berlin,
                    current_price=float(crypto_data['close']),
                    open_price=float(crypto_data['open']),
                    close_price=float(crypto_data['close']),
                    high_price=float(crypto_data['high']),
                    low_price=float(crypto_data['low']),
                    percent_change=float((float(crypto_data['close']) - float(crypto_data['open'])) / float(crypto_data['open']) * 100),
                )
            print('Data successfully fetched and stored in the database.')
        else:
            print('Unexpected API response format. Missing "values" key.')
    except requests.RequestException as e:
        print(f'Error fetching data from the API: {e}')


@shared_task
def fetch_stock_data(api_key='cm0u7r1r01qk0g5fdm6gcm0u7r1r01qk0g5fdm70', symbol='AAPL', interval='1', outputsize=1):
    api_url = f"https://finnhub.io/api/v1/stock/candle?symbol={symbol}&resolution={interval}&count={outputsize}&token={api_key}"

    try:
        response = requests.get(api_url)
        stock_data = response.json()
        print(stock_data)

# #         if 'c' in stock_data:
# #             berlin_tz = pytz.timezone('Europe/Berlin')

# #             for timestamp, close_price, open_price, high_price, low_price in zip(
# #                     stock_data['t'], stock_data['c'], stock_data['o'], stock_data['h'], stock_data['l']):
# #                 stock_datetime_utc = datetime.utcfromtimestamp(timestamp)
# #                 stock_datetime_berlin = pytz.utc.localize(stock_datetime_utc).astimezone(berlin_tz)

# #                 # Use 'pc' as the previous close
# #                 previous_close = stock_data.get('pc')

# #                 # Check if close_price is not null before creating the object
# #                 if close_price is not None:
# #                     StockData.objects.create(
# #                         symbol=symbol,
# #                         datetime=stock_datetime_berlin,
# #                         current_price=float(close_price),
# #                         open_price=float(open_price),
# #                         close_price=float(close_price),
# #                         high_price=float(high_price),
# #                         low_price=float(low_price),
# #                         previous_close=float(previous_close) if previous_close is not None else None,
# #                     )
# #                 else:
# #                     print('Skipping data with null close_price.')

#         #     print('Data successfully fetched and stored in the database.')
#         # else:
        print('Unexpected API response format. Missing "c" key.')
    except requests.RequestException as e:
        print(f'Error fetching stock data from the API: {e}')
