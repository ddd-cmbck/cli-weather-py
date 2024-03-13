from api import WeatherApiClient
from api import OutputFormatter
from api import CommandParser


class WeatherApp:
    """

    Primary class for the WeatherCLI, directing application flow,
    managing inputs, and initializing API clients based on user preferences or defaults.

    """

    def __init__(self):
        self.api_client = WeatherApiClient()
        self.formatter = OutputFormatter()
        self.cli = CommandParser()

    def run(self):  # to do
        self.cli.parse()
        cmddict = self.cli.perform_operation()

