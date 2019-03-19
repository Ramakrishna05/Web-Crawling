# Submitting the form and Scraping the webpage

import os
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import bs4 as bs
import re

file_in = open("./word_list.txt", 'r', encoding='utf-8')
file_out = open(
    "../crawl_data/Shabdkosh_dict/eng_tel_meanings.txt", 'w', encoding='utf-8')

word_list = file_in.read().split("\n")

remove_html_tags = re.compile('<.*?>|\t')

browser = webdriver.Firefox()
browser.get('http://www.shabdkosh.com/te/')

# browser.find_element_by_id("radioEn").click()

search_box = browser.find_element_by_id("e")
# word = "paper"

for word in word_list:
    search_box.clear()
    search_box.send_keys(word)
    browser.find_element_by_css_selector(
        ".btn.btn-default.btn-up.sbutton").click()
    time.sleep(7)
    data = browser.page_source
    soup = bs.BeautifulSoup(data, 'lxml')
    meanings = soup.find_all("ol", class_="eirol", id=False)
    # print(meanings)
    # print(soup)
    clean = re.sub(remove_html_tags, '', str(meanings))
    # print(clean)
    file_out.write("%s: %s\n" % (word, clean))
    search_box = browser.find_element_by_id("e")

print("Done")
