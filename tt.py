import tushare as ts 

df = ts.get_tick_data('000965',date='2017-08-03')
p = df.amount
p[1]
s=0
for i in range(0,3049):
	s=p[i]+s
print(s)
b=p.index

print(b)