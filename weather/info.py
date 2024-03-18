import requests
from . import key


class WeatherInfo:

    def get_rain_probability(self):
        """
        RainProbability	 int32	Percent representing the probability of rain. May be NULL.
        :return: returns a integer in percentage unit
        """
        return self.weather_json[0]["RainProbability"]

    def get_cloud_cover_percentage(self):
        """
        CloudCover	int32	Number representing the percentage of the sky that is covered by clouds. May be NULL.
        :return: returns a integer in percentage
        """
        return self.weather_json[0]["CloudCover"]

    def get_weather_string(self):
        """
        IconPhrase	string	Phrase description of the forecast associated with the WeatherIcon. Displayed in language specified by language code in URL.
        :return: returns a weather string representing condition
        """
        try:
            self.retrieve_key(self.name, self.country_code)
            forecast = key.get_forcast_by_location_key_link(self.location_key)
            res = requests.get(forecast)
            self.weather_json = res.json()
            print(self.weather_json)
            return self.weather_json[0]["IconPhrase"]
        except:
            print("Unable to get location")
            return ""

    def retrieve_key(self, name, country_code):
        link = key.get_cities_name_by_hint_link(name)
        res = requests.get(link)
        json_obj = res.json()
        self.location_key = json_obj[0]["Key"]
        for obj in json_obj:
            country_id = obj["Country"]["ID"]
            if country_id == country_code:
                self.location_key = obj["Key"]

    def __init__(self, name, country_code):
        self.weather_json = None
        self.location_key = None
        self.name = name
        self.country_code = country_code
