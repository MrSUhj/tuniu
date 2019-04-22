# 3，利用正则表达式快速的打印出网页的标题跟链接地址
import re
fp = open('D:\\python_exec\\tuniu.txt', 'rb')
content = fp.read().decode('utf-8')
fp.close()

title = re.search('<title>(.*?)</title>', content, re.S).group(1)

print('title = ', title + '\n')

hrefPatten = 'href="(.*?)"'

hrefC = re.findall(hrefPatten, content, re.S)  # 返回所有匹配正则表达式的值于列表中

print('Allhref = ', hrefC)

for h in hrefC:
    print(h)
