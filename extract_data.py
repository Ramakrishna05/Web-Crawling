# Extracting the data between two HTML tags #

import sys
import re
from os import listdir

dir_in = sys.argv[1]
dir_out = sys.argv[2]

files_list = [f for f in listdir(dir_in)]
remove_html_tags = re.compile('<.*?>|\t')
remove_extra_chars = re.compile(r"\s|[\t*]|[\n*]")

print("Cleaning the raw HTML files")
print("Getting files... done")
print("Extracting data")

for f in files_list:
    file_in = dir_in + f
    file_out = dir_out + f + ".out"
    print("Processing file: %s" % file_in)
    print("Writing output to file: %s" % file_out)

    file_in = open(file_in, 'r', encoding='utf-8')
    file_out = open(file_out, 'w', encoding='utf-8')

    data_in = file_in.read()

    clean = re.sub(remove_html_tags, '', data_in)
    clean = clean.strip()
    lines = clean.split("\n")

    free_data = []
    for line in lines:
        if len(line) > 0:
            temp_line = re.sub(remove_extra_chars, ' ', line)
            temp_line = temp_line.strip()
            #temp_line = re.sub("\n+", '', temp_line)
            file_out.write("%s\n" % temp_line)

print("Done")
