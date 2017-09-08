#!/usr/bin/python
# encoding:utf-8

import requests, json
import pandas as pd

def main():
	github_url = 'http://f.apiplus.net/ssq-20.json'
	r = requests.get(github_url)
	data = json.loads(r.text)
	final = pd.DataFrame(data)
	code = final.data
	values = code.values
	#print(code)
	lis = values.tolist()
	dic = lis[1]
	#得到开奖号
	opencode = dic['opencode']
	#得到开奖期数
	period = dic['expect']
	#得到开奖时间
	date = str(dic['opentime'])
	opcode_5 = opencode.split(",")
	opcode_2 = opcode_5[5].split("+")




def conn():
	config = {
			'host':'127.0.0.1',
			'port':3306,
			'user':'root',
			#有的是使用password
			'passwd':'test1234',
			'db':'gp',
			'charset':'utf8',
			}
	connection = pymysql.connect(**config)
	return connection

def inset(one,two,three,four,five,six,seven):
	cursor.execute("INSERT INTO sh_000778 (one,two,three,four,five,six,seven) VALUES (" + one + "," + two + "," + three+ "," + four+ "," + five+ "," + six+ "," + seven +")")
	#接收全部的结果行
	results = cursor.fetchall()
	return results

def close():
	cursor.close()
	conn.close()




print(type(r.text))
print(lis)