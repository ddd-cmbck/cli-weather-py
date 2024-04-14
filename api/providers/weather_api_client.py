import os


class WeatherApiClient:
    """

    Defines a common interface for all weather API clients.

    """

    def get_city_request(self, *args):
        return None

    def get_forecast_request(self, *args):
        return None

    def parse_city_list(self, city_list):
        return None

    def parse_forecasts_list(self, forecasts_json):
        return None

    def set_accuweather_api_key(self, api_key):
        os.environ['ACCUWEATHER_API_KEY'] = api_key
