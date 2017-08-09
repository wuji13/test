# -*- coding:utf-8 -*-
import numpy as np  
import matplotlib.pyplot as plt  
#x轴，y轴  

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
	plt.savefig("lot.jpg") 