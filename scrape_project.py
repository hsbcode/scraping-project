import requests
from bs4 import BeautifulSoup
from csv import writer

#Getting a request from the url: "https://www.rithmschool.com/blog
response_p1 = requests.get("https://www.rithmschool.com/blog")
response_p2 = requests.get("https://www.rithmschool.com/blog?page=2")
response_p3 = requests.get("https://www.rithmschool.com/blog?page=3")
response_p4 = requests.get("https://www.rithmschool.com/blog?page=4")
response_p5 = requests.get("https://www.rithmschool.com/blog?page=5")
response_p6 = requests.get("https://www.rithmschool.com/blog?page=6")
response_p7 = requests.get("https://www.rithmschool.com/blog?page=7")

#Instantiating a new BeautifulSoup object 
soup_1 = BeautifulSoup(response_p1.text, "html.parser")
soup_2 = BeautifulSoup(response_p2.text, "html.parser")
soup_3 = BeautifulSoup(response_p3.text, "html.parser")
soup_4 = BeautifulSoup(response_p4.text, "html.parser")
soup_5 = BeautifulSoup(response_p5.text, "html.parser")
soup_6 = BeautifulSoup(response_p6.text, "html.parser")
soup_7 = BeautifulSoup(response_p7.text, "html.parser")

# We'll be getting all the articles in the blog page with:
articles_p1 = soup_1.find_all("article")
articles_p2 = soup_2.find_all("article")
articles_p3 = soup_3.find_all("article")
articles_p4 = soup_4.find_all("article")
articles_p5 = soup_5.find_all("article")
articles_p6 = soup_6.find_all("article")
articles_p7 = soup_7.find_all("article")

# Getting article titles, urls and posting dates from the articles.

# Opening up a csv file, into which the data from the blog will be written.
with open("C:\\Users\\seyfi\\OneDrive - boun.edu.tr\\yedekleme\\Codes\\Colt Pyhton Leap 2\\Web scraping with BeautifulSoup\\rithm_blog_data.csv", "w") as file:
   csv_writer = writer(file)
   csv_writer.writerow(["title", "url", "date"]) 
#Scraping the data (entry titles, entry URLs , and entry dates) from the blog.
   for article in articles_p1:
    a_tag = article.find("a")
    title = a_tag.get_text()
    url = a_tag['href']
    date = article.find("small").get_text()
    csv_writer.writerow([title, url, date])
   for article in articles_p2:
    a_tag = article.find("a")
    title = a_tag.get_text()
    url = a_tag['href']
    date = article.find("small").get_text()
    csv_writer.writerow([title, url, date])
   for article in articles_p3:
    a_tag = article.find("a")
    title = a_tag.get_text()
    url = a_tag['href']
    date = article.find("small").get_text()
    csv_writer.writerow([title, url, date])
   for article in articles_p4:
    a_tag = article.find("a")
    title = a_tag.get_text()
    url = a_tag['href']
    date = article.find("small").get_text()
    csv_writer.writerow([title, url, date])
   for article in articles_p5:
    a_tag = article.find("a")
    title = a_tag.get_text()
    url = a_tag['href']
    date = article.find("small").get_text()
    csv_writer.writerow([title, url, date])
   for article in articles_p6:
    a_tag = article.find("a")
    title = a_tag.get_text()
    url = a_tag['href']
    date = article.find("small").get_text()
    csv_writer.writerow([title, url, date])
   for article in articles_p7:
    a_tag = article.find("a")
    title = a_tag.get_text()
    url = a_tag['href']
    date = article.find("small").get_text()
    csv_writer.writerow([title, url, date])
