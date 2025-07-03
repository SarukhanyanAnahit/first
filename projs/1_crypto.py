import requests
import argparse
import json
import time

def get_crypto_data():
    url = "https://api.coingecko.com/api/v3/coins/markets"
    headers = {
        "x-cg-pro-api-key": "CG-HNng4ue3VXGnWfeVjrd9B7pe"
    }
    params = {
        "vs_currency": "usd",
        "order": "market_cap_desc",
        "per_page": 20,
        "page": 1,
        "sparkline": "false"
    }
    try:
        response = requests.get(url, headers=headers, params=params, timeout=5)
        time.sleep(5)
        return response.json()
    except ModuleNotFoundError:
        print('install request module')
    except:
        print('check url headers or params')

def save_to_json(data, filename="crypto_data.json"):
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)
    print(f"data saved to {filename}")

def load_from_json(filename="crypto_data.json"):
    try:
        with open(filename, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        print("file not found")

def filter_data(data, name_filter=None, min_price=None):
    result = []
    for coin in data:
        name = coin["name"]
        price = coin["current_price"]
        if name_filter!=None and name_filter.lower() not in name.lower():
            continue
        if min_price!=None and price < min_price:
            continue

        result.append(coin)
    return result

def print_data(data):
    print(f"{'Name':20} {'Symbol':8}   {'Price($)':7}     {'Market Cap($)':9}    {'Volume($)':19}    {'24h Change(%)':6}")
    print("-" * 100)
    for coin in data:
        name = coin["name"][:16]
        symbol = coin["symbol"]
        price = coin["current_price"]
        market_cap = coin["market_cap"]
        volume = coin["total_volume"]
        change = coin["price_change_percentage_24h"]

        print(f"{name:20} {symbol:8} {price:12} {market_cap:15} {volume:15} {change:15}")
    print("-" * 100)

def argums():
    parser = argparse.ArgumentParser()
    parser.add_argument("-name", type=str, help="filter by name")
    parser.add_argument("-min", type=float, help="filter by minimum price")
    parser.add_argument("-load", action="store_true", help="load data from crypto_data.json")
    args = parser.parse_args()
    return args

def main():
    args=argums()
    if args.load:
        data = load_from_json()
    else:
        data = get_crypto_data()
        save_to_json(data)

    if data:
        filtered = filter_data(data, args.name, args.min)
        print_data(filtered)
    else:
        print("no data available.")

if __name__ == "__main__":
    main()
