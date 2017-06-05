#!/usr/bin/python
#coding=utf-8
import tech_163
import auto_163

import pymongo
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
conn = pymongo.MongoClient()
db = conn.newsweb #选择库  
tbl = db.news #使用集合 
    
mod = [tech_163, auto_163]

def update():
    for m in mod:
        err = 0
        cnt = 0
        for news in m.getNews():
            try:
                cnt+=1
                tbl.insert(news) #,continue_on_error=True
            except:
                err+=1
        print "update %s: %d/%d" % (mod[0].__name__,cnt-err,cnt)
print '---------------- success/count'
update()