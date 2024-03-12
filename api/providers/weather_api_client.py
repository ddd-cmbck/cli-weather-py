import requests


class WeatherApiClient:  # to do

    """

    Defines a common interface for all weather API clients.

    """

    def __init__(self):
        self.api_key = 'default'
        self.base_url = 'https://www.defaultbaseurl.com/'

    def get_city_list(self, *args):
        pass

    def get_valid_forcast_durations(self):
        pass

    def get_weather(self, city, days, units):
        pass
