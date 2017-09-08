# -*- coding:utf-8 -*-

import tushare as ts 
from draw import draw  
import numpy as np  
import matplotlib.pyplot as plt  

df = ts.get_h_data('002457', autype=None) #不复权

v = df.volume
a = df.amount
close = df.close
price = a/v
f = df['close'].plot()
p = price.plot()
plt.xlabel("时间")  
	#y轴名称
plt.ylabel("均价")   
plt.show(f)
plt.show(p)
