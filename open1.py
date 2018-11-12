#coding:utf-8
import re
import urllib
import urllib.request
import csv
import numpy as np
import pandas

con_list = []
url = "https://forum.openrov.com/t/software-exploration-dds-and-the-trident-2/6891/9"
with urllib.request.urlopen(url) as url:
    encoding = url.info().get_param('charset', 'utf8')
    s = url.read().decode(encoding)

#爬取标题
title = re.findall(r'<title>(.*?)</title>', s)
print(title[0])

#爬取图片地址
#urls = re.findall(r'src="(.*?)"', s)
#for url in urls:
 #   print url

times = re.findall(r'<time .*?>(.*?)</time>', s)
print(times)

authors = re.findall(r'<b .*?>(.*?)</b>', s)
print(authors)





#爬取内容
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

#data = np.array([authors, con_list])
#data= data.T

#with open('open.csv', 'w+') as myfile:
 #   np.savetxt(myfile, data, fmt= "%s %s")

pd = pandas.DataFrame(authors, con_list)
#pd.insert(loc=0, column='index', value = range(1, len(pd) + 1))

pd.to_csv("open.csv")
