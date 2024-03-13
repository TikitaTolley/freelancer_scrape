# Scraping Freelancer
## Description
This repository contains a gitignore, a CSV file and a python file. 
The purpose of this project was to scrape the site: [Freelancer.co.uk](https://www.freelancer.co.uk/)
for data specific to jobs I was interested in. For this CSV file, I focused on python-related jobs.
I wanted to change the layout of the list of jobs, only getting information specific to: date, title, price, description, skills, and url. In the later YouTube video I placed this data into an excel format.

## Installation
### Setting up the virtual environment
pip install virtualenv
python3 -m venv venv
source venv/bin/activate

### Create gitignore
touch .gitignore (no output expected)
open .gitignore and write in venv

### Installing dependencies
pip install requests
pip install beautifulsoup4
pip install python-csv

## Usage
### Import modules
```
import requests
from bs4 import BeautifulSoup
import csv
from datetime import date
```

- use requests to get the URL
- pass through bs4's html.parser to grab the html from that page
- search for a div with a particlular div
- isolate the information you want
- open a CSV file and pass in the data

## YouTube Video
[Scraping Project Video](https://youtu.be/fjakCJ8rjKw?si=GohBAjXNlCg_xVv5)