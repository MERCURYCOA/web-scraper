#coding:utf-8
import re
import urllib
import urllib.request
import csv
import numpy as np
import pandas
import validators


#url = "https://forum.openrov.com/t/software-exploration-dds-and-the-trident-2/6891/9"
#file = "open.csv"



def one_link_posts(file, url):
    con_list = []
    with urllib.request.urlopen(url) as url:
        encoding = url.info().get_param('charset', 'utf8')
        s = url.read().decode(encoding)

#爬取标题
    title = re.findall(r'<title>(.*?)</title>', s)
    print(title[0])

    times = re.findall(r'<time .*?>(.*?)</time>', s)
    print(times)

    authors = re.findall(r'<b .*?>(.*?)</b>', s)
    print(authors)

    start = s.find(r"<span itemprop='position'>#1</span>")
    end = s.find(r"<span itemprop='position'>#2</span>")
    page = s[start:end]
    #res = r"(?<=href=\").+?(?=\")|(?<=href=\').+?(?=\')"
    #t1 = re.findall(res, page)  #超链接
    #print t1[0]
    #t2 = re.findall(r'<b .*?>(.*?)</b>', page)  #author
    #print t2[0]
    texts = re.findall('<p>(.*?)</p>', page, re.M|re.S)
    t3 =''.join(texts)
    t3=re.sub(r'src="(.*?)"', '', t3)
    #t3=re.sub('(<a class="lightbox">).*?(</a>)',"", t3, flags=re.DOTALL)
    #t3=re.sub(r'<img  alt="(.*?)">', '', t3)
    con_list.append(t3)
    print(t3)

    start = s.find(r"<span itemprop='position'>#2</span>")
    end = s.find(r"<span itemprop='position'>#3</span>")
    page = s[start:end]
    #res = r"(?<=href=\").+?(?=\")|(?<=href=\').+?(?=\')"
    #t1 = re.findall(res, page)  #超链接
    #print t1[0]
    #t2 = re.findall(r'<a .*?>(.*?)</a>', page)  #标题
    #print t2[0]
    texts = re.findall('<p>(.*?)</p>', page, re.M|re.S)
    t3 = ''.join(texts)
    t3=re.sub(r'src="(.*?)"', '', t3)
    #t3=re.sub(r'<img alt="(.*?)">', '', t3)
    #t3=re.sub('(<a class="lightbox">).*?(</a>)',"", t3, flags=re.DOTALL)
    print(t3)
    con_list.append(t3)

    start = s.find(r"<span itemprop='position'>#3</span>")
    end = s.find(r"<span itemprop='position'>#4</span>")
    page = s[start:end]
    #res = r"(?<=href=\").+?(?=\")|(?<=href=\').+?(?=\')"
    #t1 = re.findall(res, page)  #超链接
    #print t1[0]
    #t2 = re.findall(r'<a .*?>(.*?)</a>', page)  #标题
    #print t2[0]
    texts = re.findall('<p>(.*?)</p>', page, re.M|re.S)
    t3 = ''.join(texts)
    t3=re.sub(r'src="(.*?)"', '', t3)
    #t3=re.sub(r'<img alt="(.*?)">', '', t3)
    #t3=re.sub('(<a class="lightbox">).*?(</a>)',"", t3, flags=re.DOTALL)
    print(t3)
    con_list.append(t3)

    start = s.find(r"<span itemprop='position'>#4</span>")
    end = s.find(r"<span itemprop='position'>#5</span>")
    page = s[start:end]
    #res = r"(?<=href=\").+?(?=\")|(?<=href=\').+?(?=\')"
    #t1 = re.findall(res, page)  #超链接
    #print t1[0]
    #t2 = re.findall(r'<a .*?>(.*?)</a>', page)  #标题
    #print t2[0]
    texts = re.findall('<p>(.*?)</p>', page, re.M|re.S)
    t3 = ''.join(texts)
    t3=re.sub(r'src="(.*?)"', '', t3)
    #t3=re.sub(r'<img alt="(.*?)">', '', t3)
    #t3=re.sub('(<a class="lightbox">).*?(</a>)',"", t3, flags=re.DOTALL)
    print(t3)
    con_list.append(t3)


    start = s.find(r"<span itemprop='position'>#5</span>")
    end = s.find(r"<span itemprop='position'>#6</span>")
    page = s[start:end]
    #res = r"(?<=href=\").+?(?=\")|(?<=href=\').+?(?=\')"
    #t1 = re.findall(res, page)  #超链接
    #print t1[0]
    #t2 = re.findall(r'<a .*?>(.*?)</a>', page)  #标题
    #print t2[0]
    texts = re.findall('<p>(.*?)</p>', page, re.M|re.S)
    t3 = ''.join(texts)
    t3=re.sub(r'src="(.*?)"', '', t3)
    #t3=re.sub(r'<img alt="(.*?)">', '', t3)
    #t3=re.sub('(<a class="lightbox">).*?(</a>)',"", t3, flags=re.DOTALL)
    print(t3)
    con_list.append(t3)

    start = s.find(r"<span itemprop='position'>#6</span>")
    end = s.find(r"<span itemprop='position'>#7</span>")
    page = s[start:end]
    #res = r"(?<=href=\").+?(?=\")|(?<=href=\').+?(?=\')"
    #t1 = re.findall(res, page)  #超链接
    #print t1[0]
    #t2 = re.findall(r'<a .*?>(.*?)</a>', page)  #标题
    #print t2[0]
    texts = re.findall('<p>(.*?)</p>', page, re.M|re.S)
    t3 = ''.join(texts)
    t3=re.sub(r'src="(.*?)"', '', t3)
    #t3=re.sub(r'<img alt="(.*?)">', '', t3)
    #t3=re.sub('(<a class="lightbox">).*?(</a>)',"", t3, flags=re.DOTALL)
    print(t3)
    con_list.append(t3)


    start = s.find(r"<span itemprop='position'>#7</span>")
    end = s.find(r"<span itemprop='position'>#8</span>")
    page = s[start:end]
    #res = r"(?<=href=\").+?(?=\")|(?<=href=\').+?(?=\')"
    #t1 = re.findall(res, page)  #超链接
    #print t1[0]
    #t2 = re.findall(r'<a .*?>(.*?)</a>', page)  #标题
    #print t2[0]
    texts = re.findall('<p>(.*?)</p>', page, re.M|re.S)
    t3 = ''.join(texts)
    t3=re.sub(r'src="(.*?)"', '', t3)
    #t3=re.sub(r'<img alt="(.*?)">', '', t3)
    #t3=re.sub('(<a class="lightbox">).*?(</a>)',"", t3, flags=re.DOTALL)
    print(t3)
    con_list.append(t3)

    start = s.find(r"<span itemprop='position'>#8</span>")
    end = s.find(r"<span itemprop='position'>#9</span>")
    page = s[start:end]
    #res = r"(?<=href=\").+?(?=\")|(?<=href=\').+?(?=\')"
    #t1 = re.findall(res, page)  #超链接
    #print t1[0]
    #t2 = re.findall(r'<a .*?>(.*?)</a>', page)  #标题
    #print t2[0]
    texts = re.findall('<p>(.*?)</p>', page, re.M|re.S)
    t3 = ''.join(texts)
    t3=re.sub(r'src="(.*?)"', '', t3)
    #t3=re.sub(r'<img alt="(.*?)">', '', t3)
    #t3=re.sub('(<a class="lightbox">).*?(</a>)',"", t3, flags=re.DOTALL)
    print(t3)
    con_list.append(t3)

    start = s.find(r"<span itemprop='position'>#9</span>")
    end = s.find(r"<span itemprop='position'>#10</span>")
    page = s[start:end]
    #res = r"(?<=href=\").+?(?=\")|(?<=href=\').+?(?=\')"
    #t1 = re.findall(res, page)  #超链接
    #print t1[0]
    #t2 = re.findall(r'<a .*?>(.*?)</a>', page)  #标题
    #print t2[0]
    texts = re.findall('<p>(.*?)</p>', page, re.M|re.S)
    t3 = ''.join(texts)
    t3=re.sub(r'src="(.*?)"', '', t3)
    #t3=re.sub(r'<img alt="(.*?)">', '', t3)
    #t3=re.sub('(<a class="lightbox">).*?(</a>)',"", t3, flags=re.DOTALL)
    print(t3)
    con_list.append(t3)

    start = s.find(r"<span itemprop='position'>#10</span>")
    end = s.find(r"<span itemprop='position'>#11</span>")
    page = s[start:end]
    #res = r"(?<=href=\").+?(?=\")|(?<=href=\').+?(?=\')"
    #t1 = re.findall(res, page)  #超链接
    #print t1[0]
    #t2 = re.findall(r'<a .*?>(.*?)</a>', page)  #标题
    #print t2[0]
    texts = re.findall('<p>(.*?)</p>', page, re.M|re.S)
    t3 = ''.join(texts)
    t3=re.sub(r'src="(.*?)"', '', t3)
    #t3=re.sub(r'<img alt="(.*?)">', '', t3)
    #t3=re.sub('(<a class="lightbox">).*?(</a>)',"", t3, flags=re.DOTALL)
    print(t3)
    con_list.append(t3)

    start = s.find(r"<span itemprop='position'>#11</span>")
    end = s.find(r"<footer>")
    page = s[start:end]
    #res = r"(?<=href=\").+?(?=\")|(?<=href=\').+?(?=\')"
    #t1 = re.findall(res, page)  #超链接
    #print t1[0]
    #t2 = re.findall(r'<a .*?>(.*?)</a>', page)  #标题
    #print t2[0]
    texts = re.findall('<p>(.*?)</p>', page, re.M|re.S)
    t3 = ''.join(texts)
    t3=re.sub(r'src="(.*?)"', '', t3)
    #t3=re.sub(r'<img alt="(.*?)">', '', t3)
    #t3=re.sub('(<a class="lightbox">).*?(</a>)',"", t3, flags=re.DOTALL)
    print(t3)
    con_list.append(t3)

    with open('open2.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow(zip(authors, con_list))


with open("results.csv", 'r') as f:
    for row in f:
        url = row.split(',')[1]
        if(validators.url(url)):
            print(url)
            one_link_posts("open2.csv", url)
        else:
            continue

