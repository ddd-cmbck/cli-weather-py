import http.client
import json


class WeatherApiClient:  # to do

    """

    Defines a common interface for all weather API clients.

    """

    def __init__(self):
        self.host = 'default.com'

    def get_source_response(self):
        conn = http.client.HTTPSConnection(self.host)
        conn.request('GET', '/')
        resp = conn.getresponse()
        data = resp.read().decode()
        conn.close()
        return json.loads(data)

    def get_city(self):
        pass

    def get_valid_forcast_durations(self):
        pass

    def get_weather(self, city, days, units):
        pass
