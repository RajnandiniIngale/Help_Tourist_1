import csv

import nltk

from nltk import word_tokenize
from nltk.corpus import stopwords

#create dataframe read csv file & save file in csv format

import pandas as pd
import numpy as np

#read csv file

data = pd.read_csv('keys_hotel.csv')

arr = data.to_numpy()   #convert csv data into array


overall = ["sunrise","excited","awesome","far ","disappointed","satisfied","Space ","crowd"," morning","Road ", "nature ","view","evening ",
           "rainy ","highest"," excellent","Horse riding","enjoy","difficult ","better ","beautiful","scenery","huge ","crowded ","pretty dark ",
           "worthy","vast","scenic ","convenience ","stunning","sunset","surreal "," peace","calm","Recommended ","beautyscape ","destination","horses",
            "good ","bad","patches","narrow","blind spots","bike ","big","fun ","location","Sun-gazing ","mesmerising ","cool breeze","places","monsoon",
           "cloudy"," windy","winds","winter","shivering ","beauty","climate ","couples","Perfect ","photography","mother","Famous ","Offbeat ","worth",
           "Average","Decent ","greenery","complicated ","Traveling ","overrated ","Nothing","walking ","main market","capture ","sky","sublime",
           "offer","trek ","terrain "," hill view","Amazing ","quiet ","Super ","loved ","peaceful","Life time","steep slope","wonderful ","foggy",
           "shops ","serene","appetite ","tourist attraction","weekends ","parking","washroom ","like","star gazing","cold ","experience ","Best ",
           "clean","open place","Temperature ","safely ","patience","Ample ","kids","market area","waste ","time","fuel","happy ","terrible","chilly ",
           "advertised","moonrise ","lake ","vibes","surrounding","chilled ","Summer","great ",]

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
file = open("overall.txt", "w", encoding="utf-8")


for k in arr1:           #traversing through the arr of useful words
    for feat in overall:
        if feat.lower() in k:
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
