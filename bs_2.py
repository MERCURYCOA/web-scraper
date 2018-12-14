import urllib.request as urllib2
import bs4
from bs4 import BeautifulSoup
import csv
import validators

#source_page = "https://forum.openrov.com/t/issue-connecting-openrov-2-8-to-laptop/6567"
def page_content(file, url):

    page = urllib2.urlopen(url)
    soup = BeautifulSoup(page, 'html.parser')

    title = soup.find_all('title')[0].text
    print(title)
    authors = soup.find_all('b')
    author_l = []
    time_l = []
    for author in authors:
        author_l.append(author.text)

    times = soup.find_all('time')
    for time in times:
        time_l.append(time.text)

    content_l = []
    posts = soup.find_all('div', {'class': 'post'})
    for post in posts:
        content_l.append(post.text)
        #print(post.text)

    pair_list = zip(author_l, time_l, content_l)

    with open(file, 'a') as f:
                writer = csv.writer(f)
                # writer.writerow([url])
                # writer.writerow([title])
                writer.writerow(time_l)
                writer.writerow(" ")
                # writer.writerows(pair_list)
                print("writing...")

with open("hello_2.csv", 'r') as f:
    for row in f:
        url = row.split(',')[0]
        # url = row[0]
        if(validators.url(url)):
            print(url)
            page_content("hello_2_time.csv", url)
        else:
            continue
