import requests

from api.providers.weather_api_client import WeatherApiClient


class AccuWeatherClient(WeatherApiClient):  # to do
    """

    Fetch weather data from https://www.accuweather.com/
    and convert the API response into WeatherData format

    """

    def __init__(self):
        self.api_key = 'EQwGZb1GUqPiFCx66wG5TU6cvLrnTaJh'
        self.base_url = 'https://dataservice.accuweather.com/'

    def get_city_request(self, location_name: str):
        params = {
            'apikey': self.api_key,
            'location': location_name,
            'url_descript': 'locations/v1/cities/search?'
        }
        url = self.base_url + params['url_descript'] + 'apikey=' + params['apikey'] + '&q=' + params['location']
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            print('Failed to retrieve data')
            return None

    def parse_city_list(self, city_json):
        city_list = []
        if len(city_json) > 0:
            for city_info_dict in city_json:
                city_name = city_info_dict.get('LocalizedName')
                city_id = city_info_dict.get('Key')
                admin_area = city_info_dict.get('AdministrativeArea', {}).get('LocalizedName')
                country = city_info_dict.get('Country', {}).get('LocalizedName')
                longitude = city_info_dict.get('GeoPosition', {}).get('Longitude')
                latitude = city_info_dict.get('GeoPosition', {}).get('Latitude')

                city_info = {
                    'name': city_name,
                    'admin_area': admin_area,
                    'country': country,
                    'longitude': longitude,
                    'latitude': latitude,
                    'city_id': city_id
                }
                city_list.append(city_info)
            return city_list
        else:
            print('No cities with this name')
            exit()

    def get_forecast_request(self, city_key: str, duration: str):
        params = {
            'apikey': self.api_key,
            'citykey': city_key,
            'url_descript': 'forecasts/v1/daily/',
            'duration': duration,
            'details': '&details=true'
        }
        url = self.base_url + params['url_descript'] + duration + '/' + city_key + '?' + 'apikey=' + params['apikey'] + \
              params['details']
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            print('Failed to retrieve data')
            return None

    def parse_forecasts_list(self, forecasts_json: dict):
        forecasts = forecasts_json.get('DailyForecasts', 'Unknown DailyForecasts')
        forecast_list = []
        for forecast in forecasts:
            # forecast values
            date = forecast.get('Date', None)
            sunrise = forecast.get('Sun', {}).get('Rise')
            sunset = forecast.get('Sun', {}).get('Set')
            moonrise = forecast.get('Moon', {}).get('Rise')
            moonset = forecast.get('Moon', {}).get('Set')
            min_temp = forecast.get('Temperature', {}).get('Minimum', {}).get('Value')  # Value in Fahrenheit
            max_temp = forecast.get('Temperature', {}).get('Maximum', {}).get('Value')  # Value in Fahrenheit
            min_real_feel_temp = forecast.get('RealFeelTemperature', {}).get('Minimum', {}).get(
                'Value')  # Value in Fahrenheit
            max_real_feel_temp = forecast.get('RealFeelTemperature', {}).get('Maximum', {}).get(
                'Value')  # Value in Fahrenheit
            day_has_precipitations = forecast.get('Day', {}).get('HasPrecipitation')
            day_precip_type = forecast.get('Day', {}).get('PrecipitationType')
            day_precip_intensity = forecast.get('Day', {}).get('PrecipitationIntensity')
            day_wind_speed = forecast.get('Day', {}).get('Wind', {}).get('Speed', {}).get('Value')
            day_wind_direction = forecast.get('Day', {}).get('Wind', {}).get('Direction', {}).get(
                'Value')  # value in degrees
            night_has_precipitations = forecast.get('Day', {}).get('HasPrecipitation')
            night_precip_type = forecast.get('Day', {}).get('PrecipitationType')
            night_precip_intensity = forecast.get('Day', {}).get('PrecipitationIntensity')
            night_wind_speed = forecast.get('Day', {}).get('Wind', {}).get('Speed', {}).get('Value')
            night_wind_direction = forecast.get('Day', {}).get('Wind', {}).get('Direction', {}).get(
                'Value')  # value in degrees

            forecast_info = {'date': date, 'sunrise': sunrise, 'sunset': sunset, 'moonrise': moonrise,
                             'moonset': moonset, 'min_temp': min_temp, 'max_temp': max_temp,
                             'min_real_feel_temp': min_real_feel_temp, 'max_real_feel_temp': max_real_feel_temp,
                             'day_has_precipitations': day_has_precipitations, 'day_precip_type': day_precip_type,
                             'day_precip_intensity': day_precip_intensity, 'day_wind_speed': day_wind_speed,
                             'day_wind_direction': day_wind_direction,
                             'night_has_precipitations': night_has_precipitations,
                             'night_precip_type': night_precip_type, 'night_precip_intensity': night_precip_intensity,
                             'night_wind_speed': night_wind_speed, 'night_wind_direction': night_wind_direction
                             }
            forecast_list.append(forecast_info)

        return forecast_list
