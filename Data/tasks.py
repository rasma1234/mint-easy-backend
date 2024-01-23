import requests
from datetime import datetime
from .models import ForexData 
from celery import shared_task
from datetime import datetime
from .models import ForexData, CryptoData, StockData, StockData_15min, ForexData_15min, CryptoData_15min
import pytz
from dotenv import load_dotenv
from decouple import config


@shared_task
def fetch_forex_data(api_key=config("API_KEY"), symbol='EUR/USD', interval='1min', outputsize=1):
    api_endpoint = f'https://api.twelvedata.com/time_series?symbol={symbol}&interval={interval}&apikey={api_key}&outputsize={outputsize}'
    try:
        response = requests.get(api_endpoint)
        forex_data_list = response.json()
        
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
def fetch_forex_data1(api_key=config("API_KEY"), symbol='USD/CAD', interval='1min', outputsize=1):
    api_endpoint = f'https://api.twelvedata.com/time_series?symbol={symbol}&interval={interval}&apikey={api_key}&outputsize={outputsize}'
    try:
        response = requests.get(api_endpoint)
        forex_data_list = response.json()
        
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
def fetch_forex_data2(api_key=config("API_KEY"), symbol='USD/JPY', interval='1min', outputsize=1):
    api_endpoint = f'https://api.twelvedata.com/time_series?symbol={symbol}&interval={interval}&apikey={api_key}&outputsize={outputsize}'
    try:
        response = requests.get(api_endpoint)
        forex_data_list = response.json()
        
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
def fetch_forex_data3(api_key=config("API_KEY"), symbol='USD/CHF', interval='1min', outputsize=1):
    api_endpoint = f'https://api.twelvedata.com/time_series?symbol={symbol}&interval={interval}&apikey={api_key}&outputsize={outputsize}'
    try:
        response = requests.get(api_endpoint)
        forex_data_list = response.json()
        
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
def fetch_forex_data4(api_key=config("API_KEY"), symbol='GBP/USD', interval='1min', outputsize=1):
    api_endpoint = f'https://api.twelvedata.com/time_series?symbol={symbol}&interval={interval}&apikey={api_key}&outputsize={outputsize}'
    try:
        response = requests.get(api_endpoint)
        forex_data_list = response.json()
        
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
def fetch_crypto_data(api_key=config("API_KEY"), symbol='BTC/USD', interval='1min', outputsize=1):
    api_endpoint = f'https://api.twelvedata.com/time_series?symbol={symbol}&interval={interval}&apikey={api_key}&outputsize={outputsize}'
    try:
        response = requests.get(api_endpoint)
        crypto_data_list = response.json()
        
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
def fetch_crypto_data1(api_key=config("API_KEY"), symbol='ETH/USD', interval='1min', outputsize=1):
    api_endpoint = f'https://api.twelvedata.com/time_series?symbol={symbol}&interval={interval}&apikey={api_key}&outputsize={outputsize}'
    try:
        response = requests.get(api_endpoint)
        crypto_data_list = response.json()
        
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
def fetch_stock_data(api_key=config("API_KEY"), symbol='AAPL', interval='1min', outputsize=1):
    api_endpoint = f'https://api.twelvedata.com/time_series?symbol={symbol}&interval={interval}&apikey={api_key}&outputsize={outputsize}'
    try:
        response = requests.get(api_endpoint)
        stock_data_list = response.json()
        
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


@shared_task
def fetch_stock_data1(api_key=config("API_KEY"), symbol='TSLA', interval='1min', outputsize=1):
    api_endpoint = f'https://api.twelvedata.com/time_series?symbol={symbol}&interval={interval}&apikey={api_key}&outputsize={outputsize}'
    try:
        response = requests.get(api_endpoint)
        stock_data_list = response.json()
        
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


@shared_task
def fetch_stock_data2(api_key=config("API_KEY"), symbol='AMZN', interval='1min', outputsize=1):
    api_endpoint = f'https://api.twelvedata.com/time_series?symbol={symbol}&interval={interval}&apikey={api_key}&outputsize={outputsize}'
    try:
        response = requests.get(api_endpoint)
        stock_data_list = response.json()
        
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



@shared_task
def fetch_stock_data3(api_key=config("API_KEY"), symbol='MSFT', interval='1min', outputsize=1):
    api_endpoint = f'https://api.twelvedata.com/time_series?symbol={symbol}&interval={interval}&apikey={api_key}&outputsize={outputsize}'
    try:
        response = requests.get(api_endpoint)
        stock_data_list = response.json()
        
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



@shared_task
def fetch_stock_data4(api_key=config("API_KEY"), symbol='JPM', interval='1min', outputsize=1):
    api_endpoint = f'https://api.twelvedata.com/time_series?symbol={symbol}&interval={interval}&apikey={api_key}&outputsize={outputsize}'
    try:
        response = requests.get(api_endpoint)
        stock_data_list = response.json()
        
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


@shared_task
def fetch_forex_data_15(api_key=config("API_KEY"), symbol='EUR/USD', interval='15min', outputsize=1):
    api_endpoint = f'https://api.twelvedata.com/time_series?symbol={symbol}&interval={interval}&apikey={api_key}&outputsize={outputsize}'
    try:
        response = requests.get(api_endpoint)
        forex_data_list = response.json()
        
        if 'values' in forex_data_list:
            berlin_tz = pytz.timezone('Europe/Berlin')
            for forex_data in forex_data_list['values']:
                
                ForexData_15min.objects.create(
                    symbol=symbol,
                    datetime=str(forex_data['datetime']),
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
def fetch_forex_data1_15(api_key=config("API_KEY"), symbol='USD/CAD', interval='15min', outputsize=1):
    api_endpoint = f'https://api.twelvedata.com/time_series?symbol={symbol}&interval={interval}&apikey={api_key}&outputsize={outputsize}'
    try:
        response = requests.get(api_endpoint)
        forex_data_list = response.json()

        if 'values' in forex_data_list:
            berlin_tz = pytz.timezone('Europe/Berlin')
            for forex_data in forex_data_list['values']:
                
                ForexData_15min.objects.create(
                    symbol=symbol,
                    datetime=str(forex_data['datetime']),
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
def fetch_forex_data2_15(api_key=config("API_KEY"), symbol='USD/JPY', interval='15min', outputsize=1):
    api_endpoint = f'https://api.twelvedata.com/time_series?symbol={symbol}&interval={interval}&apikey={api_key}&outputsize={outputsize}'
    try:
        response = requests.get(api_endpoint)
        forex_data_list = response.json()

        if 'values' in forex_data_list:
            berlin_tz = pytz.timezone('Europe/Berlin')
            for forex_data in forex_data_list['values']:
                
                
                ForexData_15min.objects.create(
                    symbol=symbol,
                    datetime=str(forex_data['datetime']),
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
def fetch_forex_data3_15(api_key=config("API_KEY"), symbol='USD/CHF', interval='15min', outputsize=1):
    api_endpoint = f'https://api.twelvedata.com/time_series?symbol={symbol}&interval={interval}&apikey={api_key}&outputsize={outputsize}'
    try:
        response = requests.get(api_endpoint)
        forex_data_list = response.json()

        if 'values' in forex_data_list:
            berlin_tz = pytz.timezone('Europe/Berlin')
            for forex_data in forex_data_list['values']:
                
                ForexData_15min.objects.create(
                    symbol=symbol,
                    datetime=str(forex_data['datetime']),
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
def fetch_forex_data4_15(api_key=config("API_KEY"), symbol='GBP/USD', interval='15min', outputsize=1):
    api_endpoint = f'https://api.twelvedata.com/time_series?symbol={symbol}&interval={interval}&apikey={api_key}&outputsize={outputsize}'
    try:
        response = requests.get(api_endpoint)
        forex_data_list = response.json()
        
        if 'values' in forex_data_list:
            berlin_tz = pytz.timezone('Europe/Berlin')
            for forex_data in forex_data_list['values']:
                
                ForexData_15min.objects.create(
                    symbol=symbol,
                    datetime=str(forex_data['datetime']),
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
def fetch_crypto_data_15(api_key=config("API_KEY"), symbol='BTC/USD', interval='15min', outputsize=1):
    api_endpoint = f'https://api.twelvedata.com/time_series?symbol={symbol}&interval={interval}&apikey={api_key}&outputsize={outputsize}'
    try:
        response = requests.get(api_endpoint)
        crypto_data_list = response.json()
        
        if 'values' in crypto_data_list:
            berlin_tz = pytz.timezone('Europe/Berlin')
            for crypto_data in crypto_data_list['values']:
                
                
                CryptoData_15min.objects.create(
                    symbol=symbol,
                    datetime=str(crypto_data['datetime']),
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
def fetch_crypto_data1_15(api_key=config("API_KEY"), symbol='ETH/USD', interval='15min', outputsize=1):
    api_endpoint = f'https://api.twelvedata.com/time_series?symbol={symbol}&interval={interval}&apikey={api_key}&outputsize={outputsize}'
    try:
        response = requests.get(api_endpoint)
        crypto_data_list = response.json()
        
        if 'values' in crypto_data_list:
            berlin_tz = pytz.timezone('Europe/Berlin')
            for crypto_data in crypto_data_list['values']:
             
                
                CryptoData_15min.objects.create(
                    symbol=symbol,
                    datetime=str(crypto_data['datetime']),
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
def fetch_stock_data_15(api_key=config("API_KEY"), symbol='AAPL', interval='15min', outputsize=1):
    api_endpoint = f'https://api.twelvedata.com/time_series?symbol={symbol}&interval={interval}&apikey={api_key}&outputsize={outputsize}'
    try:
        response = requests.get(api_endpoint)
        stock_data_list = response.json()
    
        if 'values' in stock_data_list:
            berlin_tz = pytz.timezone('Europe/Berlin')
            for stock_data in stock_data_list['values']:
               
                
                StockData_15min.objects.create(
                    symbol=symbol,
                    datetime=str(stock_data['datetime']),
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


@shared_task
def fetch_stock_data1_15(api_key=config("API_KEY"), symbol='TSLA', interval='15min', outputsize=1):
    api_endpoint = f'https://api.twelvedata.com/time_series?symbol={symbol}&interval={interval}&apikey={api_key}&outputsize={outputsize}'
    try:
        response = requests.get(api_endpoint)
        stock_data_list = response.json()
        
        if 'values' in stock_data_list:
            berlin_tz = pytz.timezone('Europe/Berlin')
            for stock_data in stock_data_list['values']:
                
                
                StockData_15min.objects.create(
                    symbol=symbol,
                    datetime=str(stock_data['datetime']),
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


@shared_task
def fetch_stock_data2_15(api_key=config("API_KEY"), symbol='AMZN', interval='15min', outputsize=1):
    api_endpoint = f'https://api.twelvedata.com/time_series?symbol={symbol}&interval={interval}&apikey={api_key}&outputsize={outputsize}'
    try:
        response = requests.get(api_endpoint)
        stock_data_list = response.json()
        
        if 'values' in stock_data_list:
            berlin_tz = pytz.timezone('Europe/Berlin')
            for stock_data in stock_data_list['values']:
               
                
                StockData_15min.objects.create(
                    symbol=symbol,
                    datetime=str(stock_data['datetime']),
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



@shared_task
def fetch_stock_data3_15(api_key=config("API_KEY"), symbol='MSFT', interval='15min', outputsize=1):
    api_endpoint = f'https://api.twelvedata.com/time_series?symbol={symbol}&interval={interval}&apikey={api_key}&outputsize={outputsize}'
    try:
        response = requests.get(api_endpoint)
        stock_data_list = response.json()
        if 'values' in stock_data_list:
            berlin_tz = pytz.timezone('Europe/Berlin')
            for stock_data in stock_data_list['values']:
                
                StockData_15min.objects.create(
                    symbol=symbol,
                    datetime=str(stock_data['datetime']),
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



@shared_task
def fetch_stock_data4_15(api_key=config("API_KEY"), symbol='JPM', interval='15min', outputsize=1):
    api_endpoint = f'https://api.twelvedata.com/time_series?symbol={symbol}&interval={interval}&apikey={api_key}&outputsize={outputsize}'
    try:
        response = requests.get(api_endpoint)
        stock_data_list = response.json()

        if 'values' in stock_data_list:
            berlin_tz = pytz.timezone('Europe/Berlin')
            for stock_data in stock_data_list['values']:
                
                
                StockData_15min.objects.create(
                    symbol=symbol,
                    datetime=str(stock_data['datetime']),
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



