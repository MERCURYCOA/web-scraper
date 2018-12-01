import urllib.request as urllib2
import bs4
from bs4 import BeautifulSoup
import csv


url = "https://forum.sparkfun.com/viewforum.php?f=5&start=1450"


page = urllib2.urlopen(url)
soup = BeautifulSoup(page, 'html.parser')

title_list = []
views_list = []
replies_list = []
authors_list = []
for title in soup.find_all('a', "topictitle"):
    title_list.append(title.text)
    
for views in soup.find_all('dd', "views"):
    views_list.append(views.text)
for replies in soup.find_all('dd', "posts"):
    replies_list.append(replies.text)
for authors in soup.find_all('div', 'topic-poster responsive-hide'):
    authors_list.append(authors.text)


print(title_list)
print(views_list)
print(replies_list)
print(authors_list)