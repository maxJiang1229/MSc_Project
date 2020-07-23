#!/usr/bin/env python
# coding=utf-8

import pymysql

DBHOST = '127.0.0.1'
DBUSER = 'max'
DBPASS = 'Jjy662500'
DBNAME = 'carcdb'

try:
    db = pymysql.connect( DBHOST, DBUSER, DBPASS, DBNAME)
    print("Connection succeeded")
    cur = db.cursor()
    sql = "SELECT * FROM doseresp"
    cur.execute(sql)
    results = cur.fetchall()
    for row in results:
        DoseRespID = row[0]
        ObsID = row[1]
        Dose = row[2]
        DoseUnit = row[3]
        TotalAnimals = row[4]
        WithTumours = row[5]

        print ('DoseRespID:%s, ObsID:%s, Dose:%s, DoseUnit:%s, TotalAnimals:%s,WithTumours:%s'%(DoseRespID, ObsID, Dose, DoseUnit, TotalAnimals,WithTumours))

except pymysql.Error as e:
    print ("Connection failed" +str(e))
    db.rollback()

db.close()
