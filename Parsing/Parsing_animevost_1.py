import requests
from bs4 import BeautifulSoup
import csv


HOST = "https://animevost.org"
URL = "https://animevost.org/favorites/"
HEADERS = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,"
              "application/signed-exchange;v=b3;q=0.9",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/86.0.4240.198 Safari/537.36 OPR/72.0.3815.465 "
}


def get_html(url, params=""):
    r = requests.get(url, headers=HEADERS, params=params)
    return r


def get_content(html):
    soup = BeautifulSoup(html, "html.parser")
    items = soup.find_all("div", class_="shortstory")
    cards = []
    print(items)



html = get_html(URL)
get_content(html.text)
