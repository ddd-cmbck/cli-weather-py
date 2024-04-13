import datetime

import requests


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

    def convert_iso_date_format(self, date_str):
        return None

