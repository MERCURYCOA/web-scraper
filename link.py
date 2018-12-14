from selenium import webdriver
import time, re
import urllib.request as urllib2
import os;
import bs4
import csv
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager

#os.environ["PATH"] += os.pathsep + r'/user/local/bin/chromedriver';


#url = "https://forum.openrov.com/c/underwater-robots"
#req = urllib2.urlopen(url)

driver = webdriver.Chrome(ChromeDriverManager().install())
#driver.implicity_wait(3)
# driver.get("https://forum.openrov.com/c/underwater-robots")
driver.get("https://forum.openrov.com/c/tips-and-tricks")
for i in range(1,10):
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
    time.sleep(1)
soup = BeautifulSoup(driver.page_source, "lxml")
#soup = bs4.BeautifulSoup(req, "lxml")
links = []
all_a=soup.find_all("a")
for link in all_a:
#    if "http" in link.get("href"):
    real_url = str('https://forum.openrov.com'+link.get("href"))
    links.append(link.get('href'))
    print(real_url)
    # print(link.get('href'))
with open('links.csv', 'a') as f:
                writer = csv.writer(f)
                writer.writerow(links)
                # writer.writerow([title])
                # writer.writerow(time_l)
                # writer.writerows(pair_list)
                print("writing...")
    #print(link.text)

#print(soup.prettify())



