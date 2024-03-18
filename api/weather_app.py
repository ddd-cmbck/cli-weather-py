from api import WeatherApiClient, AccuWeatherClient
from api import OutputFormatter
from api import CommandParser


class WeatherApp:
    """

    Primary class for the WeatherCLI, directing application flow,
    managing inputs, and initializing API clients based on user preferences or defaults.

    """

    def __init__(self):
        self.formatter = OutputFormatter()
        self.cli = CommandParser()

    def get_api_client(self, source):
        api_clients = {
            "accuweather.com": AccuWeatherClient,
        }

        for key in api_clients:
            if key in source:
                return api_clients[key]()

        raise ValueError(f"No API client found for source: {source}")

    def run(self):  # to do
        self.cli.parse()
        cmd_dict = self.cli.perform_operation()
        api_client = self.get_api_client(cmd_dict['source'])
        print(api_client, 'in main')
        city = api_client.get_city_list(cmd_dict['city'])
        print(city)

