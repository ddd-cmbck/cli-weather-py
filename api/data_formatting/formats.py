class OutputFormatter:
    """

    Defines a common interface for formatting weather data into various output styles

    """

    def format(self, weather_data):
        pass

    def convert_temperature_F(self):
        pass

    def convert_temperature_C(self):
        pass

    def convert_temperature_K(self):
        pass

    def wind_speed_kmh(self):
        pass

    def wind_speed_mph(self):
        pass

    def wind_seed_meter_p_sec(self):
        pass

    def date_format_DMY(self):
        pass

    def date_format_MDY(self):
        pass

    def date_format_YMD(self):
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
