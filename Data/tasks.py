import requests
from datetime import datetime
from .models import ForexData 
from celery import shared_task
from datetime import datetime
from .models import ForexData, CryptoData, StockData
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
def fetch_stock_data(api_key='1ebe6bd6682f44f5bbee1c74ba7a18cc', symbol='AAPL', interval='1min', outputsize=1):
    api_endpoint = f'https://api.twelvedata.com/time_series?symbol={symbol}&interval={interval}&apikey={api_key}&outputsize={outputsize}'
    try:
        response = requests.get(api_endpoint)
        stock_data_list = response.json()
        #print(stock_data_list)
        if 'values' in stock_data_list:
            berlin_tz = pytz.timezone('Europe/Berlin')
            for stock_data in stock_data_list['values']:
                datetime_str = stock_data['datetime']
                stock_datetime = datetime.strptime(datetime_str, '%Y-%m-%d %H:%M:%S')
                stock_datetime_utc = pytz.utc.localize(stock_datetime) 
                stock_datetime_berlin = stock_datetime_utc.astimezone(berlin_tz)
                
                StockData.objects.create(
                    symbol=symbol,
                    datetime=stock_datetime_berlin,
                    current_price=float(stock_data['close']),
                    open_price=float(stock_data['open']),
                    close_price=float(stock_data['close']),
                    high_price=float(stock_data['high']),
                    low_price=float(stock_data['low']),
                    volume=float(stock_data['volume']),
                    percent_change=float((float(stock_data['close']) - float(stock_data['open'])) / float(stock_data['open']) * 100),
                )
            print('Data successfully fetched and stored in the database.')
        else:
            print('Unexpected API response format. Missing "values" key.')
    except requests.RequestException as e:
        print(f'Error fetching data from the API: {e}')