class OutputFormatter:
    """

    Defines a common interface for formatting weather data into various output styles

    """
    def format(self, weather_data):
        pass


class VerboseFormatter(OutputFormatter):
    def format(self, weather_data):
        # Implementation for verbose format
        pass


class ShortFormatter(OutputFormatter):
    def format(self, weather_data):
        # Implementation for short format
        pass


class DefaultFormatter(OutputFormatter):
    def format(self, weather_data):
        # Implementation for default format
        pass
