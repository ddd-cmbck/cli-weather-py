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

    def create_day_instance(self, day_night_dict):
        day = Day.from_accuweather(day_night_dict)
        return day



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
        key = cities_data.get('Key', None)
        name = cities_data.get('EnglishName', None)
        country = cities_data.get('Country', {}).get('ID', None)
        admin_area = cities_data.get('AdministrativeArea', {}).get('EnglishName', None)
        data_set = cities_data.get('DataSets', None)

        return cls(key, name, country, admin_area, data_set)


class DailyForecast:
    """

    Class for extracting and generalizing forecast data from API requested datasets

    """

    def __init__(self, date, sunrise, sunset, moonrise, moonset, temperature, hours_of_sun, day, night,
                 **kwargs):
        self.date = date
        self.sunrise = sunrise
        self.sunset = sunset
        self.moonrise = moonrise
        self.moonset = moonset
        self.temperature = temperature
        self.hours_of_sun = hours_of_sun
        self.day = day
        self.night = night

    def __repr__(self):
        return f'Forecast(date={self.date}, sunrise={self.sunrise}, sunset={self.sunset},moonrise={self.moonrise}, ' \
               f'moonset={self.moonset}, day={self.day}, night={self.night})'

    @classmethod
    def from_accuweather(cls, forecast_data: dict):
        """

        Factory method for creating DailyForecast instances from accu weather data format.

        """
        date = forecast_data.get('Date', None)
        sunrise = forecast_data['Sun'].get('Rise', None)
        sunset = forecast_data['Sun'].get('Set', None)
        moonrise = forecast_data['Moon'].get('Rise', None)
        moonset = forecast_data['Moon'].get('Set', None)
        temperature = forecast_data.get('Temperature', None)
        hours_of_sun = forecast_data.get('HoursOfSun', None)
        day = forecast_data.get('Day', None)
        night = forecast_data.get('Night', None)

        return cls(date, sunrise, sunset, moonrise, moonset, temperature, hours_of_sun, day, night)


class Day:
    """

    Class for extracting and generalizing day related data from forecast data

    """

    def __init__(self, has_precipitation, precipitation_type, precipitation_intensity, short_phrase, long_phrase,
                 precipitation_probability, thunderstorm_probability, rain_probability, snow_probability,
                 ice_probability, wind_speed_miph, wind_direction_deg, wind_gust_speed_miph, wind_gust_direction_deg,
                 total_liquid_inch, rain_inch, snow_inch, ice_inch, hours_of_precipitation, hours_of_rain,
                 hours_of_snow, hours_of_ice, cloud_cover):
        self.has_precipitation = has_precipitation
        self.precipitation_type = precipitation_type
        self.precipitation_intensity = precipitation_intensity
        self.short_phrase = short_phrase
        self.long_phrase = long_phrase
        self.precipitation_probability = precipitation_probability
        self.thunderstorm_probability = thunderstorm_probability
        self.rain_probability = rain_probability
        self.snow_probability = snow_probability
        self.ice_probability = ice_probability
        self.wind_speed_miph = wind_speed_miph
        self.wind_direction_deg = wind_direction_deg
        self.wind_gust_speed_miph = wind_gust_speed_miph
        self.wind_gust_direction_deg = wind_gust_direction_deg
        self.total_liquid_inch = total_liquid_inch
        self.rain_inch = rain_inch
        self.snow_inch = snow_inch
        self.ice_inch = ice_inch
        self.hours_of_precipitation = hours_of_precipitation
        self.hours_of_rain = hours_of_rain
        self.hours_of_snow = hours_of_snow
        self.hours_of_ice = hours_of_ice
        self.cloud_cover = cloud_cover

    def __repr__(self):
        return (f"Day(has_precipitation={self.has_precipitation}, precipitation_type={self.precipitation_type}, "
                f"precipitation_intensity={self.precipitation_intensity}, short_phrase={self.short_phrase}, "
                f"long_phrase={self.long_phrase}, precipitation_probability={self.precipitation_probability}, "
                f"thunderstorm_probability={self.thunderstorm_probability}, rain_probability={self.rain_probability}, "
                f"snow_probability={self.snow_probability}, ice_probability={self.ice_probability}, "
                f"wind_speed_miph={self.wind_speed_miph}, wind_direction_deg={self.wind_direction_deg}, "
                f"wind_gust_speed_miph={self.wind_gust_speed_miph}, wind_gust_direction_deg={self.wind_gust_direction_deg}, "
                f"total_liquid_inch={self.total_liquid_inch}, rain_inch={self.rain_inch}, snow_inch={self.snow_inch}, "
                f"ice_inch={self.ice_inch}, hours_of_precipitation={self.hours_of_precipitation}, "
                f"hours_of_rain={self.hours_of_rain}, hours_of_snow={self.hours_of_snow}, hours_of_ice={self.hours_of_ice}, "
                f"cloud_cover={self.cloud_cover}")

    @classmethod
    def from_accuweather(cls, day_data):
        """

        Factory method for creating Day/Night instances from day data format.

        """
        has_precipitation = day_data.get('HasPrecipitation', None)
        precipitation_type = day_data.get('PrecipitationType', None)
        precipitation_intensity = day_data.get('PrecipitationIntensity', None)
        short_phrase = day_data.get('ShortPhrase', None)
        long_phrase = day_data.get('LongPhrase', None)
        precipitation_probability = day_data.get('PrecipitationProbability', None)
        thunderstorm_probability = day_data.get('ThunderstormProbability', None)
        rain_probability = day_data.get('RainProbability', None)
        snow_probability = day_data.get('SnowProbability', None)
        ice_probability = day_data.get('IceProbability', None)
        wind_speed_miph = day_data['Wind']['Speed'].get('Value', None)
        wind_direction_deg = day_data['Wind']['Direction'].get('Degrees', None)
        wind_gust_speed_miph = day_data['WindGust']['Speed'].get('Value', None)
        wind_gust_direction_deg = day_data['WindGust']['Direction'].get('Degrees', None)
        total_liquid_inch = day_data['TotalLiquid'].get('Value', None)
        rain_inch = day_data['Rain'].get('Value', None)
        snow_inch = day_data['Snow'].get('Value', None)
        ice_inch = day_data['Ice'].get('Value', None)
        hours_of_precipitation = day_data.get('HoursOfPrecipitation', None)
        hours_of_rain = day_data.get('HoursOfRain', None)
        hours_of_snow = day_data.get('HoursOfSnow', None)
        hours_of_ice = day_data.get('HoursOfIce', None)
        cloud_cover = day_data.get('CloudCover', None)

        return cls(has_precipitation, precipitation_type, precipitation_intensity, short_phrase, long_phrase,
                   precipitation_probability, thunderstorm_probability, rain_probability, snow_probability,
                   ice_probability, wind_speed_miph, wind_direction_deg, wind_gust_speed_miph, wind_gust_direction_deg,
                   total_liquid_inch, rain_inch, snow_inch, ice_inch, hours_of_precipitation, hours_of_rain,
                   hours_of_snow, hours_of_ice, cloud_cover)
