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

file.close()


import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
#nltk.download('vader_lexicon')

import nltk
import ssl
import pandas as pd
import numpy as np
import ast
import csv
#
# try:
#      _create_unverified_https_context = ssl._create_unverified_context
# except AttributeError:
#      pass
# else:
#      ssl._create_default_https_context = _create_unverified_https_context

#nltk.download()

# Initialize the sentiment analyzer
sia = SentimentIntensityAnalyzer()

# Define a list of reviews to analyze

# Using readlines()
file1 = open('venna_overall.txt', 'r',encoding="utf-8")
Lines = file1.readlines()
ffile = open("venna.txt", "w", encoding="utf-8")
reviewfile = open("vennareviews.txt","w",encoding="utf-8")
count = 0
sum=0
# Strips the newline character
for line in Lines:
    review=line
    scores = sia.polarity_scores(review)

    sum = sum + scores["compound"]
    reviewfile.writelines(review.rstrip() + ":" + str(scores['compound']))
    reviewfile.writelines("\n")
    stars=0

sum=sum/10

if sum < 0.3:
    stars = 1
else:

    if sum <= 0.5:
        stars = 2
    else:
        if sum <= 1.5:
            stars = 3
        else:
            if sum <= 2.5:
                stars = 4
            else:
                if sum > 2.5:
                    stars = 5;




ffile.writelines("venna_overall:" +((str))(stars)+"\n")

print(sum)


file1.close()
reviewfile.close()

file1 = open('vennareviews.txt', 'r' ,encoding='UTF-8')

Lines = file1.readlines()
my_dict={}
count = 0
# Strips the newline character
for line in Lines:
    review=line
    arr=review.split(":",1)
    if len(arr) > 1:
        key=arr[0].replace(' ] [','')
        my_dict[key]=(arr[1].rstrip())
    #print(review)

keys = list(my_dict.keys())
values = list(my_dict.values())

sorted_value_index = np.argsort(values)[::-1]    #sort in descending order ==> list of values
sorted_dict = {keys[i]: values[i] for i in sorted_value_index}      # create dictionary from list

print(sorted_dict)
with open('static/js/vennatest.csv', 'w',encoding='UTF-8') as f:
    for key in sorted_dict.keys():
        f.write("%s,%s\n"%(key,sorted_dict[key]))
f.close()
file1.close()

file1 = open('vennareviews.txt', 'r',encoding="utf-8")
Lines = file1.readlines()
my_dict={}
count = 0
sumc=0;
# Strips the newline character
for line in Lines:
    review=line
    arr=review.split(":")
    my_dict[arr[0]]=arr[1]
    try:
        vv=float(arr[1].rstrip())
    except:
         continue
    sumc=sumc+vv


print(sumc)


sumc = sumc / 100



if sumc < 0.1:
    stars = 1
else:

    if sumc <= 0.2:
        stars = 2
    else:
        if sumc <= 0.3:
            stars = 3
        else:
            if sumc <= 0.4:
                stars = 4
            else:
                if sumc > 0.5:
                    stars = 5;


print("stars",stars)
ffile.writelines("venna_compound :" + ((str))(stars) + "\n")
keys = list(my_dict.keys())
values = list(my_dict.values())
sorted_value_index = np.argsort(values)[::-1]
sorted_dict = {keys[i]: values[i] for i in sorted_value_index}

print(sorted_dict)











# print("Bigram text")
# bigrm = list(nltk.bigrams(fin.split()))
#
# print(bigrm)
#
# print("Trigram Text")
# trigrm = list(nltk.trigrams(fin.split()))
#
# print(trigrm)
