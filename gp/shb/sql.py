# -*- coding:utf8 -*-
import pymysql

def conn():
	config = {
			'host':'127.0.0.1',
			'port':3306,
			'user':'root',
			'password':'test1234',
			'db':'gp',
			'charset':'utf8',
			}
	connection = pymysql.connect(**config)
	return connection

conn = conn()
cursor = conn.cursor()

def inset(date,data):
	cursor.execute("INSERT INTO mmplb (date,data) VALUES(" + date +"," + data +")")
	#接收全部的结果行
	results = cursor.fetchall()
	return results
   

def delete(id):
	cursor.execute(" DELETE FROM mmplb WHERE id =  "+id)
	results = cursor.fetchall()
	return results

def select(id):
    cursor.execute("SELECT * FROM mmplb WHERE id = "+id)
    #接收全部的结果行
    results = cursor.fetchall()
    return results

def close(cursor,connection):
	cursor.close()
	connection.close()

fffff = select('3')
ff = fffff[0]

print(ff[2])

