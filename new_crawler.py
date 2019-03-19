# Crawler on Andhra Bank and PM Modi website #
# Same for both of the websites #

import bs4
import lxml
import sys
import requests

in_file = sys.argv[1]
in_file = open(in_file, 'r')

links = in_file.read().split("\n")

i = 0
j = 0

print("Got the links... now crawling the webpages!")

while i < len(links) or i == len(links):
    file_name = "./crawl_data/PM_India/p_tags/" + str(j+1)
    urlE = links[i]
    urlH = links[i+1]
    urlT = links[i+2]

    resE = requests.get(urlE, timeout=15)
    resH = requests.get(urlH, timeout=15)
    resT = requests.get(urlT, timeout=15)

    soupE = bs4.BeautifulSoup(resE.text, 'lxml')
    soupH = bs4.BeautifulSoup(resH.text, 'lxml')
    soupT = bs4.BeautifulSoup(resT.text, 'lxml')

    eng_text = soupE('p')
    hin_text = soupH('p')
    tel_text = soupT('p')

    temp_eng_file = open(file_name+'.eng', 'w', encoding='utf-8')
    temp_hin_file = open(file_name+'.hin', 'w', encoding='utf-8')
    temp_tel_file = open(file_name+'.tel', 'w', encoding='utf-8')
    temp_eng_file.write("%s" % eng_text)
    temp_hin_file.write("%s" % hin_text)
    temp_tel_file.write("%s" % tel_text)

    i += 3
    j += 1

    percent_links = (i / len(links)) * 100

    print("%f percent of links have crawled" % (percent_links))
print("Done")
