# -*- coding:utf8 -*-
import tushare as ts 
from datetime import datetime
from datetime import timedelta
import pymysql
import time

def main(code,num):
	global conn
	global cursor
	conn = conn()
	cursor = conn.cursor()

	for i in range(num):
		date = get_data(i)
		da = str(get_da(i))

		lb = mmplb(code,date,200)
		print(da)
		if(isinstance(lb,int)):
			time.sleep(15)
			continue
		else:
			nb = str(lb)
			inset(da,nb)
			conn.commit()
	close()

#获得基础数据
def get_min_data(code,date,vol):
	df = ts.get_tick_data(code,date)
	litte = df[df.volume<vol]
	return mmplb(litte)


#买卖盘量比
def mmplb(code,date,vol):
	#买卖盘量统计
	df = ts.get_tick_data(code,date = date,pause = 1)
	if (len(df) == 3):
		return 0
	else:
		litte = df[df.volume<vol]
		count = litte.groupby('type').sum()
		count_buy = count.loc['买盘','volume']
		count_sell = count.loc['卖盘','volume']
		#买卖盘量比
		scale_count_bs = count_buy/count_sell
		return scale_count_bs

#输出从当天前n天的日期
def get_data(n):
	d = datetime.today() - timedelta(days = n)
	date = d.strftime('%Y-%m-%d')
	da = d.strftime('%Y%m%d')
	return date

def get_da(n):
	d = datetime.today() - timedelta(days = n)
	da = d.strftime('%Y%m%d')
	return da

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

def inset(date,data):
	cursor.execute("INSERT INTO testdb (date,data) VALUES(" + date +"," + data +")")
	#接收全部的结果行
	results = cursor.fetchall()
	return results

def close():
	cursor.close()
	conn.close()

main('600704',100)


	
