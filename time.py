
import time, re
import urllib.request as urllib2
import os;
import bs4
from bs4 import BeautifulSoup

import csv
import numpy as np
import pandas
import validators

def get_time(file, url):
    req = urllib2.urlopen(url)


    soup = bs4.BeautifulSoup(req, "lxml")
    s = req.read().decode(url)

    all_time=soup.find_all("time")
    authors = re.findall(r'<b .*?>(.*?)</b>', s)
    time_list= []

    for time in all_time:
        time_list.append(time.get('datetime'))
        print(time.get('datetime'))
    print(time_list)

    with open(file, 'a') as f:
            writer = csv.writer(f)
            #writer.writerow('\n')
            writer.writerows(time_list)
            print("writing...")

with open("results_2.csv", 'r') as f:
    for row in f:
        url = row.split(',')[1]
        if(validators.url(url)):
            print(url)
            get_time("time_2.csv",url)
            #get_time("time.txt",url)
        else:
            continue



