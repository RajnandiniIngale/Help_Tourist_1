import csv

import nltk

from nltk import word_tokenize
from nltk.corpus import stopwords

#create dataframe read csv file & save file in csv format

import pandas as pd
import numpy as np

#read csv file

data = pd.read_csv('mahalaxmi.csv')

arr = data.to_numpy()   #convert csv data into array


clean = ["cleanliness","tidy","cleaning services","unhygienic","smelling","hygienic","clean","rooms","Big ","Neat","lobby ","small","floor ","carpeted","size"]

food = ["vegetarian ","vegan ","Breakfast","buffet","taste","lunch","dinner","dinning","delicious","Chef","Food quality","dosas "," dosa",
        "decent ","chef" , "Fresh ","roasted","chicken","oily ","wholesome ","meals","juicy","south Indian","utappam","Non veg","Veg","cook ","live counters","beverages "]


location = ["location ","Average ","nice","far ","Full marks","feel like home","hatsoff ","wifi ","locality","stars ","market","place","old","greenary","airy","surrounding ","garden ","pretty","landscapes ","far ","market","property ","aesthetic ","architecture","Parking ","Space","ambiance","ambience","proprietor ","wonderful"
    ,"amenities","structure","Heritage","building","Picturesque","activities","fountain","engaged ","entertained","pool","Gym","Spa","garden","sports","adventure",
         "maintenance ", "Establishment ",  "Thank you","games ","recreational","play","trek","climbing ", "high ","price","fitness ","money","overpriced","rates","bit","higher","view","budget","expensive","worth","price",
        "wastage of money","ok ok ", "away ","Prices","costly","little","upmarket","upscale","penny","dirty","higher","old "," pool table", "table tennis ", "power backup"," maintenance of indoor games", "no wifi", "mobile networks","deluxe",
         "balcony","relaxation ", "spacious ","huge","surroundings ","entrance","indoor ","fluctuates","improvement","attraction","view","away","market","landscapes ","calmness","scenery","conveniently ","ventilation ","network ","reception",]


service = ["courteous ","Quick ","staff","unprofessional","rude","help","barely sufficient","improved","management","too long","cordial","friendly","manager","arrogant ","co-operative","ready to help","people","fabulous ","Supporting ",
         "polite ","geyser","humble","responsible","helpful" ,"hospitable","hospitality","superb","professional ","hotwater","laundry","services","electricity","Satisfactory ","service","lethargic","Bed sheets","Towels","blankets","on time"]




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
pfile = open("mahalaxmi_all.txt", "w", encoding="utf-8")





for k in arr1:
    for feat in food:
        if feat.lower() in k:
            pfile.writelines(k + "\n")
            break


    for feat in clean:
        if feat.lower() in k:
            pfile.writelines(k + "\n")
            break


    for feat in location:
        if feat.lower() in k:
            pfile.writelines(k + "\n")
            break


    for feat in service:
        if feat.lower() in k:
            pfile.writelines(k + "\n")
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
