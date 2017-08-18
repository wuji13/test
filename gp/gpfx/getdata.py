# -*- coding:utf8 -*-

#问题：不能夸日，每次循环都是取得最新的日期，要修改
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
	s = 0
	tday = datetime.today() 

	for i in range(num):
		d = get_data(tday,num,i)
		date = d[0]
		da = d[1]


		lis = mmplb(code,date,200)
		print(da)
		if(isinstance(lis,int)):
			time.sleep(10)
			continue
		else:
			s = s+1
			bslb = str(lis)
			inset(da,bslb)
			conn.commit()
			print(s)
	close()




#获得基础数据
def get_min_data(code,date,vol):
	df = ts.get_tick_data(code,date)
	litte = df[df.volume<vol]
	return mmplb(litte)


#买卖盘量比
def mmplb(code,date,vol):
	global count_buy
	global count_sell
	#买卖盘量统计
	global cs_m
	df = ts.get_tick_data(code,date = date,pause = 1)
	if (len(df) == 3):
		return 0
	else:
		litte = df[df.volume<vol]
		count = litte.groupby('type').sum()
		
		if (len(count) == 1 and count.index[0]=='买盘'):
			count_buy = count.loc['买盘','volume']
			count_sell = count_buy/3
			print(a)


		elif (count.index[0]=='买盘'):
			count_buy = count.loc['买盘','volume']
			count_sell = count.loc['卖盘','volume']
			print(b)

		elif (count.index[0]=='卖盘'):
			count_sell = count.loc['卖盘','volume']
			count_buy = count_sell/3
			print(c)


		#买卖盘量比
		scale_count_bs = count_buy/count_sell
		#次数统计
		#cs = litte.groupby('type').size()
		#买盘次数
		#cs_buy = cs['买盘']
		#卖盘次数统计
		#cs_sell = cs['卖盘']
		#中性盘次数
		#if(len(cs) == 3):
		#	cs_m = cs['中性盘']
		#else:
		#	cs_m = 1
		#买盘次数与卖盘次数比
		#scale_cs_bs = cs_buy/cs_sell
		#主动盘与中性盘之比
		#scale_cs_b = (cs_buy+cs_sell)/cs_m
		return scale_count_bs

#输出从当天前n天的日期,n天为总数，x为相差的天数
def get_data(tday,n,i):
	d = tday - timedelta(days = n - i)
	date = d.strftime('%Y-%m-%d')
	da = d.strftime('%Y%m%d')
	return date,da



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

def inset(date,bslb):
	cursor.execute("INSERT INTO sh_000778 (date,bslb) VALUES (" + date +"," + bslb  +")")
	#接收全部的结果行
	results = cursor.fetchall()
	return results

def close():
	cursor.close()
	conn.close()

main('000778',133)


	
