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

    def get_valid_forcast_durations(self):
        pass

    def get_weather(self, city, days, units):
        pass

