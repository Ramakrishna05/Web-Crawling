# A simple way to access webpage using urllib #
# Author: A. Ramakrishna #
# Date: 31 January, 2019 #
# Base url: Bharatavani Dictionaries #

import urllib3
import bs4
from bs4 import BeautifulSoup as bs
import re
import lxml
import time

# starting the clock
start_time = time.time()

# getting the page #
http = urllib3.PoolManager()
i = 1
j = 1
link = "http://bharatavani.in/dictionary-surf/?did=29&language=English"

# regular expression for cleaning the h4 and p tags #
clean_tags = re.compile('<.*?>')

# saving data into two dictionaries
final_dict_te = {}
final_dict_others = {}

# opening file to save dictionary
fin = open("./te-kn_en.txt", 'a', encoding="utf-8")

# getting pages
print("Crawling is started!")
for i in range(1,524):
    next_link = link+"&page="+str(i)
    response = http.request('GET', next_link)
    soup = bs(response.data, 'lxml')
    divTag = soup.find_all("div", {"class": "wordbox small-12 large-12 columns"})
    
    #h4 tag contains the English words
    #p tag contains the Kannada words
    for tag in divTag:
        h4Tag = tag.find_all("h4")
        final_dict_te[j] = re.sub(clean_tags, '', str(h4Tag))
        pTag = tag.find_all("p")
        ulTag = tag.find_all("ul")
        final_dict_others[j] = re.sub(clean_tags, '', str(pTag)) + re.sub(clean_tags, '', str(ulTag))
        
        # writing the data into the file
        fin.write("%s:" %(final_dict_te[j]))
        temp = final_dict_others[j].split(',')
        for element in temp:
            fin.write("%s," %element)
        fin.write("\n*****\n")

        j += 1

    if i % 25 == 0:
        print("%d words crawled so far..." %(len(final_dict_te.keys())))
        print("%0.3f seconds took so far..." %(time.time() - start_time))
        print("Crawling link:%s" %next_link)

'''    
# writing the dictionary into the file
limit = len(final_dict_en.keys()) + 1

for i in range(1,limit):
    fin.write("%s:" %(final_dict_en[i]))
    temp = final_dict_kn[i].split(',')
    for element in temp:
        fin.write("%s," %element)
    fin.write("\n*****\n")
'''

print("Writing to file success")

# statistics of the crawling
print("No.of records: %d" %len(final_dict_te))
print("Total time taken in seconds: %0.5f" %(time.time() - start_time))
