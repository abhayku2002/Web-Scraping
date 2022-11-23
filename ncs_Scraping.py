import requests
from bs4 import BeautifulSoup

req = requests.get("https://ncs.io/")

soup = BeautifulSoup(req.content, "html.parser")

print(soup.prettify())          #case: 1




# pip install beautifulsoup4
# pip install requests

print(soup.get_text())          #case: 2

res= soup.title

print(res.get-text())           #case: 3
