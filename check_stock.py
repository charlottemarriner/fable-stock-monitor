import requests
from bs4 import BeautifulSoup

URL = "https://eu.shop.xboxgamestudios.com/products/fable-collectors-edition"

html = requests.get(URL, headers={
    "User-Agent": "Mozilla/5.0"
}).text

if "Out of stock" not in html:
    print("IN STOCK")
    exit(1)      # Trigger notification
else:
    print("Still out of stock")