from api.functionality.weather_api_client import WeatherApiClient


class AccuWeatherClient(WeatherApiClient):  # to do
    """

    Fetch weather data from https://www.accuweather.com/
    and convert the API response into WeatherData format

    """

    def get_weather(self, city, days, units):
        pass
