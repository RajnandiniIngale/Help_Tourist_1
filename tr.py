import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
#nltk.download('vader_lexicon')

import pandas as pd     #create dataframe read csv file & save file in csv format

#read csv file

#data = pd.read_csv('keys_hotel.csv')

#print(data)

#import ssl

#try:
 #    _create_unverified_https_context = ssl._create_unverified_context
#except AttributeError:
 #    pass
#else:
 #    ssl._create_default_https_context = _create_unverified_https_context

#nltk.download()

# Initialize the sentiment analyzer
sia = SentimentIntensityAnalyzer()

# Define a list of reviews to analyze
reviews = [
    "the reception staff was so rude i called to book a room and he dont knw how to greet the customers on calland talk with courtesy. i called him around 1:30 pls checkout who is the person and take some step otherwise its a big concern about the property . hoteln is a 4 star property and how ur keeping ur staff so dis mannered",
   "I had a terrible experience at this hotel. The room was dirty and the staff was rude.",
    "I really enjoyed my stay at this resort. The facilities were top-notch and the staff was friendly and helpful.",
    "The movie was just okay. It had some good moments but overall it was pretty boring.",
    "I love this product! It's exactly what I was looking for and it works perfectly.",
    "The food was delicious",
    "The food was not delicious"
    ]



# Analyze the sentiment of each review
for review in reviews:
 scores = sia.polarity_scores(review)
 print(review)
 print("Negative Score:", scores['neg'])
 print("Neutral Score:", scores['neu'])
 print("Positive Score:", scores['pos'])
 print("Compound Score:", scores['compound'])
 print()
