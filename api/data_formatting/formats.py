class OutputFormatter:
    """

    Defines a common interface for formatting weather data into various output styles

    """
    sunny = """
       \    /   
        .--.    
     - (    ) - 
        `--’    
       /    \   
    """

    # Sunny with Clouds
    sunny_with_clouds = """
       \    /   
        .--.     .--.
     - (    )--(    ).
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

    # Clouds with Ice (using a crystal-like symbol to represent ice)
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

    def format(self, weather_data):
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
    def format(self, weather_data):
        # Implementation for verbose format
        pass


class ShortFormatter(OutputFormatter):
    def format(self, weather_data):
        # Implementation for short format
        pass


class DefaultFormatter(OutputFormatter):
    def format(self, weather_data):
        # Implementation for default format
        pass
