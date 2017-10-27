import qrcode

data = 'www.baidu.com'
img_file = r'/Users/liberty/Desktop/photo/py_qrcode.png'

img = qrcode.make(data)
# 图片数据保存至本地文件
img.save(img_file)
# 显示二维码图片
img.show()