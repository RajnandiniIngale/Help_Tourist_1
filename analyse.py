import numpy as np
import ast
import csv

import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
#nltk.download('vader_lexicon')

import nltk
import ssl
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
sia = SentimentIntensityAnalyzer()      #create
# object

# Define a list of reviews to analyze

# Using readlines()
file1 = open('food.txt', 'r',encoding="utf-8")
Lines = file1.readlines()
x = len(Lines)
print("no of reviews : ",x)
ffile = open("keys.txt", "w", encoding="utf-8")
reviewfile = open("keysreviews.txt","w",encoding="utf-8")

count = 0
sum=0
# Strips the newline character
for line in Lines:
    review=line
    scores = sia.polarity_scores(review)
    sum=sum+scores["compound"]
    reviewfile.writelines(review.rstrip()+":"+str(scores['compound']))
    reviewfile.writelines("\n")

    stars=0

sum=sum/10
print(x)
#sum=(100*sum)/x
print(sum)

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



ffile.writelines("stars_food:" +((str))(stars)+"\n")

file1 = open('clean.txt', 'r', encoding="utf-8")
Lines = file1.readlines()
x = len(Lines)
print(sum)

count = 0
sum = 0
# Strips the newline character
for line in Lines:
    review = line
    scores = sia.polarity_scores(review)
    #print(scores["compound"])
    sum = sum + scores["compound"]
    reviewfile.writelines(review.rstrip()+":"+str(scores['compound']))
    reviewfile.writelines("\n")
    stars = 0
#sum=(100*sum)/x
sum=sum/10
print(sum)

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

ffile.writelines("stars_clean:" + ((str))(stars) + "\n")


print(sum)

file1 = open('service.txt', 'r', encoding="utf-8")
Lines = file1.readlines()


count = 0
sum = 0
# Strips the newline character
for line in Lines:
    review = line
    scores = sia.polarity_scores(review)
    sum = sum + scores["compound"]
    reviewfile.writelines(review.rstrip()+":"+str(scores['compound']))
    reviewfile.writelines("\n")
    stars = 0
    
x = len(Lines)
#sum=(100*sum)/x
sum=sum/10
print(sum)
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

ffile.writelines("stars_service:" + ((str))(stars) + "\n")

file1 = open('location.txt', 'r', encoding="utf-8")
Lines = file1.readlines()
print(sum)

count = 0
sum = 0
# Strips the newline character
for line in Lines:
    review = line
    scores = sia.polarity_scores(review)
    sum = sum + scores["compound"]
    reviewfile.writelines(review.rstrip()+":"+str(scores['compound']))
    reviewfile.writelines("\n")

#print(sum)
x = len(Lines)
#sum=(100*sum)/x
sum=sum/10
print(sum)

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
ffile.writelines("stars_location:" + ((str))(stars) + "\n")


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

#ffile = open("abc.csv", "w")
file1 = open('keysreviews.txt', 'r')

Lines = file1.readlines()
my_dict={}
count = 0
# Strips the newline character
for line in Lines:
    review=line
    print(review)
    arr=review.split(":")
    key=arr[0].replace(' ] [','')
    my_dict[key]=(arr[1].rstrip())


keys = list(my_dict.keys())
values = list(my_dict.values())


sorted_value_index = np.argsort(values)[::-1]
sorted_dict = {keys[i]: values[i] for i in sorted_value_index}

print(sorted_dict)
with open('test.csv', 'w') as f:
    for key in sorted_dict.keys():
        f.write("%s,%s\n"%(key,sorted_dict[key]))





file1.close()

file1 = open('keysreviews.txt', 'r' ,encoding='UTF-8')

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
with open('static/js/test.csv', 'w',encoding='UTF-8') as f:
    for key in sorted_dict.keys():
        f.write("%s,%s\n"%(key,sorted_dict[key]))

