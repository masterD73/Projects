# -------------------------
# title: Email Crawler
# -------------------------
# -------------------------
# Description:
# -------------------------
# ------------------------------
# Author: Daniel Merchav.
# Reviewer: Alexander-Volkovich.
# AI2 InfinityLabs.
# ------------------------------
import requests
from bs4 import BeautifulSoup
import schedule
from time import sleep
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.edge.options import Options


def read_email(url, email, password):
    options = Options()
    options.edge_executable = path = "/Users/merda/Desktop/msedgedriver.exe"
    driver = webdriver.Edge(options=options)
    driver.get(url)
    sleep(2)
    login = driver.find_element(By.CSS_SELECTOR, "#login")
    login.click()
    login.send_keys("dan_007@netvision.net.il")
    password = driver.find_element(By.CSS_SELECTOR, "#password")
    password.click()
    password.send_keys(password)
    enter = driver.find_element(By.CSS_SELECTOR, "#submit")
    enter.click()
    sleep(2)
    emails = driver.find_elements(By.CLASS_NAME, 'wm_inbox_read_item')
    emails[0].click()


def main():
    url = "website"
    email = "email"
    password = "password"
    read_email(url, email, password)
    print("Done.")


if __name__ == '__main__':
    main()
