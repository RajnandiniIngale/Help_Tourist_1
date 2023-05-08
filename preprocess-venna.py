import csv

import nltk

from nltk import word_tokenize
from nltk.corpus import stopwords

#create dataframe read csv file & save file in csv format

import pandas as pd
import numpy as np

#read csv file

data = pd.read_csv('venna.csv')

arr = data.to_numpy()   #convert csv data into array


overall = ["smelly","life ","visit","Beautiful ","Lake","enjoy ","time","happy ","boat","trip","Great ","family","Boating","horse riding",
           "attraction","fresh","near","like ","favourite ","big ","boat","ride","Nice ","natural ","avoid ","Average ","evening","Excellent ",
           "crowd ","ample ","serene ","horse","rides","rains ","life time","experience","cloud ","monsoon ","season","heavy","rainfall",
           "difficult","extremely","satisfying ","mandatory ","options","prices ","fast food","available","boats ","food stalls","trip ",
           "raining ","fog","chilled weather","expensive","closed ","full of water","weekend","rush ","Affordable ","prices","cheaper ","recommended " ,
           "families"," warm sun","cool breeze"," life time ","cheap rates","crowdy","Popular ","facility ","Plenty","Lovely ","clean place",
           "worth","Best"," dream ","issue ","games ","tourists","lot","scenic ","picturesque","beauty "," fresh water","fun ","Excellent ",
           "scenic ","amusement ","expensive ","okay ","relax","problem ","unorganised","friendly","amazing ","surrounding ","nature","crowded ",
           "chill ","Charges","mesmerizing","free","over charge","cheat"," looting","dust ","lack ","clean","upliftment","Overhyped","Overcrowded ",
           "Overpriced ","calmness","exotic ","love ","cool","Famous ","commercialized ","crammed ","jam packed","pleasant ","not affordable",
           "mouthwatering ","fog","cleanliness ","excited ","recommend ","optimal ","waiting ","foggy ","available","climate ","extra ","more money",
           "mismanagement","sanitation ","mess ","long walk","peaceful "," leisurely","satisfying","high"," EXTRA MONEY","queue","loot","old ","freezes",
           "traffic ","scenes ","challange ","speciality ","Average ","huge","must-visit","tranquility","cooperative","trap ","Refreshing ","soothing ",
           "cost ","sunset","scenic ",""]

stop_words = set(stopwords.words('english'))



word_tokens = word_tokenize(str(arr))
# converts the words in word_tokens to lower case and then checks whether
# they are present in stop_words or not

filtered_sentence = [w for w in word_tokens if not w.lower() in stop_words]
# with no lower case conversion

filtered_sentence = []
fin = ""
for w in word_tokens:
    #if w not in stop_words:
     #   filtered_sentence.append(w)
    fin=fin+" "+w

print(word_tokens)

print("Text without stop words")
print(fin)

import re
arr1 = re.split("[.|,|!,0-9]", fin)

print(arr1)     # arr after removing after removing punctuations

print('')
file = open("venna_overall.txt", "w", encoding="utf-8")


for k in arr1:           #traversing through the arr of useful words
    for feat in overall:
        if feat.lower() in k:
            file.writelines(k + "")
            file.writelines(k + "\n")
            break










# print("Bigram text")
# bigrm = list(nltk.bigrams(fin.split()))
#
# print(bigrm)
#
# print("Trigram Text")
# trigrm = list(nltk.trigrams(fin.split()))
#
# print(trigrm)
