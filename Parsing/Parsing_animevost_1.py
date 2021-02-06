import requests
from bs4 import BeautifulSoup

URL = "https://animevost.org"
HEADERS = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,"
              "application/signed-exchange  ;v=b3;q=0.9",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/86.0.4240.198 Safari/537.36 OPR/72.0.3815.465 "
}


def get_html(url):
    r = requests.get(url, headers=HEADERS)
    return r


def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.findAll('div', class_='shortstory')
    comps = []
    print((items))

    # for item in items:
    #     title = item.find("div", class_="shortstoryHead").find("a").text,
    #     link_product = item.find("div", class_="shortstoryHead").find("a").get("href"),
    #     ani_img = item.find("div", class_="shortstoryContent").find("img").get("src")
    #     comps.append(title),
    #     comps.append(link_product),
    #     comps.append(ani_img),
    #
    # print(comps)


html = get_html(URL)
get_content(html.text)
