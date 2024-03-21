import requests

from api.providers.weather_api_client import WeatherApiClient


class AccuWeatherClient(WeatherApiClient):  # to do
    """

    Fetch weather data from https://www.accuweather.com/
    and convert the API response into WeatherData format

    """

    def __init__(self):
        self.api_key = 'EQwGZb1GUqPiFCx66wG5TU6cvLrnTaJh'
        self.base_url = 'https://dataservice.accuweather.com/'

    def get_city_list(self, location_name: str):
        params = {
            'apikey': self.api_key,
            'location': location_name,
            'url_descript': 'locations/v1/cities/search?'
        }
        url = self.base_url + params['url_descript'] + 'apikey=' + params['apikey'] + '&q=' + params['location']
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            print('Failed to retrieve data')
            return None

    def get_forecast(self, city_key: str, duration: str):
        params = {
            'apikey': self.api_key,
            'citykey': city_key,
            'url_descript': 'forecasts/v1/daily/',
            'duration': duration,
            'details': '&details=true'
        }
        url = self.base_url + params['url_descript'] + duration + '/' + city_key + '?' + 'apikey=' + params['apikey'] + params['details']
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            print('Failed to retrieve data')
            return None
