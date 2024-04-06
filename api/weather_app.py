from api import WeatherApiClient, AccuWeatherClient, WeatherData, OutputFormatter, CommandParser
from api.data_formatting.formats import DefaultFormatter, VerboseFormatter, ShortFormatter
from api.data_formatting.weather_data import City, DailyForecast, Day


class WeatherApp:
    """

    Primary class for the WeatherCLI, directing application flow,
    managing inputs, and initializing API clients based on user preferences or defaults.

    """

    def __init__(self):
        self.cli = CommandParser()
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
        # cli perform
        self.cli.parse()
        cmd_dict = self.cli.perform_operation()
        # get specific api
        api_client: WeatherApiClient = self.get_api_client(cmd_dict['source'])
        output_formatter: OutputFormatter = self.get_output_format(cmd_dict['output'])
        city_list = api_client.get_city_list(cmd_dict['city'])
        weather_data = WeatherData()
        cities = weather_data.create_cities(city_list)
        specific_city: City = cities[0]
        forecasts_data = api_client.get_forecast(specific_city.key, cmd_dict['duration'])
        forecasts_list = weather_data.parse_to_list(forecasts_data=forecasts_data)
        forecasts = weather_data.create_forecasts(forecasts_list=forecasts_list)
        specific_forecast: DailyForecast = forecasts[0]
        day_dict = specific_forecast.day
        night_dict = specific_forecast.night
        day: Day = weather_data.create_day_instance(day_night_dict=day_dict)
        night: Day = weather_data.create_day_instance(day_night_dict=night_dict)
        print(output_formatter.city_format(specific_city))
        print(output_formatter.forecast_format(specific_forecast))
        print(output_formatter.day_format(day))
        print(output_formatter.day_format(night))
