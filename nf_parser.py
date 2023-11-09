import requests
from bs4 import BeautifulSoup
import pprint
from bs4.element import Tag


URL = "https://www.nfactorial.live/"


def get_html(URL, headers=[]):
    r = requests.get(URL)
    if r.status_code == 200:
        return r.text


def get_projects(soup:BeautifulSoup):
    mydivs:Tag = soup.find_all("div", {"class": "project-card"})
    iframe:Tag = mydivs[0].find("iframe")
    print(iframe)
    print(iframe.get("src"))


def nf_parse():
    r = get_html(URL)
    soup = BeautifulSoup(r, 'html.parser')
    get_projects(soup)


nf_parse()