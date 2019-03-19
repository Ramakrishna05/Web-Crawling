# Submitting the form and Scraping the webpage

import os
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import bs4 as bs

file_in = open("./meanings_soup.txt", 'w', encoding='utf-8')

browser = webdriver.Firefox()
browser.get('http://www.shabdkosh.com/')

# browser.find_element_by_id("radioEn").click()

datePicker = browser.find_element_by_id("e")
date = "paper"
for i in range(1):
    datePicker.clear()
    datePicker.send_keys(date)
    browser.find_element_by_css_selector(
        ".btn.btn-default.btn-up.sbutton").click()
    time.sleep(1)
    data = browser.page_source
    soup = bs.BeautifulSoup(data, 'lxml')
    meanings = soup.find_all("ol", class_="eirol", id=False)
    print(meanings)
    # print(soup)
    file_in.write("%s\n" % meanings)
    date = "2013/08/03"
