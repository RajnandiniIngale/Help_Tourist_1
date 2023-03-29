
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
file1 = open('food.txt', 'r')
Lines = file1.readlines()
foodfile = open("starsparkclean.txt", "w", encoding="utf-8")

count = 0
# Strips the newline character
for line in Lines:
    review=line
    scores = sia.polarity_scores(review)
    foodfile.writelines(review + "\n")
    print(review)
    foodfile.writelines("Negative Score:", scores['neg'])
    foodfile.writelines("Neutral Score:", scores['neu'])
    foodfile.writelines("Positive Score:", scores['pos'])
    foodfile.writelines("Compound Score:",+ scores['compound'])

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




        foodfile.writelines("stars  " +((str))(stars))