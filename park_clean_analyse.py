
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

import nltk
import ssl


# Initialize the sentiment analyzer
sia = SentimentIntensityAnalyzer()

# Define a list of reviews to analyze

# Using readlines()
file = open('park_clean.txt', 'r',encoding="utf-8")

Lines = file.readlines()

count = 0
# Strips the newline character
for line in Lines:
    review=line
    scores = sia.polarity_scores(review)
    print(review)
    print("Negative Score:", scores['neg'])
    print("Neutral Score:", scores['neu'])
    print("Positive Score:", scores['pos'])
    print("Compound Score:", scores['compound'])
    print()

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

                    pfile = open("starsparkclean.txt", "a", encoding="utf-8")

