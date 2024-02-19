import requests
from bs4 import BeautifulSoup

URL = 'https://www.upwork.com/nx/find-work/best-matches'
req = requests.get(URL)
soup = BeautifulSoup(req.content, "html.parser")
results = soup.find_all("a")
print(results)