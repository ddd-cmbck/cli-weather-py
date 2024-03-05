class WeatherData:
    """

    Used to standardize the weather data format across different APIs.

    """

    def __init__(self, temperature, wind, humidity, time):
        self.temperature = temperature
        self.wind = wind
        self.humidity = humidity
        self.time = time

    def convert_temperature_F(self):
        pass

    def convert_temperature_C(self):
        pass

    def convert_temperature_K(self):
        pass

    def min_unit(self):
        pass

    def max_unit(self):
        pass

    def average_unit(self):
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
