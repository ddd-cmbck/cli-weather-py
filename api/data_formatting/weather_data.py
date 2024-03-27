class WeatherData:
    """

    Used to standardize the weather data format across different APIs.

    """

    def __init__(self):
        self.udict = {}
        self.ulist = []

    def create_cities(self, cities_list: list):
        ulist = []
        for c in cities_list:
            city = City.from_accuweather(c)
            ulist.append(city)
        return ulist

    def create_forecasts(self, forecasts_list: list):
        ulist = []
        for f in forecasts_list:
            forecast = DailyForecast.from_accuweather(f)
            ulist.append(forecast)
        return ulist

    def parse_to_list(self, forecasts_data: dict):
        forecasts_list = forecasts_data.get('DailyForecasts', 'Unknown DailyForecasts')
        return forecasts_list


class City:
    """

    Class for extracting and generalizing city data from API requested datasets

    """

    def __init__(self, key, name, country, admin_area, data_set, **kwargs):
        self.key = key
        self.name = name
        self.country = country
        self.admin_area = admin_area
        self.data_set = data_set

    def __repr__(self):
        return f'City(key={self.key}, name={self.name}' \
               f', country={self.country}, admin_area={self.admin_area})'

    @classmethod
    def from_accuweather(cls, cities_data):
        """

        Factory method for creating City instances from accu weather data format.

        """
        key = cities_data.get('Key', 'Unknown Key')
        name = cities_data.get('EnglishName', 'Unknown Name')
        country = cities_data.get('Country', {}).get('ID', 'Unknown Country ID')
        admin_area = cities_data.get('AdministrativeArea', {}).get('EnglishName', 'Unknown Admin Area')
        data_set = cities_data.get('DataSets', 'Unknown DataSet')

        return cls(key, name, country, admin_area, data_set)


class DailyForecast:
    """

    Class for extracting and generalizing forecast data from API requested datasets

    """
    def __repr__(self):
        return f'Forecast(date={self.date}, sun={self.sun}' \
               f', day={self.day}, night={self.night})'

    def __init__(self, date: dict, sun: dict, moon: dict, temperature: dict, hours_of_sun: str, day: dict, night: dict, **kwargs):
        self.date = date
        self.sun = sun
        self.moon = moon
        self.temperature = temperature
        self.hours_of_sun = hours_of_sun
        self.day = day
        self.night = night

    @classmethod
    def from_accuweather(cls, forecast_data):
        """

        Factory method for creating DailyForecast instances from accu weather data format.

        """
        date = forecast_data.get('Date', 'Unknown Date')
        sun = forecast_data.get('Sun', 'Unknown Sun Data')
        moon = forecast_data.get('Moon', 'Unknown Moon Data')
        temperature = forecast_data.get('Temperature', 'Unknown Temperature Data')
        hours_of_sun = forecast_data.get('HoursOfSun', 'Unknown HoursOfSun')
        day = forecast_data.get('Day', 'Unknown Day')
        night = forecast_data.get('Night', 'Night')

        return cls(date, sun, moon, temperature, hours_of_sun, day, night)

