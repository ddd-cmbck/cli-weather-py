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

    def convert_date(self, date: str, format: str):
        date_obj = datetime.strptime(date, '%Y-%m-%dT%H:%M:%S%z')
        formatted_date = date_obj.strftime(format)
        return formatted_date

    def city_format(self, city_obj: City):
        pass

    def forecast_format(self, forecast_obj: DailyForecast):
        pass

    def average(self, *args):
        total = 0
        count = 0

        if len(args) == 1 and isinstance(args[0], (list, tuple, set)):
            args = args[0]

        for num in args:
            if isinstance(num, (int, float)):
                total += num
                count += 1
            else:
                raise ValueError("All inputs must be numbers")

        if count == 0:
            raise ValueError("At least one number is required to calculate the average")
        return total / count


class VerboseFormatter(OutputFormatter):
    def city_format(self, city_obj: City):
        label = (f"\n\n| Admin Area ::::: {city_obj.admin_area}\n"
                 f"| Name of City ::::: {city_obj.name}\n"
                 f"| Country ::::: {city_obj.country}\n"
                 f"| Coordinates ::::: Lat {city_obj.latitude}, Lon {city_obj.longitude}\n\n")
        return label

    def forecast_format(self, forecast_obj: DailyForecast):
        return (f"Date: {self.convert_date(forecast_obj.date, format='%A, %B %d')}\n"
                f"Sunrise at: {self.convert_date(forecast_obj.sunrise, format='%H:%M')}"
                f" and Sunset at: {self.convert_date(forecast_obj.sunset, format='%H:%M')}\n"
                f"Min/Max Temperature: {forecast_obj.min_temp}°F / {forecast_obj.max_temp}°F\n"
                f"Day Precipitation: {forecast_obj.day_precip_type} at intensity {forecast_obj.day_precip_intensity}\n"
                f"Night Wind: {forecast_obj.night_wind_speed} mph towards {forecast_obj.night_wind_direction}\n")


class ShortFormatter(OutputFormatter):
    def city_format(self, city_obj: City):
        label = f'\n{city_obj.name} '
        return label

    def forecast_format(self, forecast_obj: DailyForecast):
        date = self.convert_date(forecast_obj.date, format='%m-%d')
        avrg_temp = self.average(forecast_obj.min_temp, forecast_obj.max_temp)
        phrase = 'default'
        label = f'{date}\n' \
                f'T: {avrg_temp} F\n'
        return label


class DefaultFormatter(OutputFormatter):
    def city_format(self, city_obj: City):
        label = f'{city_obj.admin_area} ::::: {city_obj.name} ::::: {city_obj.country}\n\n'
        return label

    def forecast_format(self, forecast_obj: DailyForecast):
        return (f"Date: {self.convert_date(forecast_obj.date, format='%B %d')}\n"
                f"Temp Range: {forecast_obj.min_temp}°F to {forecast_obj.max_temp}°F\n"
                f"Precipitations during the day: {forecast_obj.day_precip_type}\n")
