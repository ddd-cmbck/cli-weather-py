from argparse import ArgumentParser, Namespace


class CommandParser:
    """

    Responsible for parsing and validating command-line arguments or user inputs
    CommandParser converts user input into a format that the WeatherApp class can use to perform actions

    """

    def __init__(self):
        # Initialize the parser
        self.args = None
        self.udict = {}
        self.parser = ArgumentParser(usage='This program takes user input in form "forecast -(additional optional '
                                           'args)" default: source AccuWeather city -> Cork, 14 days forecast, '
                                           'default output, weather, temperature, cloud cover ')
        self.setup_args()

    def setup_args(self):
        # Configuration of command line arguments
        self.parser.add_argument('command', choices=['forecast'],
                                 help='The command to run. Currently supports "forecast"')
        self.parser.add_argument('-s', '--source', type=str, default='accuweather.com',
                                 help='defines the source of the forecast')
        self.parser.add_argument('-c', '--city', type=str, default='Cork',
                                 help='defines the city of forecast')
        self.parser.add_argument('-ctr', '--country', type=str, default='Ireland',
                                 help='defines the country of forecast')  # change it in future
        self.parser.add_argument('-dur', '--duration', type=str,
                                 default='1d',
                                 help='an argument that accepts number of days/hours and str(d - days/ h - hours)'
                                 )
        self.parser.add_argument('-wS', '--wind_speed', type=bool, default=True,
                                 help='an argument that shows if user want to see average wind speed')
        self.parser.add_argument('-tmp', '--temperature', type=bool, default=True,
                                 help='an argument that shows if user want to see average temperature')
        self.parser.add_argument('-wth', '--weather', type=bool, default=True,
                                 help='an argument that shows if user want to see average type of weather')
        self.parser.add_argument('-prc', '--precipitation', type=bool, default=True,
                                 help='an argument that shows if user want to see amount of precipitation')
        self.parser.add_argument('-clCv', '--cloud_cover', type=bool, default=False,
                                 help='an argument that shows if user want to see cloud cover percentage')
        self.parser.add_argument('-prPr', '--precipitation_probability', type=bool, default=False,
                                 help='an argument that shows if user want to see probability of precipitation')
        self.parser.add_argument('-sunr', '--sunrise', type=bool, default=False,
                                 help='an argument that shows if user want to see sunrise time')
        self.parser.add_argument('-suns', '--sunset', type=bool, default=False,
                                 help='an argument that shows if user want to see sunset time')
        self.parser.add_argument('-o', '--output', choices=['default', 'verbose', 'short'], default='default',
                                 help='specifies the preferred output')

    def parse(self):
        self.args: Namespace = self.parser.parse_args()

    def perform_operation(self):
        if self.args.command == 'forecast':
            self.udict['command'] = self.args.command
            self.udict['source'] = self.args.source
            self.udict['city'] = self.args.city
            self.udict['duration'] = self.args.duration
            self.udict['wind_speed'] = self.args.wind_speed
            self.udict['temperature'] = self.args.temperature
            self.udict['weather'] = self.args.weather
            self.udict['precipitation'] = self.args.precipitation
            self.udict['cloud_cover'] = self.args.cloud_cover
            self.udict['precipitation_prob'] = self.args.precipitation_probability
            self.udict['sunrise'] = self.args.sunrise
            self.udict['sunset'] = self.args.sunset
            self.udict['output'] = self.args.output
            # print(self.udict.keys())
            # print(self.udict.values())
        else:
            self.parser.print_help()
        return self.udict
