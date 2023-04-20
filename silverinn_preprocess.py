import csv

import nltk

from nltk import word_tokenize
from nltk.corpus import stopwords

#create dataframe read csv file & save file in csv format

import pandas as pd
import numpy as np


#read csv file

data = pd.read_csv('silverinn.csv')

arr = data.to_numpy()   #convert csv data into array


clean = ["cleanliness","cleaning services"," hygienic"," clean","rooms","Big ","Neat","lobby ","small","floor ","carpeted","size"]

food = ["Breakfast","buffet","taste","lunch","dinner","dinning","delicious","Chef","Food quality","dosas "," dosa",
        "chef"  ,"roasted","chicken","oily ","juicy","south Indian","utappam","Non veg","Veg","cook ","live counters"]


location = ["location ","place","greenary","airy","surrounding ","landscapes ","far ","market","property ","aesthetic ","architecture","Parking ","Space","ambiance","ambience","proprietor ","wonderful"
    ,"amenities","structure","Heritage","building","Picturesque","activities","fountain","engaged ","entertained","pool","Gym","Spa","garden","sports","adventure",
              "recreational","play","trek","climbing ", "fitness ","money","overpriced","rates","bit","higher","budget","expensive","worth","price",
         "Prices","costly","little","upmarket","upscale","penny"]


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
sfile = open("silverinn_food.txt", "w", encoding="utf-8")
sfile1 = open("silverinn_clean.txt", "w", encoding="utf-8")
sfile2 = open("silverinn_location.txt", "w", encoding="utf-8")
sfile3 = open("silverinn_service.txt", "w", encoding="utf-8")




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




# print("Bigram text")
# bigrm = list(nltk.bigrams(fin.split()))
#
# print(bigrm)
#
# print("Trigram Text")
# trigrm = list(nltk.trigrams(fin.split()))
#
# print(trigrm)


