import argparse
import requests
import json
import os

def get_temperature(data):
    return f"{data['main']['temp']} °C"

def get_feels_like(data):
    return f"{data['main']['feels_like']} °C"

def get_humidity(data):
    return f"{data['main']['humidity']} %"

def get_pressure(data):
    return f"{data['main']['pressure']} hPa"

def get_wind_speed(data):
    return f"{data['wind']['speed']} m/s"

def get_description(data):
    return data['weather'][0]['description']

options_list = {
    "temperature": get_temperature,
    "feels_like": get_feels_like,
    "humidity": get_humidity,
    "pressure": get_pressure,
    "wind_speed": get_wind_speed,
    "description": get_description,
}

def fetch_weather(city):
    params = {
        'q': city,
        'appid': '53eb2016dee56fe18c7179c0aa1bdb76',
        'units': 'metric',
    }
    url = 'http://api.openweathermap.org/data/2.5/weather'
    try:
        response = requests.get(url, params=params)
        if response.status_code == 200:
            data = response.json()

            with open("weather.json", "w") as f:
                json.dump(data, f, indent=4)
            return data
        else:
            return None
    except ModuleNotFoundError:
        return "module not found"


def load_weather_from_file():
    try:
        if os.path.exists("weather.json"):
            with open("weather.json", "r") as f:
                return json.load(f)
        return None
    except FileNotFoundError:
        return "file not found"


def available_options():
    print("available options:")
    for opt in options_list:
        print(f" -{opt}")

def argums():
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', help="name of city")
    parser.add_argument('-options', choices=options_list.keys())
    args = parser.parse_args()
    return args

def main():
    args=argums()

    if not args.c:
        return available_options()

    data = load_weather_from_file()

    if not data or data.get("name", "").lower() != args.c.lower():
        try:
            data = fetch_weather(args.c)
        except:
            print("request doesn't working")

    if not data:
        print("city hasn't been found.")
        return

    if args.options:
        try:
            value = options_list[args.options](data)
            print(f"{args.options.capitalize()}: {value}")
        except KeyError:
            return "you inputted wrong key"
    else:
        print(f"weather of {args.c}:")
        try:
            for field, func in options_list.items():
                print(f"{field.capitalize()}: {func(data)}")
        except AttributeError:
            return "not corresponding"

if __name__ == '__main__':
    main()
