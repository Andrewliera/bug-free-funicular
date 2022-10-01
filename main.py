from enum import Enum
import requests
import configparser


class NoSuchLocation(Exception):
    pass


class BadInput(Exception):
    pass


class SomeOtherError(Exception):
    pass


class temp_key():
    try:
        config = configparser.ConfigParser()
        config.read('app.config')
        config.sections()
        curr_key = config['secrets']['apikey']
    except SomeOtherError:
        print("An Error Occered with app.config")

class url_calls(Enum):
    LOCATION = 1
    CONDITIONS = 2
    FORECASTS = 3


def url_factory(call_type, api_key, additional_data):
    try:
        if call_type == url_calls.LOCATION:
            return 'http://dataservice.accuweather.com/locations/v1/postalcodes/search?apikey={}' \
                   '&q={}'.format(api_key, additional_data)
        elif call_type == url_calls.CONDITIONS:
            return 'http://dataservice.accuweather.com/currentconditions/v1/' \
                   '{}?apikey={}'.format(additional_data, api_key)
        elif call_type == url_calls.FORECASTS:
            return 'http://dataservice.accuweather.com/forecasts/v1/daily/5day/' \
                   '{}?apikey={}'.format(additional_data, api_key)
    except SomeOtherError:
        print('Some Other Error in url factory calls')


def get_location(user_zip):

    location_url = url_factory(url_calls.LOCATION, temp_key.curr_key, user_zip)
    response = requests.get(location_url)

    try:
        key = response.json()[0].get('Key')
        name = response.json()[0].get('EnglishName')
        print("The current Forecast in " + name)
    except IndexError:
        raise NoSuchLocation()
    return key


def get_conditions(key):

    conditions_url = url_factory(url_calls.CONDITIONS, temp_key.curr_key, key)
    response = requests.get(conditions_url)
    json_version = response.json()
    print("The current forecast is {}".format(json_version[0].get('WeatherText')))
    return


def get_forcast(key):

    forecast_url = url_factory(url_calls.FORECASTS, temp_key.curr_key, key)
    response = requests.get(forecast_url)
    json_version = response.json()

    try:
        for i in range(0, 4):
            print(json_version['DailyForecasts'][i]['Date'] + " will be: "
                  + json_version['DailyForecasts'][i]['Day']['IconPhrase'])
    except SomeOtherError:
        print("Some Other Error")
    return


def weather_check(user_in):
    try:
        location_key = get_location(user_in)
        get_conditions(location_key)
        get_forcast(location_key)
    except BadInput:
        raise BadInput()
    return


if __name__ == '__main__':
    try:
        print("Welcome to a quick weather checker")
        start_prog = input("press c to continue\nother keys to exit\nYour Input: ")

        while start_prog == 'c':
            user_input = input("Please Input Your Zipcode to continue: ")
            weather_check(user_input)
            start_prog = input("press c to continue\nother keys to exit\nYour Input: ")

    except NoSuchLocation:
        print("Unable to find location")
