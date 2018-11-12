#coding:utf-8
import re
import urllib

url = "http://www.eastmountyxz.com/"
content = urllib.urlopen(url).read()

#爬取标题
title = re.findall(r'<title>(.*?)</title>', content)
print title[0]

#爬取图片地址
urls = re.findall(r'src="(.*?)"', content)
for url in urls:
    print url

#爬取内容
start = content.find(r'<div class="essay">')
end = content.find(r'<div class="essay1">')
page = content[start:end]
res = r"(?<=href=\").+?(?=\")|(?<=href=\').+?(?=\')"
t1 = re.findall(res, page)  #超链接
print t1[0]
t2 = re.findall(r'<a .*?>(.*?)</a>', page)  #标题
print t2[0]
t3 = re.findall('<p style=.*?>(.*?)</p>', page, re.M|re.S) #摘要(
print t3[0]
print ''

start = content.find(r'<div class="essay1">')
end = content.find(r'<div class="essay2">')
page = content[start:end]
res = r"(?<=href=\").+?(?=\")|(?<=href=\').+?(?=\')"
t1 = re.findall(res, page)  #超链接
print t1[0]
t2 = re.findall(r'<a .*?>(.*?)</a>', page)  #标题
print t2[0]
t3 = re.findall('<p style=.*?>(.*?)</p>', page, re.M|re.S) #摘要(
print t3[0]
