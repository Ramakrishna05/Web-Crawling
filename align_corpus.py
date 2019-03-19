# Alignment of sentences in two languages as a parallel corpus #

import sys
#import nltk
#from nltk import sent_tokenize

in_file_eng = sys.argv[1]
in_file_tel = sys.argv[2]
out_file_com = sys.argv[3]

in_file_eng = open(in_file_eng, 'r', encoding='utf-8')
in_file_tel = open(in_file_tel, 'r', encoding='utf-8')
out_file_com = open(out_file_com, 'w', encoding='utf-8')

eng_data = in_file_eng.read()
tel_data = in_file_tel.read()

eng_sents = eng_data.split(".")
tel_sents = tel_data.split(".")
print(len(eng_sents))
print(len(tel_sents))

i = 0
while i < len(eng_sents):
    out_file_com.write("%s||%s\n" % (eng_sents[i], tel_sents[i]))
    i += 1
