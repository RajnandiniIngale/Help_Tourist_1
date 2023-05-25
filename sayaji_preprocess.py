import csv
import os
import nltk

from nltk import word_tokenize
from nltk.corpus import stopwords

#create dataframe read csv file & save file in csv format

import pandas as pd
import numpy as np


#read csv file

data = pd.read_csv('sayaji.csv')

arr = data.to_numpy()   #convert csv data into array


clean = ["cleanliness","cleaning services"," hygienic"," clean","rooms","Big ","Neat","lobby ","small","floor ","carpeted","size"]

food = ["Breakfast","food","buffet","delicious","not delicious","taste","lunch","dinner","dinning","delicious","Chef","Food quality","dosas "," dosa",
        "chef"  ,"roasted","chicken","oily ","juicy","south Indian","utappam","Non veg","Veg","cook ","live counters"]


location = ["location ","place","greenary","airy","surrounding ","landscapes ","far ","market","property ","aesthetic ","architecture","Parking ","Space","ambiance","ambience","proprietor ","wonderful"
    ,"amenities","structure","Heritage","building","Picturesque","activities","fountain","engaged ","entertained","pool","Gym","Spa","garden","sports","adventure",
              "recreational","play","trek","climbing ", "fitness ","money","overpriced","rates","bit","higher","budget","expensive","worth","price",
         "Prices","costly","little","upmarket","upscale","penny","environment"]


service = ["courteous ","staff","unprofessional","management","cordial","friendly","co-operative","ready to help","people",
         "humble","helpful" ,"hospitable","hospitality","services","Satisfactory ","service","lethargic","Bed sheets","Towels","blankets","on time"]




stop_words = set(stopwords.words('english'))

word_tokens = word_tokenize(str(arr))
# converts the words in word_tokens to lower case and then checks whether
# they are present in stop_words or not

filtered_sentence = [w for w in word_tokens if not w.lower() in stop_words]
# with no lower case conversion

filtered_sentence = []
fin = ""
for w in word_tokens:
    if w not in stop_words:
        filtered_sentence.append(w)
        fin=fin+" "+w

print(word_tokens)

print("Text without stop words")
print(fin)

import re
arr1 = re.split("[.|,|!,0-9]", fin)

print(arr1)

print('')
sfile = open("sayaji_food.txt", "w", encoding="utf-8")
sfile1 = open("sayaji_clean.txt", "w", encoding="utf-8")
sfile2 = open("sayaji_location.txt", "w", encoding="utf-8")
sfile3 = open("sayaji_service.txt", "w", encoding="utf-8")




for k in arr1:
    for feat in food:
        if feat.lower() in k:
            sfile.writelines(k + "\n")
            break


    for feat in clean:
        if feat.lower() in k:
            sfile1.writelines(k + "\n")
            break


    for feat in location:
        if feat.lower() in k:
            sfile2.writelines(k + "\n")
            break


    for feat in service:
        if feat.lower() in k:
            sfile3.writelines(k + "\n")
            break

sfile.close()
sfile1.close()
sfile2.close()
sfile3.close()

import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
#nltk.download('vader_lexicon')

import nltk
import ssl
# try:
#      _create_unverified_https_context = ssl._create_unverified_context
# except AttributeError:
#      pass
# else:
#      ssl._create_default_https_context = _create_unverified_https_context

#nltk.download()
import pandas as pd
import numpy as np
# Initialize the sentiment analyzer
sia = SentimentIntensityAnalyzer()

# Define a list of reviews to analyze

# Using readlines()
file1 = open('sayaji_food.txt', 'r',encoding="utf-8")
Lines = file1.readlines()
ffile = open("sayaji.txt", "w", encoding="utf-8")
reviewfile = open("sayajireviews.txt","w",encoding="utf-8")

count = 0
sum=0
# Strips the newline character
for line in Lines:
    review=line
    scores = sia.polarity_scores(review)
    sum=sum+scores["compound"]

    reviewfile.writelines(review.rstrip() + ":" + str(scores['compound']))
    reviewfile.writelines("\n")
    stars = 0


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




ffile.writelines("sayaji_food :" +((str))(stars)+"\n")

file1 = open('sayaji_clean.txt', 'r', encoding="utf-8")
Lines = file1.readlines()
print(sum)

count = 0
sum = 0
# Strips the newline character
for line in Lines:
    review = line
    scores = sia.polarity_scores(review)
    #print(scores["compound"])

    sum = sum + scores["compound"]
    reviewfile.writelines(review.rstrip() + ":" + str(scores['compound']))
    reviewfile.writelines("\n")
    stars = 0

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

ffile.writelines("sayaji_clean :" + ((str))(stars) + "\n")


print(sum)
file1 = open('sayaji_service.txt', 'r', encoding="utf-8")
Lines = file1.readlines()


count = 0
sum = 0
# Strips the newline character
for line in Lines:
    review = line
    scores = sia.polarity_scores(review)
    sum = sum + scores["compound"]

    reviewfile.writelines(review.rstrip() + ":" + str(scores['compound']))
    reviewfile.writelines("\n")
    stars=0
stars = 0
sum = sum / 10

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

ffile.writelines("sayaji_service :" + ((str))(stars) + "\n")

file1 = open('sayaji_location.txt', 'r', encoding="utf-8")
Lines = file1.readlines()
print(sum)

count = 0
sum = 0
# Strips the newline character
for line in Lines:
    review = line
    scores = sia.polarity_scores(review)
    sum = sum + scores["compound"]

    reviewfile.writelines(review.rstrip() + ":" + str(scores['compound']))
    reviewfile.writelines("\n")
    stars=0
sum = sum / 10
stars = 0

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
print(sum)
ffile.writelines("sayaji_location :" + ((str))(stars) + "\n")



file1.close()
reviewfile.close()

file1 = open('sayajireviews.txt', 'r' ,encoding='UTF-8')

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
with open('static/js/sayaji_test.csv', 'w',encoding='UTF-8') as f:
    for key in sorted_dict.keys():
        f.write("%s,%s\n"%(key,sorted_dict[key]))

file1.close()

file1 = open('sayajireviews.txt', 'r')
#Lines = file1.readlines()
my_dict={}
count = 0
sumc=0;
# Strips the newline character
for line in Lines:
    review=line
    arr=review.split(":")
    my_dict[arr[0]]=arr[1]
    vv=float(arr[1].rstrip())
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
ffile.writelines("sayaji_compound :" + ((str))(stars) + "\n")
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


