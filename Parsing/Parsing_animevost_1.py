import requests
from bs4 import BeautifulSoup


URL = "https://animevost.org"

def get_html(url):
    r = requests.get(url)
    return r


def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.findAll('div', class_='shortstory')
    comps = []


    for item in items:
        name =  item.find("div", class_="shortstoryHead").find("a").text,
        link = item.find("div", class_="shortstoryHead").find("a").get("href"),
        src =  item.find("div", class_="shortstoryContent").find("img").get("src")
        comps.append(name)
        comps.append(link)
        comps.append("https://animevost.org"+src)
    print(comps)



html = get_html(URL)
get_content(html.text)

