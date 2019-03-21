# coding:utf-8
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
    con_list = []
    with urllib.request.urlopen(url) as url:
        encoding = url.info().get_param('charset', 'utf8')
        s = url.read().decode(encoding)

    title = re.findall(r'<title>(.*?)</title>', s)
    print(title[0])

    authors = re.findall(r'<b .*?>(.*?)</b>', s)
    print(authors)

    # start = s.find(r"<span itemprop='position'>#%s</span>" % num)
    # end = s.find(r"<span itemprop='position'>#%s</span>" % num)

    for i in range(len(authors)):

        start = position(s, i+1)
        end = position(s, i+2)
        print(1)
        #one_post(start, end, con_list)
        page = s[start:end]
        print(2)
        texts = re.findall(r'<p>(.*?)</p>', page, re.M | re.S)

        print(3)
        t3 = ''.join(texts)
        t3 = re.sub(r'src="(.*?)"', '', t3)
        con_list.append(t3)
        print(4)
        print(t3)

    with open(file, 'a') as f:

        writer = csv.writer(f)
        writer.writerow(title)
        writer.writerow(url)
        writer.writerows(zip(authors, con_list))
        print("writing...")


with open("userLinks.csv", 'r') as f:
    for row in f:
        url = row.split(',')[1]
        if(validators.url(url)):
            print(url)
            one_link_posts("userPost.csv", url)
        else:
            continue
