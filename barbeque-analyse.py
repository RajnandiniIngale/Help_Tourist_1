import numpy as np
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
# nltk.download('vader_lexicon')

import nltk
import ssl

# Initialize the sentiment analyzer
sia = SentimentIntensityAnalyzer()  # create
# object

# Define a list of reviews to analyze

# Using readlines()
file1 = open('bbqfood.txt', 'r', encoding="utf-8")
Lines = file1.readlines()
x = len(Lines)
print("no of reviews : ", x)
ffile = open("barbeque.txt", "w", encoding="utf-8")
reviewfile = open("barbeque-reviews.txt", "w", encoding="utf-8")

count = 0
sum = 0
# Strips the newline character
for line in Lines:
    review = line
    scores = sia.polarity_scores(review)
    sum = sum + scores["compound"]
    reviewfile.writelines(review.rstrip() + ":" + str(scores['compound']))
    reviewfile.writelines("\n")

    stars = 0

sum = sum / 10
print(x)
# sum=(100*sum)/x
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

ffile.writelines("barbeque_food:" + ((str))(stars) + "\n")


file1 = open('bbqmoney.txt', 'r', encoding="utf-8")
Lines = file1.readlines()
x = len(Lines)
print(sum)

count = 0
sum = 0
# Strips the newline character
for line in Lines:
    review = line
    scores = sia.polarity_scores(review)
    # print(scores["compound"])
    sum = sum + scores["compound"]
    reviewfile.writelines(review.rstrip() + ":" + str(scores['compound']))
    reviewfile.writelines("\n")
    stars = 0
# sum=(100*sum)/x
sum = sum / 10
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
    stars = 0

x = len(Lines)
# sum=(100*sum)/x
sum = sum / 10
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

# print(sum)
x = len(Lines)
# sum=(100*sum)/x
sum = sum / 10
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
ffile.writelines("barbeque_location:" + ((str))(stars) + "\n")


file1.close()

file1 = open('barbeque-reviews.txt', 'r' ,encoding='UTF-8')

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

