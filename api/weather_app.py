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

    def cli_setup(self):
        user_args = 0
        cli = CommandParser()
        cli.parse()
        cli.perform_operation()

    def run(self):  # to do
        self.cli_setup()
