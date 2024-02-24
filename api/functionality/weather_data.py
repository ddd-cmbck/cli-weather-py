class WeatherData:
    """

    Used to standardize the weather data format across different APIs.

    """

    def __init__(self, temperature, wind, humidity, time):
        self.temperature = temperature
        self.wind = wind
        self.humidity = humidity
        self.time = time
