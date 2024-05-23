import requests
from sys import exit, argv

def main():
    if len(argv) != 2:
        exit("Missing command-line argument")
    try:
        n = float(argv[1])
    except ValueError:
        exit("Command-line argument is not a number")
    try:
        request = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    except requests.RequestException:
        exit()
    price = request.json()["bpi"]["USD"]["rate_float"] * float(argv[1])
    print(f"${price:,.4F}")
main()
