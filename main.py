import requests
import json
from ui import QuotesInterface

API_URL = "https://officeapi.dev/api/quotes"

quotes_interface = QuotesInterface()


def get_quotes():
    response = requests.get(API_URL)
    quotes_list = [
        {"quote": item["content"], "name": f"{item['character']['firstname']} {item['character']['lastname']}"} for item
        in response.json()["data"]]

    with open("quotes.json", "w") as file:
        json.dump(quotes_list, file)
