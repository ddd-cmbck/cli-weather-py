from api.functionality.weather_api_client import WeatherApiClient
from api.functionality.formats import OutputFormatter


class WeatherApp:
    """

    Primary class for the WeatherCLI, directing application flow,
    managing inputs, and initializing API clients based on user preferences or defaults.

    """

    def __init__(self):
        self.api_client = WeatherApiClient()
        self.formatter = OutputFormatter()

    def run(self):  # to do
        # Main application logic for initializing clients, fetching weather, and formatting output
        pass
