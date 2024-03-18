
import requests


class WeatherApiClient:
    _subclasses = []

    """

    Defines a common interface for all weather API clients.

    """

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        WeatherApiClient._subclasses.append(cls)


    def get_city_list(self, *args):
        return 'Hello'

    def get_valid_forcast_durations(self):
        pass

    def get_weather(self, city, days, units):
        pass

    @classmethod
    def append_subclasses(cls):
        return [subclass() for subclass in cls._subclasses]
