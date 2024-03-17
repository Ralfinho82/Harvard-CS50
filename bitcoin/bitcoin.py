import json
import sys
import requests

user_amount = float(sys.argv[1])

if type(user_amount) != float:
    sys.exit("Wrong input")

try:
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    o = response.json()

    result = user_amount * float(o["bpi"]["USD"]["rate_float"])
    print(f"${result:,.4f}")

except KeyError:
    pass
