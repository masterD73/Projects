# -------------------------
# title: 
# -------------------------
# -------------------------
# Description: 
# -------------------------
# ----------------------------
# Author: Daniel Merchav.
# Reviewer: 
# AI2 InfinityLabs.
# ----------------------------
import requests
from bs4 import BeautifulSoup


def get_languages(url):
    page_languages = []
    result = requests.get(url)
    soup = BeautifulSoup(result.content, 'html.parser')
    languages = soup.find_all(class_="interlanguage-link-target")
    for language in languages:
        page_languages.append(language.get('data-language-local-name'))
    return page_languages


def main():
    url = 'https://en.wikipedia.org/wiki/Jacobian_matrix_and_determinant'
    print(get_languages(url))
    print("Done.")


if __name__ == '__main__':
    main()
