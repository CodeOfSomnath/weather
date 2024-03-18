WEATHER_DECODING_KEY = 'oI1QNRXcss6AiVq7TucNMlXyBDOGREtk'
WEBSITE_USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"

from enum import Enum


class CountryCode(Enum):
    INDIA = 'IN'
    WEST_BENGAL = 'WB'


# https://dataservice.accuweather.com/locations/v1/cities/autocomplete?apikey=oI1QNRXcss6AiVq7TucNMlXyBDOGREtk&q=egra


def get_admin_area_link(country_code):
    return f"http://dataservice.accuweather.com/locations/v1/adminareas/{country_code}?apikey=oI1QNRXcss6AiVq7TucNMlXyBDOGREtk"


def get_country_name_link(region_code):
    """
    Returns basic information about all countries within a specified region.
    :param region_code: Region code for getting country on that region
    :return: a link where you can get country names by http get request
    """
    return f"http://dataservice.accuweather.com/locations/v1/countries/{region_code}?apikey=oI1QNRXcss6AiVq7TucNMlXyBDOGREtk"


def get_all_regions_info_link():
    return "http://dataservice.accuweather.com/locations/v1/regions?apikey=oI1QNRXcss6AiVq7TucNMlXyBDOGREtk"


def get_all_top_cities_name_link():
    return "http://dataservice.accuweather.com/locations/v1/topcities/group?apikey=oI1QNRXcss6AiVq7TucNMlXyBDOGREtk"


def get_cities_name_by_hint_link(query):
    return f"http://dataservice.accuweather.com/locations/v1/cities/autocomplete?apikey=oI1QNRXcss6AiVq7TucNMlXyBDOGREtk&q={query}"


def get_search_by_locations_name_link(location_key):
    return f"http://dataservice.accuweather.com/locations/v1/{location_key}?apikey=oI1QNRXcss6AiVq7TucNMlXyBDOGREtk"


def get_forcast_by_location_key_link(location_key):
    return f"http://dataservice.accuweather.com/forecasts/v1/hourly/1hour/{location_key}?apikey=oI1QNRXcss6AiVq7TucNMlXyBDOGREtk&details=true"
