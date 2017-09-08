# -*- coding:utf-8 -*-
import tushare as ts 
from datetime import datetime
from datetime import timedelta
import pandas as pd
import numpy as np  
import matplotlib.pyplot as plt  

def get_mix_data(code,date,vol):
	df = ts.get_sina_dd(code,date,vol)

#获得基础数据
def get_min_data(code,date,vol):
	df = ts.get_tick_data(code,date)
	litte = df[df.volume<vol]
	return mmplb(litte)
	
#a==0为是买卖盘次数比，a!=0是主动盘与被动盘之比
def mmpcsb(code,date,vol):
	df = ts.get_tick_data(code,date)
	litte = df[df.volume<vol]
	#买卖盘次数统计
	cs = litte.groupby('type').size()
	#中性盘次数
	cs_m = cs['中性盘']
	#买盘次数
	cs_buy = cs['买盘']
	#卖盘次数统计
	cs_sell = cs['卖盘']
	scale_cs_bs = cs_buy/cs_sell
	#主动盘与中性盘之比
	scale_cs_b = (cs_buy+cs_sell)/cs_m
	if(a==0):
		return scale_cs_bs
	return scale_cs_b

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
	return date



def main(code,num):
	dates = []
	datas = []

	for i in range(num):
		date = get_data(i)
		lb = mmplb(code,date,200)
		if(isinstance(lb,int)):
			pass
		else:
			dates.append(date)
			datas.append(lb)
	datess = dates[::-1]
	datass = datas[::-1]

	df_t = pd.Series(datass,index=datess)
	f = df_t.plot(label="均价",color="red",linewidth=2)
	#plt.plot(dates,datas,label="均价",color="red",linewidth=2)
	plt.xlabel("时间")  
	#y轴名称
	plt.ylabel("均价")   
	plt.show(f)

main('002457',28)




	





