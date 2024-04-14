from api import WeatherApiClient, AccuWeatherClient, WeatherData, OutputFormatter, CommandParser
from api.data_formatting.formats import DefaultFormatter, VerboseFormatter, ShortFormatter
from api.data_formatting.weather_data import City, DailyForecast


class WeatherApp:
    """

    Primary class for the WeatherCLI, directing application flow,
    managing inputs, and initializing API clients based on user preferences or defaults.

    """

    def __init__(self):
        self.cli = CommandParser()
        self.weather_data = WeatherData()
        self.api_clients = {
            "accuweather.com": AccuWeatherClient,
        }
        self.formats = {
            "default": DefaultFormatter,
            "verbose": VerboseFormatter,
            "short": ShortFormatter
        }

    def get_api_client(self, source):

        for key in self.api_clients:
            if key in source:
                return self.api_clients[key]()

        raise ValueError(f"No API client found for source: {source}")

    def get_output_format(self, output):

        for key in self.formats:
            if key in output:
                return self.formats[key]()
        raise ValueError(f'Not supported output format: {output}')

    def run(self):  # to do
        # CLI command processing
        self.cli.parse()
        cmd_dict = self.cli.perform_operation()

        # API client selection based on source
        api_client: WeatherApiClient = self.get_api_client(cmd_dict['source'])

        # Output formatter selection based on desired output type
        output_formatter: OutputFormatter = self.get_output_format(cmd_dict['output'])

        # City data retrieval and processing
        city_json = api_client.get_city_request(cmd_dict['city'])
        city_list = api_client.parse_city_list(city_json)
        cities = self.weather_data.parse_to_objects(city_list)
        specific_city: City = self.weather_data.choose_item(cities)

        # Weather forecast retrieval and processing
        forecasts_json = api_client.get_forecast_request(specific_city.city_id, cmd_dict['duration'])
        forecasts_list = api_client.parse_forecasts_list(forecasts_json)
        forecasts = self.weather_data.parse_forecasts(forecasts_list)
        specific_forecast: DailyForecast = forecasts[0]

        print(output_formatter.city_format(specific_city))
        print(output_formatter.forecast_format(specific_forecast))
