import requests
from bs4 import BeautifulSoup

req = requests.get("https://www.pexels.com/videos/")

soup = BeautifulSoup(req.content, "html.parser")

print(soup.prettify())

