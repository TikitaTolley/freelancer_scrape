import requests
from bs4 import BeautifulSoup

URL = 'https://www.freelancer.co.uk/jobs/?keyword=python'
req = requests.get(URL)
soup = BeautifulSoup(req.content, "html.parser")
results = soup.findAll("div", {"class": "pinky-template"})

unique_cards = set()

if results:  # Check if results is not empty
    res = results[1]
    children = res.findChildren()
    for child in children:
        print(child)
        title = child.find("a", {'class' : 'JobSearchCard-primary-heading-link'})
        description = child.find("p", {"class" : "JobSearchCard-primary-description"})
        price = child.find('div', {'class' : 'JobSearchCard-primary-price'})
        key_skills = 'none'
        url = 'none'
        if description:
            unique_cards.add(description.text.strip())


# for cards in unique_cars:
#     print(cards)
# else:
#     print("No results found")
