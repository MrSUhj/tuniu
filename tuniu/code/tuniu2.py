import requests
from bs4 import BeautifulSoup


def got_html(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) '

                             'Chrome/69.0.3497.100 Safari/537.36'}

    # url = 'http://s.tuniu.com/search_complex/whole-nj-0-%E6%B3%B0%E5%9B%BD/'

    response = requests.get(url, headers=headers)

    html = response.content.decode()

    # print(html)

    return html


def parse_html(html):
    soup = BeautifulSoup(html, 'lxml')

    item_list = soup.select('ul[class="thebox clearfix"] li')

    print(len(item_list))

    for item in item_list:
        # 名称

        name = item.select('div > a > dl > dt > p.title > span')[0].get_text().strip()

        # 价格

        price = item.select('div > a > div.priceinfo > div.tnPrice > em')[0].get_text().strip()

        # 满意度

        dos = item.select('div > a > div.priceinfo > div.comment-sat.clearfix > div.comment-satNum > span > i')[
            0].get_text().strip()

        # 出游人数

        number = item.select('div > a > div.priceinfo > div.comment-sat.clearfix > div.trav-person > p.person-num > i')[
            0].get_text().strip()

        print(name, price, dos, number)


content = got_html('http://s.tuniu.com/search_complex/whole-nj-0-%E6%B3%B0%E5%9B%BD/')

parse_html(content)
