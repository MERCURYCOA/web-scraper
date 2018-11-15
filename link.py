from selenium import webdriver
import time, re
import urllib.request as urllib2
import os;
import bs4
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager

#os.environ["PATH"] += os.pathsep + r'/user/local/bin/chromedriver';


#url = "https://forum.openrov.com/c/underwater-robots"
#req = urllib2.urlopen(url)

driver = webdriver.Chrome(ChromeDriverManager().install())
#driver.implicity_wait(3)
driver.get("https://forum.openrov.com/c/underwater-robots")
for i in range(1,10):
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
    time.sleep(1)
soup = BeautifulSoup(driver.page_source, "lxml")
#soup = bs4.BeautifulSoup(req, "lxml")
all_a=soup.find_all("a")
for link in all_a:
#    if "http" in link.get("href"):
     print('https://forum.openrov.com'+link.get("href"))

    #print(link.text)

#print(soup.prettify())



