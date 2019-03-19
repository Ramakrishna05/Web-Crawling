# National Translation Mission Translators Database Crawler #
# Author: A. Ramakrishna #
# Date: 17 February, 2019 #
# Base url: http://www.ntm.org.in/languages/english/nrtdb.aspx #

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
link = "http://www.ntm.org.in/languages/english/search_nrtdetails.aspx?regid="

# regular expression for cleaning the html tags #
clean_tags = re.compile('<.*?>')

# crawling the links
print("Crawling is started!")
for i in range(6601, 6651):
    next_link = link + str(i)
    #print("Crawling link %s" %(next_link))
    fname = './Database/' + str(i)
    fin = open(fname, 'w', encoding='utf-8')
    response = http.request('GET', next_link)
    soup = bs(response.data, 'lxml')
    divTag = soup.find_all("div", {"class": "formdetailsbg"})
    
    # extracting data
    for tag in divTag:
        #print(tag)
        trtag = tag.find_all("tr")
        temp = re.sub(clean_tags, '', str(trtag)).split('\n')
        
        # writing into file
        for ele in temp:
            #print(ele)
            fin.write("%s\n" %ele)
            
    fin.close()

    if i%25 == 0:
        print("%d pages crawled so far" %i)
        print("Time established: %0.3f" %(time.time() - start_time))

# total statistics of the crawling
print("Total %d pages crawled" %i)
print("Total time established: %0.3f" %(time.time() - start_time))