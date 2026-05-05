# -------------------------
# title: Languages Crawler
# -------------------------
# -------------------------
# Description: 
# -------------------------
# ------------------------------
# Author: Daniel Merchav.
# Reviewer: Alexander-Volkovich.
# AI2 InfinityLabs.
# ------------------------------
from bs4 import BeautifulSoup
import requests


def page_word(url):
    page = BeautifulSoup(requests.get(url).content, 'html.parser').get_text(strip=True).split(' ')
    return sorted(page, key=len)


def main():
    url = "https://en.wikipedia.org/wiki/Jacobian_matrix_and_determinant"
    print(page_word(url))


if __name__ == '__main__':
    main()
