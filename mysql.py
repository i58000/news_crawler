#!/usr/bin/python
#coding=utf-8
import tech_163
import MySQLdb
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def insertNews(news):
    for n in news:
        sql = 'insert REPLACE into news(link,title,dt,cate,src,content) value(%s,%s,%s,%s,%s,%s)'
        cur.execute(sql, (n['link'], n['title'], n['dt'], n['cate'], n['src'], n['content']))

conn = MySQLdb.connect(user='root', passwd='1234', host='localhost', db="news_db", charset="utf8")
conn.autocommit(1)
cur = conn.cursor()

news = tech_163.getNews()
insertNews(news)

cur.close()
conn.close()