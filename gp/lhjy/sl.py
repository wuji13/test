import talib
import numpy as np
import math
import pandas
import time 
import datetime 
from functools import reduce 

# 初始化信息
def init(context):
    #滑点默认值2‰
    context.set_slippage(0.002)
    #交易费默认值0.25‰
    context.set_commission(0.00025)
    #基准默认沪深300
    context.set_benchmark("000300.SH")
    
    #目前策略默认分钟数据为收盘前8分钟进行买卖，天数据为收盘买卖
    #task.daily(option_stock,time_rule=market_close(minute=8))
    #下面为几个定时执行的策略代码，可放开注释替换上面的执行时间
    task.daily(option_stock, time_rule=market_open(minute=0.1))  #每天开盘后5分钟运行
    #task.weekly(option_stock, weekday=2, time_rule=market_open(minute=5))  #每周周二开盘后5分钟运行
    #task.monthly(option_stock,tradingday=1 ,time_rule=market_open(minute=5))  #每月第1个交易日开盘后5分运行

#每天开盘前进行选股    
def before_trade(context):
    context.stock_list = choose_stock_finance()
    
#日或分钟或实时数据更新，将会调用这个函数
def handle_data(context,data_dict):
    #option_stock(context,data_dict)
    pass

#操作股票
def option_stock(context,data_dict):
    stock_list = context.stock_list
    sell_stock(context,stock_list,data_dict)  #先卖出股票再买入
    for stock in stock_list:
        buy_stock(context,stock,data_dict)  #买入股票

#策略买入信号函数
def buy_stock(context,stock ,data_dict):
    max_position = 0.2  #最大买入仓位 
    stock_buy_num = 5 #最多买入5支股票
    stock_percentage = 0.99/stock_buy_num  #每支股票买入的最大仓位
    if len(context.portfolio.positions) < stock_buy_num:
       cash = context.portfolio.cash #当前投资当前投资组合剩余现金
       portfolio_value = context.portfolio.portfolio_value  #总资产包含剩余现金与市场价值
       quantity = context.portfolio.positions[stock].quantity   #总股数
       price_value = data_dict[stock].last   #新价格 
       p_value = price_value*quantity
       stock_position = p_value/portfolio_value
       if p_value/portfolio_value < max_position and cash/portfolio_value > max_position:
          order_target_percent(stock, max_position) #买入股票

#策略卖出信号函数
def sell_stock(context,stock_list,data_dict):
    for stock in list(context.portfolio.positions.keys()):
        if not (stock in stock_list):
           order_target_value(stock,0)  #如果不在股票列表中则全部卖出
           print(context.portfolio.positions[stock])

#选股函数
def choose_stock_finance():
    dataframe = get_fundamentals(
     query(
         fundamentals.equity_valuation_indicator.market_cap_2   #总市值
     ).filter(
         fundamentals.equity_valuation_indicator.market_cap_2 < 20000000000  #总市值小说200亿
     ).order_by(
        fundamentals.equity_valuation_indicator.market_cap_2.asc()  #DESC降序asc升序
     ).limit(20) #选择结果的前20只股票 
    )
    stock_list = dataframe.columns.values
    print(stock_list)
    return stock_list

