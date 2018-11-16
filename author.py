#coding:utf-8
#
#
#
#
# python3 open_general_content.py
import re
import urllib
import urllib.request
import csv
import numpy as np
import pandas
import validators

#url = "https://forum.openrov.com/t/software-exploration-dds-and-the-trident-2/6891/9"
#file = "open.csv"

def position(content, num):
        return content.find(r"<span itemprop='position'>#%s</span>" % num)


def one_link_posts(file, url):

    with urllib.request.urlopen(url) as url:
        encoding = url.info().get_param('charset', 'utf8')
        s = url.read().decode(encoding)



    authors = re.findall(r'<b .*?>(.*?)</b>', s)
    print(authors)

    with open(file, 'a') as f:

        writer = csv.writer(f)
        writer.writerow('\n')
        #writer.writerow(url)
        writer.writerows(authors)
        print("writing...")

with open("results_2.csv", 'r') as f:
    for row in f:
        url = row.split(',')[1]
        if(validators.url(url)):
            print(url)
            one_link_posts("author_support.csv", url)
        else:
            continue
