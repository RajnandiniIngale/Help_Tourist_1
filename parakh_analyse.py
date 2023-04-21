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
file1 = open('parakh_food.txt', 'r', encoding="utf-8")
Lines = file1.readlines()
x = len(Lines)
print("no of reviews : ", x)
ffile = open("parakh.txt", "w", encoding="utf-8")
reviewfile = open("parakh_reviews.txt", "w", encoding="utf-8")

count = 0
sum = 0
# Strips the newline character
for line in Lines:
    review = line
    scores = sia.polarity_scores(review)
   # sum = sum + scores["compound"]
    #reviewfile.writelines(review)
    #reviewfile.writelines(" Negative Score : " + str(scores['neg']))
    #reviewfile.writelines(" Neutral Score : " + str(scores['neu']))
    #reviewfile.writelines(" Positive Score :" + str(scores['pos']))
    #reviewfile.writelines(" Compound Score : " + str(scores['compound']))
    #reviewfile.writelines("\n\n")
    sum = sum + scores["compound"]
    reviewfile.writelines(review.rstrip() + ":" + str(scores['compound']))
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

ffile.writelines("parakh_food :" + ((str))(stars) + "\n")


file1 = open('parakh_clean.txt', 'r', encoding="utf-8")
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

ffile.writelines("parakh_clean :" + ((str))(stars) + "\n")

print(sum)

file1 = open('parakh_service.txt', 'r', encoding="utf-8")
Lines = file1.readlines()

count = 0
sum = 0
# Strips the newline character
for line in Lines:
    review = line
    scores = sia.polarity_scores(review)
    sum = sum + scores["compound"]
    reviewfile.writelines(review.rstrip() + ":" + str(scores['compound']))
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

ffile.writelines("parakh_service :" + ((str))(stars) + "\n")

file1 = open('parakh_location.txt', 'r', encoding="utf-8")
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
    stars = 0

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
ffile.writelines("parakh_location :" + ((str))(stars) + "\n")