import requests
from bs4 import BeautifulSoup
import csv
from datetime import date

URL = 'https://www.freelancer.co.uk/jobs/?keyword=python'
req = requests.get(URL)
soup = BeautifulSoup(req.content, "html.parser")
results = soup.findAll("div", {"class": "pinky-template"})

unique_cards = []
titles = []

if results:  # Check if results is not empty
    res = results[1]
    children = res.findChildren()
    for child in children:
        title = child.find("a", {'class' : 'JobSearchCard-primary-heading-link'})

        description = child.find("p", {"class" : "JobSearchCard-primary-description"})
        price = child.find('div', {'class' : 'JobSearchCard-primary-price'})
        skills_data = child.find('div', {"class" : "JobSearchCard-primary-tags"})
        if skills_data:
            skill_links = skills_data.find_all('a', href=True)
            for skill in skill_links:
                skill_text = skill.text.strip()
        url_tag = child.findAll('a', {'class' : 'JobSearchCard-primary-heading-link'})
        for url in url_tag:
            if url != 'None':
                link = 'https://www.freelancer.co.uk/jobs/?keyword=python' + url['href']
        if description and title and price:
            ftitle = title.text.strip()
            if ftitle not in titles:
                titles.append(ftitle)
                unique_cards.append([ftitle, price.text.strip(), description.text.strip(), skill_text, link])


for cards in unique_cards:
    for c in cards:
        print(c)
if len(unique_cards) == 0:
    print("No results found")

today = date.today()
print("today's date: ", today)

with open('data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    field = ["date", "title", "price", "description", "skills", "url"]
    
    writer.writerow(field)
    for c in unique_cards:
        writer.writerow([f"{today}", f"{c[0]}", f"{c[1]}", f"{c[2]}", f"{c[3]}", f"{c[4]}"])