import csv

import nltk

from nltk import word_tokenize
from nltk.corpus import stopwords

#create dataframe read csv file & save file in csv format

import pandas as pd
import numpy as np

#read csv file

data = pd.read_csv('newpalace.csv')

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
pfile = open("newpalace_all.txt", "w", encoding="utf-8")





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
file1 = open('newpalace_all.txt', 'r',encoding="utf-8")
Lines = file1.readlines()
ffile = open("newpalace.txt", "w", encoding="utf-8")
reviewfile = open("newpalacereviews.txt","w",encoding="utf-8")
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




ffile.writelines("newpalace_all :" +((str))(stars)+"\n")

print(sum)



file1.close()
reviewfile.close()

file1 = open('newpalacereviews.txt', 'r' ,encoding='UTF-8')

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
with open('static/js/newpalacetest.csv', 'w',encoding='UTF-8') as f:
    for key in sorted_dict.keys():
        f.write("%s,%s\n"%(key,sorted_dict[key]))
file1.close()



file1 = open('newpalacereviews.txt', 'r')
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
        vv = float(arr[1].rstrip())
    except:
        print("error")
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
ffile.writelines("newpalace_compound :" + ((str))(stars) + "\n")

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
