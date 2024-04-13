from api.data_formatting.weather_data import City, DailyForecast

from datetime import datetime


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

    def convert_date(self, date_str):
        pass

    def city_format(self, city_obj: City):
        pass

    def forecast_format(self, forecast_obj: DailyForecast):
        pass


class VerboseFormatter(OutputFormatter):
    def city_format(self, city_obj: City):
        label = f'| Admin Area ::::: {city_obj.admin_area}\n' \
                f'| Name of City ::::: {city_obj.name}\n' \
                f'| Country ::::: {city_obj.country}, {city_obj.country}\n\n'
        return label

    def forecast_format(self, forecast_obj: DailyForecast):
        print(forecast_obj)

    def convert_date(self, date_str):
        date_obj = datetime.strptime(date_str, '%Y-%m-%dT%H:%M:%S%z')
        formatted_date = date_obj.strftime('%A, %B %d')
        return formatted_date


class ShortFormatter(OutputFormatter):
    def city_format(self, city_obj: City):
        label = f'\n{city_obj.name}, {city_obj.city_id}\n\n'
        return label

    def forecast_format(self, forecast_obj: DailyForecast):
        label = f'bla..bla'
        return label

    def convert_date(self, date_str):
        date_obj = datetime.strptime(date_str, '%Y-%m-%dT%H:%M:%S%z')
        formatted_date = date_obj.strftime('%m-%d')
        return formatted_date


class DefaultFormatter(OutputFormatter):
    def city_format(self, city_obj: City):
        label = f'{city_obj.admin_area} ::::: {city_obj.name} ::::: {city_obj.country}\n\n'
        return label

    def forecast_format(self, forecast_obj: DailyForecast):
        print(forecast_obj)

    def convert_date(self, date_str):
        date_obj = datetime.strptime(date_str, '%Y-%m-%dT%H:%M:%S%z')
        formatted_date = date_obj.strftime('%B %d')
        return formatted_date
