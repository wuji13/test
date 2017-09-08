#coding:utf-8
#这是获取固定有效地址

import urllib.request  
import time  


opener = urllib.request.build_opener()  

def main():
	for i in range(10000):
		a = 20000+i
		s = str(a)
		url = wz(s)
		jc(url)
		time.sleep(0.001)



def wz(num):
 	url = 'http://61.222.131.65:8080/vod/mp4:' + num + '.mp4/playlist.m3u8'
 	return url


def jc(url): 
    try :
        opener.open(url)  
        print(url+'没问题')
        with open('/Users/liberty/Desktop/ok/xx.txt', 'a') as f:
        	f.write(url+'\n')  
    except urllib.error.HTTPError:
        print(url+'=访问页面出错')  
    except urllib.error.URLError:
        print(url+'=访问页面出错')  



main()