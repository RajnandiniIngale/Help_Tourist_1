

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
file1 = open('maratha_food.txt', 'r',encoding="utf-8")
Lines = file1.readlines()
ffile = open("starmarathafood.txt", "w", encoding="utf-8")

count = 0
# Strips the newline character
for line in Lines:
    review=line
    scores = sia.polarity_scores(review)
    ffile.writelines(review + "\n")

    ffile.writelines("Negative Score:" + str(scores['neg']))
    ffile.writelines("Neutral Score:" + str(scores['neu']))
    ffile.writelines("Positive Score:" + str(scores['pos']))
    ffile.writelines("Compound Score:" + str(scores['compound']))

    stars=0


    if scores["compound"]<0:
        stars=1
    else:

        if scores["compound"]==0 and scores["neu"]==1:
            stars=2
        else:
            if scores["compound"]>0 and scores["compound"]<=0.4:
                stars=3
            else:
                if scores["compound"]>0 and scores["compound"]<=0.6:
                    stars=4
                else:
                    if scores["compound"]>0.6:
                       stars=5;




        ffile.writelines("stars  " +((str))(stars))