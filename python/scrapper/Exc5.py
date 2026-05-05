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


def get_links(url, depth=1, results=set()):
    if depth == 0:
        return results
    page = BeautifulSoup(requests.get(url).content, 'html.parser')
    links = page.find_all('a', href=True)

    for link in links:
        href = link["href"]
        if href.startswith("/wiki/") and not href.startswith("/wiki/Main_Page") and ':' not in href:
            full_url = f'https://en.wikipedia.org{href}'
            if full_url in results:
                continue
            results.add(full_url)
            get_links(full_url, depth - 1, results)
    return results


def main():
    url = 'https://en.wikipedia.org/wiki/Constantine%5F%28son%5Fof%5FTheophilos%29'
    url2 = 'https://en.wikipedia.org/wiki/Led_Zeppelin'
    url3 = 'https://en.wikipedia.org/wiki/Oshri_Roash'
    length = len(get_links(url3, 4))
    print(length)


if __name__ == '__main__':
    main()
