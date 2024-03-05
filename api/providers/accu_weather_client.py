from api.providers.weather_api_client import WeatherApiClient


class AccuWeatherClient(WeatherApiClient):  # to do
    """

    Fetch weather data from https://www.accuweather.com/
    and convert the API response into WeatherData format

    """

    def get_source_response(self):
        pass

    def get_city(self):
        pass

    def get_valid_forcast_durations(self):
        pass

    def get_weather(self, city, days, units):
        pass
