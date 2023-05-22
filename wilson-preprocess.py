import csv

import nltk

from nltk import word_tokenize
from nltk.corpus import stopwords

#create dataframe read csv file & save file in csv format

import pandas as pd
import numpy as np

#read csv file

data = pd.read_csv('wilson.csv')

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
           "advertised","moonrise ","lake ","vibes","surrounding","chilled ","Summer","great "]



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
pfile = open("overall.txt", "w", encoding="utf-8")


for k in arr1:
    for feat in overall:
        if feat.lower() in k:
            pfile.writelines(k + "\n")
            break


pfile.close()
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
file1 = open('overall.txt', 'r',encoding="utf-8")
Lines = file1.readlines()
ffile = open("wilson.txt", "w", encoding="utf-8")
reviewfile = open("wilsonreviews.txt","w",encoding="utf-8")
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




ffile.writelines("wilson_overall:" +((str))(stars)+"\n")

print(sum)


file1.close()
reviewfile.close()

file1 = open('wilsonreviews.txt', 'r' ,encoding='UTF-8')

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
with open('static/js/wilsontest.csv', 'w',encoding='UTF-8') as f:
    for key in sorted_dict.keys():
        f.write("%s,%s\n"%(key,sorted_dict[key]))


# print("Bigram text")
# bigrm = list(nltk.bigrams(fin.split()))
#
# print(bigrm)
#
# print("Trigram Text")
# trigrm = list(nltk.trigrams(fin.split()))
#
# print(trigrm)
