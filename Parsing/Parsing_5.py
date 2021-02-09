import requests
from bs4 import BeautifulSoup

URL = 'https://www.anilibria.tv/pages/catalog.php'


def get_html(url):
    r = requests.get(url)
    return r


def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.findALL("div", class_='margin-top: 12px;')
    cards = []
    print(items)

    # for item in items:
    #      # name = item.find('div', class_='th-title').text,
    #      link = item.find('div', class_='torrent_pic').find('a').get('href'),
    #      # img = item.find('div', class_='/uploads/posts/2021-01/1609587207_3-1.jpg').find('img').get('src')
    #      # cards.append(name),
    #      cards.append(link)
    #     # cards.append(img)
    # print(cards)

    html = get_html(URL)
    get_content(html.content)