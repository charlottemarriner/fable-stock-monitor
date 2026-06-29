import os
import requests

URL = "https://eu.shop.xboxgamestudios.com/products/fable-collectors-edition"

headers = {
    "User-Agent": "Mozilla/5.0"
}

page = requests.get(URL, headers=headers).text

if "Out of stock" not in page:
    webhook = os.environ["DISCORD_WEBHOOK"]

    requests.post(
        webhook,
        json={
            "content":
            "🚨 Fable Collector's Edition appears to be IN STOCK!\nhttps://eu.shop.xboxgamestudios.com/products/fable-collectors-edition"
        }
    )

    print("Notification sent!")

else:
    print("Still out of stock.")
