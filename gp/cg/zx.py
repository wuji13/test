import pandas as pd

def sj(mi,ma):
	data_basic = pd.read_excel(r'/Users/liberty/Desktop/ok/top_20170901.xlsx','Sheet1',na_values=['NA'])
	data_zx = pd.read_excel(r'/Users/liberty/Desktop/ok/zxg.xlsx','Sheet1',na_values=['NA'])

	


	data_zj = data_zd[data.changepercent < ma]

	for i in range(len(data_zj.index)):
		da = str(data_zj.iloc[[i],[0]])
		print(da)




	#排序by按照某列数据，进行ascending为0为降序，为1为升序
	p = data_zj.sort_values(by=['turnoverratio'] , ascending = [0]).head(10)
	print(p)
	#p.to_excel(r'/Users/liberty/Desktop/ok/te.xlsx',sheet_name = 'Sheet1')