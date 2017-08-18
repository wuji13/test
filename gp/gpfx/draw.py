# -*- coding:utf8 -*-
import numpy as np  
import matplotlib.pyplot as plt  
import pymysql
import time
import pandas as pd
from pandas import Series,DataFrame

def main():
	global conn
	global cursor
	conn = conn()
	cursor = conn.cursor()

	rows = select()
	close()
	#数据库数据转换为dataframe
	df = pd.DataFrame([ij for ij in i] for i in rows)
	df.rename(columns={0:'id',1:'date',2:'bslb',3:'bscb',4:'bmcb'},inplace = True)

	dates = df['date'].values
	bslbs = df['bslb'].values

	dd = dates.tolist()
	bs = bslbs.tolist()

	#ob = pd.DataFrame([ij for ij in i] for i in rows,index = dd, columns = ['id','date','bslb','bscb','bmcb'])
	#print(ob)
	print(dd)
	draw(dd,bs)
	#xx = df['bslb']


	#xx.plot() 
	#plt.show(xx)



def conn():
	config = {
			'host':'127.0.0.1',
			'port':3306,
			'user':'root',
			'passwd':'test1234',
			'db':'gp',
			'charset':'utf8',
			}
	connection = pymysql.connect(**config)
	return connection

def select():
	
    cursor.execute("SELECT * FROM mmplb")
    #接收全部的结果行
    results = cursor.fetchall()
    return results

def close():
	cursor.close()
	conn.close()

def draw(x,y):
	#x轴名称
	plt.xlabel("时间")  
	#y轴名称
	plt.ylabel("均价")  
	#图的标题
	plt.title("A simple plot")    
	#创建绘图对象  
	#创建绘图对象，figsize参数可以指定绘图对象的宽度和高度，单位为英寸，一英寸=80px
	plt.figure(figsize=(20,10))  
	#在当前绘图对象中画图（x轴,y轴,给所绘制的曲线的名字，画线颜色，画线宽度）  
	plt.plot(x,y,label="均价",color="red",linewidth=2)
	#在当前绘图对象进行绘图（两个参数是x,y轴的数据）  
	plt.plot(x,y)  
	#保存图象  
	plt.show()

main()

