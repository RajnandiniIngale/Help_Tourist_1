import csv

import nltk

from nltk import word_tokenize
from nltk.corpus import stopwords

#create dataframe read csv file & save file in csv format

import pandas as pd
import numpy as np

#read csv file

data = pd.read_csv('chingari.csv')

arr = data.to_numpy()   #convert csv data into array




clean = ["cleanliness","cleaning services"," hygienic"," clean","rooms","Big ","Neat","lobby ","small","floor ","carpeted","size"]

food = ["great ","Breakfast","non spicy","plain dal ","set menu","dry sabzi","buffet","mind-blowing","taste","lunch","dinner","dinning","delicious","Chef","Food quality","dosas "," dosa",
      "chicken roganjosh","bharwaan alu","flavorful ","optimum spice", "Indian cuisine", "loved ","baked ","exceptional","Talented ","dal makhani","galouti","steals the show","chicken lababdar ","fine dine","kulcha ","lip smacking","portion ","Dum Ki Biryani","savoury ","worth it","pricey ","appetisers ","recommendations","perfection ","requirements","chef" ,"served ","Good ","excellent","spices", "roasted","chicken","oily ","juicy","south Indian","utappam","Non veg","Veg","cook ","live counters"]


location = ["location ","place","greenary","airy","surrounding ","disappointed","humiliating","landscapes ","far ","market","property ","aesthetic ","architecture","Parking ","Space","ambiance","ambience","proprietor ","wonderful"
    ,"amenities","structure","Heritage","building","Picturesque","activities","fountain","engaged ","entertained","pool","Gym","Spa","garden","sports","adventure","five-star","5 start"
        ,"atmosphere ","perfect", "special", "bless", "experience", "bless","recreational","play","trek","climbing ", "fitness ","visit ","decor ","nice ","fond memories ","recommend"]


money = ["Prices","costly","little","upmarket","upscale","penny","Overrated ","Expensive","money","overpriced","rates","bit","higher","budget","expensive","worth","price"]
service = ["great ","gentle ","gesture ","anytime","courteous ","staff","unprofessional","management","cordial","server","friendly","co-operative","ready to help","people",
        "awesome", "shout out","humble","winner ","accommodating ","trusted ","helpful" ,"Brilliant","prior reservation","cordial ","welcoming","fellow ","hospitable","worth it","hospitality","services","Satisfactory ","service","lethargic","Bed sheets","Towels","blankets","on time","excellent"]




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
file = open("chfood.txt", "w", encoding="utf-8")
file1 = open("chmoney.txt", "w", encoding="utf-8")
file2 = open("chlocation.txt", "w", encoding="utf-8")
file3 = open("chservice.txt", "w", encoding="utf-8")



for k in arr1:           #traversing through the arr of useful words
    for feat in food:
        if feat.lower() in k:
            file.writelines(k + "\n")
            break


    for feat in money:
        if feat.lower() in k:
            file1.writelines(k + "\n")
            break


    for feat in location:
        if feat.lower() in k:
            file2.writelines(k + "\n")
            break


    for feat in service:
        if feat.lower() in k:
            file3.writelines(k + "\n")
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
