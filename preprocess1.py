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


#features1 =["food","location","staff","service","Rooms"]


food = ["Breakfast","buffet","taste","lunch","dinner","dinning","delicious","Chef","Food quality"," dosas",
        "chef"  "roasted","chicken","oily ","juicy","south Indian","utappam","Non veg","Veg","cook ","live counters"]

clean = ["cleanliness","cleaning services"," hygienic"," clean"]

location = ["location ","place","greenary","airy","surrounding ","landscapes ","far ","market","property ","aesthetic ","architecture","Parking ","Space","ambiance","ambience","proprietor ","wonderful"
    ,"amenities","structure","Heritage","building","Picturesque","rooms","Big ","Neat","lobby ","small","floor ","carpeted","size","activities","fountain","engaged ","entertained","pool","Gym","Spa","garden","sports","adventure",
              "recreational","play","trek","climbing ", "fitness "]

service = ["hospitality","services","Satisfactory ","lethargic","Bed sheets","Towels","blankets","on time"
             ,"courteous ", "staff","unprofessional","management","cordial","friendly","co-operative","ready to help","people",
            "humble","helpful","hospitable"]

money = ["money","overpriced","rates","higher","budget","expensive","worth","price",
         "Prices","costly","upmarket","upscale","penny"]


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


for k in arr1:
    for feat in food:
        if feat.lower() in k:
            file = open("food.txt", "a", encoding="utf-8")
            file.writelines(feat+" : "+k + "\n")
            file.close()

    for feat in clean:
        if feat.lower() in k:
            file = open("clean.txt", "a", encoding="utf-8")
            file.writelines(feat+" : "+k + "\n")
            file.close()

    for feat in location:
        if feat.lower() in k:
            file = open("location.txt", "a", encoding="utf-8")
            file.writelines(feat+" : "+k + "\n")
            file.close()

    for feat in service:
        if feat.lower() in k:
            file = open("service.txt", "a", encoding="utf-8")
            file.writelines(feat+" : "+k + "\n")
            file.close()

    for feat in money:
        if feat.lower() in k:
            file = open("money.txt", "a", encoding="utf-8")
            file.writelines(feat+" : "+k + "\n")
            file.close()

# print("Bigram text")
# bigrm = list(nltk.bigrams(fin.split()))
#
# print(bigrm)
#
# print("Trigram Text")
# trigrm = list(nltk.trigrams(fin.split()))
#
# print(trigrm)
