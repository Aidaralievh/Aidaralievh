import requests
from bs4 import BeautifulSoup
import csv

CSV = "ani_pars.csv"
HOST = "https://animevost.org"
URL = "https://animevost.org/page/2/"
HEADERS = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,"
              "application/signed-exchange  ;v=b3;q=0.9",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/86.0.4240.198 Safari/537.36 OPR/72.0.3815.465 "
}


def get_html(url, params=""):
    r = requests.get(url, headers=HEADERS, params=params)
    return r


def get_content(html):
    soup = BeautifulSoup(html, "html.parser")
    items = soup.find_all("div", id_="dle-content")
    cards = []

    for item in items:
        cards.append(
            {
                "title": item.find("div", id_="shortstoryHead").get_text(strip=True),
                "link_product": HOST + item.find("div", id_="shortstoryHead").find("a").get("href"),
                "short_story": item.find("div", id_="shortstoryContent").get_text(strip=True),
                "ani_img": HOST + item.find("div", id_="shortstoryContent").find("img").get("src"),

            }
        )
        return cards


def save_doc(items, path):
    with open(path, 'w', newline='') as file:
        writer = csv.writer(file, delimiter=";")
        writer.writerow(["name of anime", "link_of_product", "short_stories", "ani_img"])
        for item in items:
            writer.writerow([item["title"], item["link_product"], item["number_of_episodes"], item["ani_img"]])


def parser():
    PAGENATION = input("how many pages to parse: ")
    PAGENATION = int(PAGENATION.strip())
    html = get_html(URL)
    if html.status_code == 200:
        cards = []
        for page in range(1, PAGENATION):
            print(f'parsing page: {page}')
            html = get_html(URL, params={'page': page})
            cards.extend(get_content(html.text))
            print(cards)
            # save_doc(cards, CSV)
        pass
    else:
        print("Error")


parser()

html = get_html(URL)
get_content(html.text)
