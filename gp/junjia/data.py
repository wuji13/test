# -*- coding:utf-8 -*-

import tushare as ts 
from draw import draw  

df = ts.get_h_data('002457', autype=None) #不复权

v = df.volume
a = df.amount

s = []
d = []
x=len(a)
for i in range(0,x):
	p = round(a[i]/v[i],1)
	s.append(p)
	d.append(i)


print(s[1])
print(type(s))
draw(d,s)