import tushare as ts

def get_data():
	data = ts.get_today_all()
	data.to_excel(r'/Users/liberty/Desktop/ok/top_20170907.xlsx',sheet_name = 'Sheet1')

get_data()