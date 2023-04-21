import csv

import nltk

from nltk import word_tokenize
from nltk.corpus import stopwords

#create dataframe read csv file & save file in csv format

import pandas as pd
import numpy as np

#read csv file

data = pd.read_csv('barbequebay.csv')

arr = data.to_numpy()   #convert csv data into array




food = ["Delicious ","dine","kid friendly","Wonderful ","Excellent ","grills ","Barbecue ","tasty","choices","Starters ","Main course","sweets ","Breakfast","cravings","buffet","taste","lunch","dinner","dinning","delicious","Chef","Food quality","dosas "," dosa",
       "not enough","mockta","local delicacies","mojito ","quantity","quality", "biryani","kebab","Desserts ","Best","Barbeque","recommended ","chef","spread","grills","live counter","bland","roasted","spread of food","enjoyed","level up","chicken","oily ","juicy","south Indian","utappam","Non veg","Veg","cook ","live counters"]


location = ["definitely try","Decent ","Best ","disheartened "," top notch","loved ","spread of food ","location ","place","greenary","airy","surrounding ","landscapes ","far ","market","property ","aesthetic ","architecture","Parking ","Space","ambiance","ambience","proprietor ","wonderful"
    ,"celebration","amenities","structure","Heritage","building","Picturesque","activities","fountain","engaged ","entertained","pool","Gym","Spa","garden","sports","adventure",
 " open air","weather","Very Good" ,"atmosphere","time","great","failed ", "Horrible ", "great time","recreational","play","trek","climbing ", "fitness "
      ,"disappointed","must  visit", "avoid ","reputed brand","Limited ","premises","pleasant","memorable"]

money = ["bill ","at par","worth ","expensive","price","penny","costlier","costly" ,"double the price ","upmarket","penny","upscale","Overpriced","half the quantity","overpriced ","Prices","costly","little","fair","money","overpriced","rates","bit","higher","budget"]
service = ["Excellent ","personalized ","Kudos ","extreme pressure","courteous ","warm ","concern ","help","staff","special","unprofessional","management","cordial","friendly","co-operative","ready to help","people",
         "slow","match ","humble","helpful" ,"best ","music","hospitable","hospitality","services","Satisfactory ","service","lethargic","Bed sheets","Towels","blankets","on time"]




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
arr1 = re.split("[.|,|!|0-9]", fin)

print(arr1)     # arr after removing after removing punctuations

print('')
file = open("bbqfood.txt", "w", encoding="utf-8")
file1 = open("bbqmoney.txt", "w", encoding="utf-8")
file2 = open("bbqlocation.txt", "w", encoding="utf-8")
file3 = open("bbqservice.txt", "w", encoding="utf-8")


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



