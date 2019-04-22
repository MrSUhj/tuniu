import urllib.request
# 1,获取网页源代码
url = 'http://www.tuniu.com'

wp = urllib.request.urlopen(url)
file_content = wp.read()

print(file_content)
# 2,将网页内容存入文件中
fp = open('tuniu.txt', 'wb') #打开一个文本文件

fp.write(file_content) #写入数据

fp.close() #关闭文件

