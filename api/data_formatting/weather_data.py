class WeatherData:
    """

    Used to standardize the weather data format across different APIs.

    """

    def __init__(self):
        self.udict = {}
        self.ulist = []

    def create_cities(self, cities_list: list):
        for c in cities_list:
            city = City.from_accuweather(c)
            self.ulist.append(city)
        return self.ulist


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


class Forecast:
    """

    Class for extracting and generalizing forecast data from API requested datasets

    """

    def __init__(self, source, duration):
        self.source = source
        self.duration = duration
