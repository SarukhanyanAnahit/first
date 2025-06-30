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

av_op = {
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
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()

        with open("weather.json", "w") as f:
            json.dump(data, f, indent=4)
        return data
    else:
        return None

def load_weather_from_file():
    if os.path.exists("weather.json"):
        with open("weather.json", "r") as f:
            return json.load(f)
    return None


def available_options():
    print("available options:")
    for opt in av_op:
        print(f" -{opt}")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', help="name of city")
    parser.add_argument('-options', choices=av_op.keys())
    args = parser.parse_args()

    if not args.c:
        return available_options()

    data = load_weather_from_file()

    if not data or data.get("name", "").lower() != args.c.lower():
        data = fetch_weather(args.c)

    if not data:
        print("city hasn't been found.")
        return

    if args.options:
        value = av_op[args.options](data)
        print(f"{args.options.capitalize()}: {value}")
    else:
        print(f"weather of {args.c}:")
        for field, func in av_op.items():
            print(f"{field.capitalize()}: {func(data)}")

if __name__ == '__main__':
    main()
