#!/usr/bin/env python
# coding=utf-8

import pymysql

try:
    db = pymysql.connect('127.0.0.1', 'max', 'Jjy662500', 'carcdb')
    print("连接成功")
    cur = db.cursor()
    sql = "SELECT * FROM site"
    cur.execute(sql)
    results = cur.fetchall()
    for row in results:
        SiteID = row[0]
        SiteName = row[1]
        print ('SiteID:%s, SiteName:%s'%(SiteID, SiteName))

except pymysql.Error as e:
    print ("失败" +str(e))
    db.rollback()


db.close()
