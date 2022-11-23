import requests
from bs4 import BeautifulSoup

req = requests.get("https://ncs.io/")

soup = BeautifulSoup(req.content, "html.parser")

print(soup.prettify())




#
