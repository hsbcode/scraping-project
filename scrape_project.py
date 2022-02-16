import requests
from bs4 import BeautifulSoup
import csv

#Getting a request from the url: "https://www.rithmschool.com/blog
response = requests.get("https://www.rithmschool.com/blog")

#Instantiating a new BeautifulSoup object 
soup = BeautifulSoup(response.text, "html.parser")

# We'll be getting all the articles in the blog page with:
articles = soup.find_all("article")

# Getting article titles from a href tags.
for article in articles:
    a_tag = article.find("a")
    title = a_tag.get_text()
    url = a_tag['href']
    time = article.find("small").get_text()