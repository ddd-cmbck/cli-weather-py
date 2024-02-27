from argparse import ArgumentParser, Namespace


class CommandParser:
    """

    Responsible for parsing and validating command-line arguments or user inputs
    CommandParser converts user input into a format that the WeatherApp class can use to perform actions

    """

    def __init__(self):
        # Initialize the parser
        self.args = None
        self.parser = ArgumentParser(usage='This program takes user input in form "forecast -(additional args)"'
                                           'default: AccuWeather city -> Cork, 14 days forecast, default output,'
                                           'weather, temperature, cloud cover ')
        self.setup_args()

    def setup_args(self):
        # Configuration of command line arguments
        self.parser.add_argument('forecast', action='store_true',
                                 help='main command that returns true and runs our forecast ')
        self.parser.add_argument('--source', type=str, default='accuweather.com',
                                 help='defines the source of the forecast')
        self.parser.add_argument('-c', '--city', type=str, default='Cork, Ireland',
                                 help='defines the city of forecast')
        self.parser.add_argument('-dur', '--duration', nargs=2, type=str, default=(1, 'd'),
                                 help='an argument that accepts number of days/hours and str(d - days/ h - hours)',
                                 metavar=('INT', 'STR'))
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

    def parse(self):
        self.args: Namespace = self.parser.parse_args()

    def perform_operation(self):
        print(self.args.forecast)
