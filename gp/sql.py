# -*- coding:utf8 -*-
import pymysql

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

connection = conn()
cursor = connection.cursor()

def inset(date,data):
    cursor.execute("INSERT INTO mmplb (date,data) VALUES(" + date +"," + data +")")
    #接收全部的结果行
    results = cursor.fetchall()
    return results
   

def delete(id):
    cursor.execute(" DELETE FROM mmplb WHERE id =  "+id)
    results = cursor.fetchall()
    return results

def close():
    cursor.close()
    connection.close()
 
delete('6')

connection.commit()
close()

'''
# -*- coding:utf-8 -*-
import pymysql


# 执行SQL，并返回收影响行数
#effect_row = cursor.execute("select * from tb7")
  
# 执行SQL，并返回受影响行数
#effect_row = cursor.execute("update tb7 set pass = '123' where nid = %s", (11,))
  
# 执行SQL，并返回受影响行数,执行多次
#effect_row = cursor.executemany("insert into tb7(user,pass,licnese)values(%s,%s,%s)", [("u1","u1pass","11111"),("u2","u2pass","22222")])
  
  
# 提交，不然无法保存新建或者修改的数据


insert_table_sql = """\
INSERT INTO fuck(username,nickname,birthday)
 VALUES('{username}','{nickname}','{birthday}')
"""

query_table_sql = """\
SELECT id,name
FROM blog_blog
"""

delete_table_sql = """\
DELETE FROM fuck 
"""

drop_table_sql = """\
DROP TABLE fuck
"""
def select(aa,bb):
    cursor.execute("SELECT " + aa +"," + bb +" FROM blog_blog")
    #接收全部的结果行
    results = cursor.fetchall()
    return results

'''

  

