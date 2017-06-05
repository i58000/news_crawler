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
    aList = soup.select('.bigsize > a') #所有标题a标签
    linkList = []
    for a in aList:
        linkList.append(a.get('href')) #a标签链接内容
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
            'cate': 'tech',
            'src': '163',
            'link': link,
    }
    return item
    
def getNews():
    linkList = []
    linkList.extend(getPage('http://tech.163.com/special/gd2016/'))
    linkList.extend(getPage('http://tech.163.com/special/gd2016_02/'))
    #linkList.extend(getLinks('http://tech.163.com/special/gd2016_03/'))
    #linkList.extend(getLinks('http://tech.163.com/special/gd2016_04/'))
    #linkList.extend(getLinks('http://tech.163.com/special/gd2016_05/'))
    news = []
    for link in linkList:
        news.append(getItem(link))
    return news
