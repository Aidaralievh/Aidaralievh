import requests
from bs4 import BeautifulSoup

URL = "https://animevost.org"


def get_html(url, params=""):
    r = requests.get(url, params=params)
    return r


def take_content(html):
    soup = BeautifulSoup(html, "html.parser")
    text = soup.find_all("div", class_='shortstory')
    anime = []
    for i in text:
        anime.append({
            'name_anime': i.find("div", class_='shortstoryHead').find('a').text,
            'name_link': i.find('div', class_='shortstroyHead').find('a').get('href'),
            'ani_img': i.find('div', class_='shortstoryContent').find('img').get('src'),
            "short_story": i.find("div", id_="shortstoryContent").get_text(strip=True),
            }
        )
        return anime

html = get_html(URL)
take_content(html.content)
