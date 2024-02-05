import datetime as dt
import requests

BASE_URL = 'http://dataservice.accuweather.com/forecasts/v1/daily/1day/'
CITY_CODE = '207697'
API_KEY = open('api_key.txt', 'r').read()

url = BASE_URL + CITY_CODE + '?apikey=' + API_KEY

response = requests.get(url).json()

print(response)
