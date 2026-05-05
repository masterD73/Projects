# -------------------------
# title: LinkedIn Crawler
# -------------------------
# -------------------------
# Description: 
# -------------------------
# ------------------------------
# Author: Daniel Merchav.
# Reviewer: Alexander Volkovich.
# AI2 InfinityLabs.
# ------------------------------
from time import sleep
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.edge.options import Options


def get_jobs():
    roles = []
    index = 0
    options = Options()
    url = "https://il.linkedin.com/company/linkedin/jobs"
    options.edge_executable = "/Users/merda/Desktop/msedgedriver.exe"
    driver = webdriver.Edge(options=options)
    driver.get(url)
    sleep(3)
    x = driver.find_element(By.CSS_SELECTOR,
                            '#base-contextual-sign-in-modal > div > section > button > icon > svg')
    x.click()
    jobs = driver.find_element(By.CSS_SELECTOR,
                               '#main-content > section.core-rail.mx-auto.papabear\\'
                               ':w-core-rail-width.mamabear\\:max-w-\\[790px\\].babybear\\'
                               ':max-w-\\[790px\\] > div > section > div > ul').find_elements(By.TAG_NAME, 'a')
    for job in jobs:
        index += 1
        try:
            roles.append((job.find_elements(By.CLASS_NAME, 'sr-only')[0].text,
                          driver.find_element(By.CSS_SELECTOR,
                                              f'#main-content > section.core-rail.mx-auto.papabear\\'
                                              f':w-core-rail-width.mamabear\\:max-w-\\[790px\\].babybear\\'
                                              f':max-w-\\[790px\\] > div > section > div > ul > li:nth-child({index})'
                                              f' > div > div > h4 > a').text,
                          job.get_attribute('href')))
        except Exception:
            continue
    return roles


def main():
    print(get_jobs())
    print("Done")


if __name__ == '__main__':
    main()
