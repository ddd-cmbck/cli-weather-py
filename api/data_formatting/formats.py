from api.data_formatting.weather_data import City, DailyForecast, Day


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
        # Implementation for verbose format
        pass

    def forecast_format(self, forecast_obj: DailyForecast):
        pass

    def day_format(self, day_obj: Day):
        pass


class ShortFormatter(OutputFormatter):
    def city_format(self, city_obj: City):
        # Implementation for verbose format
        pass

    def forecast_format(self, forecast_obj: DailyForecast):
        pass

    def day_format(self, day_obj: Day):
        pass


class DefaultFormatter(OutputFormatter):
    def city_format(self, city_obj: City):
        # Implementation for verbose format
        pass

    def forecast_format(self, forecast_obj: DailyForecast):
        pass

    def day_format(self, day_obj: Day):
        pass
