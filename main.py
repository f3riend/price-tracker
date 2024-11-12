from bs4 import BeautifulSoup
from twilio.rest import Client
import requests
import os

url = "https://appbrewery.github.io/instant_pot/"

account_sid = os.getenv("SID")
auth_token = os.getenv("AUTH_TOKEN")


response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")
price = float(soup.find(class_="a-offscreen").get_text().split("$")[1])

title = soup.find(id="productTitle").get_text().strip()

BUY_PRICE = 100

if price < BUY_PRICE:
    message = f"{title} is on sale for ${price}!"
    client = Client(account_sid, auth_token)
    client.messages.create(
    from_='VIRTURAL NUMBER',
    body=message,
    to='REAL NUMBER'
    )

