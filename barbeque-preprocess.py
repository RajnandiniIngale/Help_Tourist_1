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



file.close()
file1.close()
file2.close()
file3.close()

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
file1 = open('bbqfood.txt', 'r',encoding="utf-8")
Lines = file1.readlines()
ffile = open("barbeque.txt", "w", encoding="utf-8")
reviewfile = open("barbeque-reviews.txt","w",encoding="utf-8")

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




ffile.writelines("barbeque_food:" +((str))(stars)+"\n")

file1 = open('bbqmoney.txt', 'r', encoding="utf-8")
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

ffile.writelines("barbeque_money:" + ((str))(stars) + "\n")


print(sum)
file1 = open('bbqservice.txt', 'r', encoding="utf-8")
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

ffile.writelines("barbeque_service:" + ((str))(stars) + "\n")

file1 = open('bbqlocation.txt', 'r', encoding="utf-8")
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
ffile.writelines("barbeque_location:" + ((str))(stars) + "\n")



file1.close()
reviewfile.close()


import numpy as np
import ast
import csv
#Open a CSV file for writing
with open('data.csv', 'w', newline='') as csvfile:
#   # Define the header row of the CSV file
   fieldnames = ['Reviews', 'ratings']

#   # Create a CSV writer object
   writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

#   # Write the header row
   writer.writeheader()

file1 = open('barbeque-reviews.txt', 'r',encoding='UTF-8')

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
with open('static/js/bbqtest.csv', 'w',encoding='UTF-8') as f:
    for key in sorted_dict.keys():
        f.write("%s,%s\n"%(key,sorted_dict[key]))


f.close()
file1.close()

file1 = open('barbeque-reviews.txt', 'r',encoding="utf-8")
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
ffile.writelines("barbeque_compound:" + ((str))(stars) + "\n")

keys = list(my_dict.keys())
values = list(my_dict.values())
sorted_value_index = np.argsort(values)[::-1]
sorted_dict = {keys[i]: values[i] for i in sorted_value_index}

print(sorted_dict)






