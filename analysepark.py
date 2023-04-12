
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
#nltk.download('vader_lexicon')

import nltk
import ssl
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
file1 = open('park_food.txt', 'r',encoding="utf-8")
Lines = file1.readlines()
ffile = open("park_plaza.txt", "w", encoding="utf-8")

count = 0
sum=0
# Strips the newline character
for line in Lines:
    review=line
    scores = sia.polarity_scores(review)
    sum=sum+scores["compound"]

    stars=0

sum=sum/10

if sum<0:
    stars=1
else:

    if sum<=0.2:
     stars=2
    else:
        if sum<=0.4:
         stars=3
        else:
            if sum<=0.6:
                stars=4
            else:
                if sum>0.6:
                     stars=5;




ffile.writelines("park_food :" +((str))(stars)+"\n")

file1 = open('park_clean.txt', 'r', encoding="utf-8")
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

    stars = 0
sum=sum/10

if sum < 0:
    stars = 1
else:

    if sum <= 0.2:
        stars = 2
    else:
        if sum <= 0.4:
            stars = 3
        else:
            if sum <= 0.6:
                 stars = 4
            else:
                if sum > 0.6:
                    stars = 5;

ffile.writelines("park_clean :" + ((str))(stars) + "\n")


print(sum)
file1 = open('park_service.txt', 'r', encoding="utf-8")
Lines = file1.readlines()


count = 0
sum = 0
# Strips the newline character
for line in Lines:
    review = line
    scores = sia.polarity_scores(review)
    sum = sum + scores["compound"]

    stars = 0
sum = sum / 10
if sum < 0:
    stars = 1
else:

    if sum <= 0.2:
        stars = 2
    else:
        if sum <= 0.4:
            stars = 3
        else:
            if sum <= 0.6:
                stars = 4
            else:
                if sum > 0.6:
                    stars = 5;

ffile.writelines("park_service :" + ((str))(stars) + "\n")

file1 = open('park_location.txt', 'r', encoding="utf-8")
Lines = file1.readlines()
print(sum)

count = 0
sum = 0
# Strips the newline character
for line in Lines:
    review = line
    scores = sia.polarity_scores(review)
    sum = sum + scores["compound"]

sum = sum / 10
stars = 0

if sum < 0:
    stars = 1
else:

    if sum <= 0.2:
        stars = 2
    else:
        if sum <= 0.4:
            stars = 3
        else:
            if sum <= 0.6:
                stars = 4
            else:
                if sum > 0.6:
                    stars = 5;
print(sum)
ffile.writelines("park_location :" + ((str))(stars) + "\n")