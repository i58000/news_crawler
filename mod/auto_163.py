#!/usr/bin/python
#coding=utf-8
import re
import requests
from bs4 import BeautifulSoup
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def getPage(addr):
    html = requests.get(addr).text
    soup = BeautifulSoup(html,'lxml')
    aList = soup.select('.item-cont > h3 > a')
    linkList = []
    for a in aList:
        linkList.append(a.get('href'))
    return linkList

def getItem(link):
    html = requests.get(link).text
    soup = BeautifulSoup(html,'lxml')
    title = soup.select("#epContentLeft > h1")[0].get_text()
    dateRE = re.compile(r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}')
    date = re.findall(dateRE, soup.select('#epContentLeft > div.post_time_source')[0].get_text())[0]
    content = ""
    pl = soup.select('div.post_text  p')      
    if pl[0].get('class') != None:
        if pl[0].get('class')[0] == 'otitle':
            del(pl[0])
    for t in pl:
        content += t.get_text() + '\n'
    item = {'title': title,
            'date': date,
            'content': content,
            'cate': 'auto',
            'src': '163',
            'link': link,
    }
    return item
    
def getNews():
    linkList = []
    linkList.extend(getPage('http://auto.163.com/news/'))
    linkList.extend(getPage('http://auto.163.com/special/2016news_02/'))
#     linkList.extend(getPage('http://auto.163.com/special/2016news_03/'))
#     linkList.extend(getPage('http://auto.163.com/special/2016news_04/'))
#     linkList.extend(getPage('http://auto.163.com/special/2016news_05/'))
    news = []
    for link in linkList:
        news.append(getItem(link))
    return news