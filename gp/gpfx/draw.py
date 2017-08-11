# -*- coding:utf8 -*-
import numpy as np  
import matplotlib.pyplot as plt  
import pymysql

def main(star,end):
	global conn
	global cursor
	dates = []
	datas = []
	conn = conn()
	cursor = conn.cursor()

	for i in range(end - star + 1):
		td =select(end-i)
		tdd = td[0]
		date = tdd[2]
		data = tdd[3]
		dates =dates.append(date)
		datas =dates.append(data)

	close()


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

def select(id):
	
    cursor.execute("SELECT * FROM mmplb WHERE id = "+id)
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
	plt.figure(figsize=(200,100))  
	#在当前绘图对象中画图（x轴,y轴,给所绘制的曲线的名字，画线颜色，画线宽度）  
	plt.plot(x,y,label="均价",color="red",linewidth=2)
	#在当前绘图对象进行绘图（两个参数是x,y轴的数据）  
	plt.plot(x,y)  
	#保存图象  
	plt.show()





main(53,122)

