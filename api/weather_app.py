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

    def call_source(self, source_domain: str) -> None:
        source_list: list = ['accuweather.com', 'corkweather.com', 'myweather.com']
        try:
            if source_domain not in source_list:
                raise ValueError('non existing source')

            for i in range(0, len(source_list)):
                if source_domain == source_list[i]:  # wait for source response
                    # initialize the WetherAPIClient but use the same class as source_domain
                    print(source_list[i])
                    print(type(source_list), type(source_domain))  # to do
        except ValueError:
            print(f'please, provide existing source. Available sources: {source_list}')

    def call_city(self, city_name: str, country_name: str):
        try:
            if type(city_name) != str and type(country_name) != str:
                raise ValueError('must be str')
            # Sends city info to api
        except ValueError:
            print('Please, input can only be of a type string')

    def call_time_duration(self, values):
        print('Checking possible variants ')  # adds time duration for the api url

    def call_forecast(self):
        print('I am calling forecast')

    def run(self):  # to do
        self.cli.parse()
        self.cli.perform_operation()
