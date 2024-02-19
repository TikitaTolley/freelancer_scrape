import requests
from bs4 import BeautifulSoup

URL = 'https://www.freelancer.co.uk/jobs/?keyword=python'
req = requests.get(URL)
soup = BeautifulSoup(req.content, "html.parser")
results = soup.find("div", {"class": "pinky-template"})
#print(results)
children = results.findChildren()
for child in children:
    print(child.prettify())