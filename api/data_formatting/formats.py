from api.data_formatting.weather_data import City, DailyForecast, Day

import datetime


class OutputFormatter:
    """

    Defines a common interface for formatting weather data into various output styles

    """
    sunny = """
       \    /   
        .--.    
    -- (    ) -- 
        `--’    
       /    \   
    """

    moon = """
         .-`
       :` ;  
      (  (    
       :  ;
         `-.              
    """
    # Moon with Clouds
    moon_with_clouds = """
         .-`
       :` ;   .--.
      (  (  (     ).  
       :  ;(___.__)__)   
         `-. 
    """

    # Sunny with Clouds
    sunny_with_clouds = """
       \    /   
        .--.     .--.
     - (    )--(     ).
        `--’ (___.__)__)
       /    \    
    """
    # Clouds
    clouds = """
          .--.
      .-(     ). 
     (___.__)___)
    """

    # Clouds with Rain
    clouds_with_rain = """
          .--.    
      .-(     ).   
     (___.__)___) 
        ` ` ` `    
        ` ` ` `    
    """

    # Clouds with Snow
    clouds_with_snow = """
          .--.
      .-(     ). 
     (___.__)___)
        *  *  * 
        *  *  * 
    """

    # Clouds with Ice
    clouds_with_ice = """
          .--.
      .-(     ). 
     (___.__)___)
        *  *  * 
       *  ICE  * 
    """

    # Grouping the ASCII art in a dictionary for easy access
    ascii_art_icons = {
        "Sunny": sunny,
        "SunnyWithClouds": sunny_with_clouds,
        "Clouds": clouds,
        "CloudsWithRain": clouds_with_rain,
        "CloudsWithSnow": clouds_with_snow,
        "CloudsWithIce": clouds_with_ice,
    }

    def print_output(self):
        pass

    def city_format(self, city_obj: City):
        pass

    def forecast_format(self, forecast_obj: DailyForecast):
        pass

    def day_format(self, day_obj: Day):
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
    def city_format(self, city_obj: City):
        label = f'| Admin Area ::::: {city_obj.admin_area}\n' \
                f'| Name of City ::::: {city_obj.name}\n' \
                f'| Country ::::: {city_obj.country}, {city_obj.country_id}\n\n'
        return label

    def forecast_format(self, forecast_obj: DailyForecast):
        print(forecast_obj)

    def day_format(self, day_obj: Day):
        print(day_obj)


class ShortFormatter(OutputFormatter):
    def city_format(self, city_obj: City):
        label = f'\n{city_obj.name}, {city_obj.key}\n\n'
        return label

    def forecast_format(self, forecast_obj: DailyForecast):
        label = 'March 12 12:33\n' \
                'Sunrise at 5:34\n' \
                'Temperature\n' \
                'Max: 12 deg, avrg: 10 deg, min: 8 deg\n\n'
        return label

    def day_format(self, day_obj: Day):
        label = 'Very windy; Morning Showers\n' \
                'Precipitation: Rain\n' \
                'Intensity: Light\n' \
                'wind speed: 32 km/h\n\n'
        return label


class DefaultFormatter(OutputFormatter):
    def city_format(self, city_obj: City):
        label = f'{city_obj.admin_area} ::::: {city_obj.name} ::::: {city_obj.country}\n\n'
        return label

    def forecast_format(self, forecast_obj: DailyForecast):
        print(forecast_obj)

    def day_format(self, day_obj: Day):
        print(day_obj)
