import urllib.request as urllib2
import bs4
from bs4 import BeautifulSoup
import csv
import validators

#source_page = "https://forum.openrov.com/t/issue-connecting-openrov-2-8-to-laptop/6567"
def page_content(file, url):

    page = urllib2.urlopen(url)
    soup = BeautifulSoup(page, 'html.parser')
    print(soup.get_text())
    
    loc_l
    location = soup.find_all('h3', class_='location-and-website')
    lines = [loc.get_text() for loc in location]
    for line in lines:
        loc_l.append(line)
        

    joint = soup.find_all('span', {class_: 'relative-date date'})[0].text
    seen = soup.find_all('span', {class_: 'relative-date date'})[2].text



    with open(file, 'a') as f:
                writer = csv.writer(f)
                # writer.writerow([url])
                # writer.writerow([title])
                writer.writerow(loc_l)
                writer.writerow(" ")
                # writer.writerows(pair_list)
                print("writing...")

with open("userPost.csv", 'r') as f:
    for row in f:
        url = row.split(',')[0]
        url = row[0]
        if(validators.url(url)):
            print(url)
            page_content("userLinks.csv", url)
        else:
            continue
