#coding:utf-8
import re
import urllib
import urllib.request
import csv
import numpy as np
import pandas
#url = "https://forum.openrov.com/t/software-exploration-dds-and-the-trident-2/6891/9"
#file = "open.csv"


def one_post(start, end, con_list, s):
        page = s[start:end]
        texts = re.findall('<p>(.*?)</p>', page, re.M|re.S)
        t3 =''.join(texts)
        t3=re.sub(r'src="(.*?)"', '', t3)
        con_list.append(t3)
        print(t3)

def one_link_posts(file, url):

    with urllib.request.urlopen(url) as url:
        encoding = url.info().get_param('charset', 'utf8')
        s = url.read().decode(encoding)

    title = re.findall(r'<title>(.*?)</title>', s)
    print(title[0])

    times = re.findall(r'<time .*?>(.*?)</time>', s)
    print(times)

    authors = re.findall(r'<b .*?>(.*?)</b>', s)
    print(authors)

    con_list = []
    if len(authors) > 1 :
        for i in range(len(authors)-1):
            start = s.find(r"<span itemprop='position'>#(i+1)</span>")
            end = s.find(r"<span itemprop='position'>#(i+2)</span>")
            one_post(start, end, con_list,s)
        start = s.find(r"<span itemprop='position'>#n</span>")
        end = s.find(r"<footer>")
        one_post(start, end, con_list,s)
    else:
        start = s.find(r"<span itemprop='position'>#n</span>")
        end = s.find(r"<footer>")
        one_post(start, end, con_list,s)

    pd = pandas.DataFrame(authors, con_list)
    pd.to_csv("file")

one_link_posts("open2.csv", "https://forum.openrov.com/t/software-exploration-dds-and-the-trident-2/6891/9")
