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
        date = forecast_data.get('Date', 'Unknown Date')
        sunrise = forecast_data['Sun'].get('Rise', 'Unknown Sun Data')
        sunset = forecast_data['Sun'].get('Set', 'Unknown Sun Data')
        moonrise = forecast_data['Moon'].get('Rise', 'Unknown Moon Data')
        moonset = forecast_data['Moon'].get('Set', 'Unknown Moon Data')
        temperature = forecast_data.get('Temperature', 'Unknown Temperature Data')
        hours_of_sun = forecast_data.get('HoursOfSun', 'Unknown HoursOfSun')
        day = forecast_data.get('Day', 'Unknown Day')
        night = forecast_data.get('Night', 'Night')

        return cls(date, sunrise, sunset, moonrise, moonset, temperature, hours_of_sun, day, night)


class Day:
    """

    Class for extracting and generalizing day related data from forecast data

    """

    def __init__(self, has_precipitation, precipitation_type, precipitation_intensity, short_phrase, long_phrase,
                 precipitation_probability, thunderstorm_probability, rain_probability, snow_probability,
                 ice_probability, wind_speed_miph, wind_direction_deg, wind_gust_speed_miph, wind_gust_direction_deg,
                 total_liquid_inch, rain_inch, snow_inch, ice_inch, hours_of_precipitation, hours_of_rain,
                 hours_of_snow, hours_of_ice, cloud_cover, min_temperature_f, max_temperature_f, avrg_temperature_f):
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
        self.min_temperature_f = min_temperature_f
        self.max_temperature_f = max_temperature_f
        self.avrg_temperature_f = avrg_temperature_f

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
                f"cloud_cover={self.cloud_cover}, min_temperature_f={self.min_temperature_f}, "
                f"max_temperature_f={self.max_temperature_f}, avrg_temperature_f={self.avrg_temperature_f})")

    @classmethod
    def from_accuweather(cls, day_data):
        """

        Factory method for creating Day/Night instances from day data format.

        """
        has_precipitation = day_data.get('HasPrecipitation', 'Unknown HasPrecipitation')
        precipitation_type = day_data.get('PrecipitationType', 'Unknown PrecipitationType')
        precipitation_intensity = day_data.get('PrecipitationIntensity', 'Unknown PrecipitationIntensity')
        short_phrase = day_data.get('ShortPhrase', 'Unknown ShortPhrase')
        long_phrase = day_data.get('LongPhrase', 'Unknown LongPhrase')
        precipitation_probability = day_data.get('PrecipitationProbability', 'Unknown PrecipitationProbability')
        thunderstorm_probability = day_data.get('ThunderstormProbability', 'Unknown ThunderstormProbability')
        rain_probability = day_data.get('RainProbability', 'Unknown RainProbability')
        snow_probability = day_data.get('SnowProbability', 'Unknown SnowProbability')
        ice_probability = day_data.get('IceProbability', 'Unknown IceProbability')
        wind_speed_miph = day_data['Wind']['Speed'].get('Value', 'Unknown Wind Speed')
        wind_direction_deg = day_data['Wind']['Direction'].get('Degrees', 'Unknown Wind Direction')
        wind_gust_speed_miph = day_data['WindGust']['Speed'].get('Value', 'Unknown Wind Gust Speed')
        wind_gust_direction_deg = day_data['WindGust']['Direction'].get('Degrees', 'Unknown Wind Gust Direction')
        total_liquid_inch = day_data['TotalLiquid'].get('Value', 'Unknown Total Liquid')
        rain_inch = day_data['Rain'].get('Value', 'Unknown Rain Inch')
        snow_inch = day_data['Snow'].get('Value', 'Unknown Snow Inch')
        ice_inch = day_data['Ice'].get('Value', 'Unknown Ice Inch')
        hours_of_precipitation = day_data.get('HoursOfPrecipitation', 'Unknown Hours Of Precipitation')
        hours_of_rain = day_data.get('HoursOfRain', 'Unknown Hours Of Rain')
        hours_of_snow = day_data.get('HoursOfSnow', 'Unknown Hours Of Snow')
        hours_of_ice = day_data.get('HoursOfIce', 'Unknown Hours Of Ice')
        cloud_cover = day_data.get('CloudCover', 'Unknown Cloud Cover')
        min_temperature_f = day_data['WetBulbTemperature']['Minimum'].get('Value', 'Unknown Min Temperature')
        max_temperature_f = day_data['WetBulbTemperature']['Maximum'].get('Value', 'Unknown Max Temperature')
        avrg_temperature_f = day_data['WetBulbTemperature']['Average'].get('Value', 'Unknown Average Temperature')

        return cls(has_precipitation, precipitation_type, precipitation_intensity, short_phrase, long_phrase,
                   precipitation_probability, thunderstorm_probability, rain_probability, snow_probability,
                   ice_probability, wind_speed_miph, wind_direction_deg, wind_gust_speed_miph, wind_gust_direction_deg,
                   total_liquid_inch, rain_inch, snow_inch, ice_inch, hours_of_precipitation, hours_of_rain,
                   hours_of_snow, hours_of_ice, cloud_cover, min_temperature_f, max_temperature_f, avrg_temperature_f)
