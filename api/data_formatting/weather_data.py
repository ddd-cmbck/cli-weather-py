class WeatherData:
    """

    Used to standardize the weather data format across different APIs.

    """

    def __init__(self):
        self.udict = {}
        self.ulist = []

    def parse_to_objects(self, cities_list: list):
        ulist = []
        for c in cities_list:
            city_name = c.get('name')
            city_id = c.get('city_id')
            admin_area = c.get('admin_area')
            country = c.get('country')
            longitude = c.get('longitude')
            latitude = c.get('latitude')
            city = City(city_id=city_id, name=city_name, admin_area=admin_area,
                        country=country, longitude=longitude, latitude=latitude)
            ulist.append(city)
        return ulist

    def parse_forecasts(self, forecasts_list: list):
        ulist = []
        for f in forecasts_list:
            # Extracting fields
            date = f.get('date')
            sunrise = f.get('sunrise')
            sunset = f.get('sunset')
            moonrise = f.get('moonrise')
            moonset = f.get('moonset')
            min_temp = f.get('min_temp')
            max_temp = f.get('max_temp')
            min_real_feel_temp = f.get('min_real_feel_temp')
            max_real_feel_temp = f.get('max_real_feel_temp')
            day_has_precipitations = f.get('day_has_precipitations')
            day_precip_type = f.get('day_precip_type')
            day_precip_intensity = f.get('day_precip_intensity')
            day_wind_speed = f.get('day_wind_speed')
            day_wind_direction = f.get('day_wind_direction')
            night_has_precipitations = f.get('night_has_precipitations')
            night_precip_type = f.get('night_precip_type')
            night_precip_intensity = f.get('night_precip_intensity')
            night_wind_speed = f.get('night_wind_speed')
            night_wind_direction = f.get('night_wind_direction')

            forecast = DailyForecast(date, sunrise, sunset, moonrise, moonset, min_temp, max_temp, min_real_feel_temp,
                                     max_real_feel_temp, day_has_precipitations, day_precip_type, day_precip_intensity,
                                     day_wind_speed, day_wind_direction, night_has_precipitations, night_precip_type,
                                     night_precip_intensity, night_wind_speed, night_wind_direction)
            ulist.append(forecast)
        return ulist

    def choose_item(self, items: list):
        for index, item in enumerate(items, start=1):
            print(f"{index}. {item}")

        while True:
            try:
                choice = int(input("Enter the number of your choice: "))
                if 1 <= choice <= len(items):
                    selected_item = items[choice - 1]
                    print(f"You have chosen {selected_item}.")
                    return selected_item
                else:
                    print("Invalid choice, please choose a valid number.")
            except ValueError:
                print("Please enter a numeric value.")


class City:
    """
    Class for extracting and generalizing city data from API requested datasets.
    """

    def __init__(self, city_id: int, name: str, admin_area: str, country: str, latitude: float, longitude: float):
        self.city_id = city_id
        self.name = name
        self.country = country
        self.admin_area = admin_area
        self.latitude = latitude
        self.longitude = longitude

    def __str__(self):
        return f'{self.name}, {self.admin_area}, {self.country}'


class DailyForecast:
    """

    Class for extracting and generalizing forecast data from API requested datasets

    """

    def __init__(self, date, sunrise, sunset, moonrise, moonset, min_temp, max_temp, min_real_feel_temp,
                 max_real_feel_temp, day_has_precipitations, day_precip_type, day_precip_intensity, day_wind_speed,
                 day_wind_direction, night_has_precipitations, night_precip_type, night_precip_intensity,
                 night_wind_speed, night_wind_direction):
        self.date = date
        self.sunrise = sunrise
        self.sunset = sunset
        self.moonrise = moonrise
        self.moonset = moonset
        self.min_temp = min_temp
        self.max_temp = max_temp
        self.min_real_feel_temp = min_real_feel_temp
        self.max_real_feel_temp = max_real_feel_temp
        self.day_has_precipitations = day_has_precipitations
        self.day_precip_type = day_precip_type
        self.day_precip_intensity = day_precip_intensity
        self.day_wind_speed = day_wind_speed
        self.day_wind_direction = day_wind_direction
        self.night_has_precipitations = night_has_precipitations
        self.night_precip_type = night_precip_type
        self.night_precip_intensity = night_precip_intensity
        self.night_wind_speed = night_wind_speed
        self.night_wind_direction = night_wind_direction

    def __repr__(self):
        return (f"DailyForecast(date={self.date!r}, sunrise={self.sunrise!r}, sunset={self.sunset!r}, "
                f"moonrise={self.moonrise!r}, moonset={self.moonset!r}, min_temp={self.min_temp}, "
                f"max_temp={self.max_temp}, min_real_feel_temp={self.min_real_feel_temp}, "
                f"max_real_feel_temp={self.max_real_feel_temp}, day_has_precipitations={self.day_has_precipitations}, "
                f"day_precip_type={self.day_precip_type!r}, day_precip_intensity={self.day_precip_intensity!r}, "
                f"day_wind_speed={self.day_wind_speed}, day_wind_direction={self.day_wind_direction!r}, "
                f"night_has_precipitations={self.night_has_precipitations}, night_precip_type={self.night_precip_type!r}, "
                f"night_precip_intensity={self.night_precip_intensity!r}, night_wind_speed={self.night_wind_speed}, "
                f"night_wind_direction={self.night_wind_direction!r})")
