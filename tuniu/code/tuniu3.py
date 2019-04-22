import requests
from bs4 import BeautifulSoup

url = requests.get('https://go.hao123.com')  # 请求这个网址
soup = BeautifulSoup(url.content, "lxml")  # 解析网址
# print(soup)  #可以查看HTML源代码
images = soup.select('body > div.content-outer-wrapper > div > div > div > div > div > div > div > a > img')
prices = soup.select(
    'body > div.content-outer-wrapper > div > div > div.tejia-menpiao > div.container > div > div > div.price > a > div.new')
names = soup.select(
    'body > div.content-outer-wrapper > div > div > div.tejia-menpiao > div.container > div > div > div.pic > a > div')

data = {}
# 三个同时遍历用到zip()
for name, price, image in zip(names, prices, images):
    data = {
        'name': name.get_text(),
        'price': price.get_text(),
        'img': image.get('src')
    }
    print(data)  # 遍历列表，并用字典存储
