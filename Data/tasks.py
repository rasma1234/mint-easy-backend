import requests
from datetime import datetime
from .models import ForexData 
from celery import shared_task
from datetime import datetime
from .models import ForexData
import pytz

@shared_task
def fetch_forex_data(api_key='b6e55de583394e2b97799f6a82e3156a', symbol='EUR/USD', interval='1min', outputsize=1):
    api_endpoint = f'https://api.twelvedata.com/time_series?symbol={symbol}&interval={interval}&apikey={api_key}&outputsize={outputsize}'
    try:
        response = requests.get(api_endpoint)
        forex_data_list = response.json()
        print(forex_data_list)
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



