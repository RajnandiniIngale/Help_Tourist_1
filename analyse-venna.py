import numpy as np
import ast
import csv

import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
# nltk.download('vader_lexicon')

import nltk
import ssl

#
# try:
#      _create_unverified_https_context = ssl._create_unverified_context
# except AttributeError:
#      pass
# else:
#      ssl._create_default_https_context = _create_unverified_https_context

# nltk.download()

# Initialize the sentiment analyzer
sia = SentimentIntensityAnalyzer()  # create
# object

# Define a list of reviews to analyze

# Using readlines()
file1 = open('overall_venna.txt', 'r', encoding="utf-8")
Lines = file1.readlines()
x = len(Lines)
print("no of reviews : ", x)
ffile = open("venna.txt", "w", encoding="utf-8")
reviewfile = open("vennareviews.txt", "w", encoding="utf-8")

count = 0
sum = 0
# Strips the newline character
for line in Lines:
    review = line
    scores = sia.polarity_scores(review)
    sum = sum + scores["compound"]
    reviewfile.writelines(review.rstrip() + ":" + str(scores['compound'])
                          )
    # reviewfile.writelines(" Negative Score : " + str(scores['neg']))
    # reviewfile.writelines(" Neutral Score : " + str(scores['neu']))
    # reviewfile.writelines(" Positive Score :" + str(scores['pos']))
    # reviewfile.writelines(" Compound Score : " + str(scores['compound']))
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

ffile.writelines("venna_overall:" + ((str))(stars) + "\n")

