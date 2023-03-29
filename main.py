import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
# nltk.download('vader_lexicon')


import ssl

import mimetypes
from flask import Flask, render_template, request
app = Flask(__name__)

mimetypes.add_type("text/css", ".css", True)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/tours')
def tours():
    stars={}
#
    # try:
    #      _create_unverified_https_context = ssl._create_unverified_context
    # except AttributeError:
    #      pass
    # else:
    #      ssl._create_default_https_context = _create_unverified_https_context

    # nltk.download()

    # Initialize the sentiment analyzer
    sia = SentimentIntensityAnalyzer()

    # Define a list of reviews to analyze

    # Using readlines()
    file1 = open('food.txt', 'r')
    Lines = file1.readlines()

    count = 0
    # Strips the newline character
    for line in Lines:
        review = line
        scores = sia.polarity_scores(review)
        print(review)
        print("Negative Score:", scores['neg'])
        print("Neutral Score:", scores['neu'])
        print("Positive Score:", scores['pos'])
        print("Compound Score:", scores['compound'])
        print()

        starsfoodkeys = 0

        if scores["compound"] < 0:
            starsfoodkeys = 1
        else:

            if scores["compound"] == 0 and scores["neu"] == 1:
                starsfoodkeys = 2
            else:
                if scores["compound"] > 0 and scores["compound"] <= 0.4:
                    starsfoodkeys = 3
                else:
                    if scores["compound"] > 0 and scores["compound"] <= 0.6:
                        starsfoodkeys = 4
                    else:
                        if scores["compound"] > 0.6:
                            starsfoodkeys = 5;

        print("stars  " + ((str))(starsfoodkeys))
        stars["starsfoodkeys"]=(str)(starsfoodkeys)

    file1.close()

    file1 = open('location.txt', 'r', encoding="utf8")
    Lines = file1.readlines()

    count = 0
    # Strips the newline character
    for line in Lines:
        review = line
        scores = sia.polarity_scores(review)
        print(review)
        print("Negative Score:", scores['neg'])
        print("Neutral Score:", scores['neu'])
        print("Positive Score:", scores['pos'])
        print("Compound Score:", scores['compound'])
        print()

        starslocationkeys = 0

        if scores["compound"] < 0:
            starslocationkeys = 1
        else:

            if scores["compound"] == 0 and scores["neu"] == 1:
                starslocationkeys = 2
            else:
                if scores["compound"] > 0 and scores["compound"] <= 0.4:
                    starslocationkeys = 3
                else:
                    if scores["compound"] > 0 and scores["compound"] <= 0.6:
                        starslocationkeys = 4
                    else:
                        if scores["compound"] > 0.6:
                            starslocationkeys = 5;

        print("stars  " + ((str))(starslocationkeys))
        stars["starslocationkeys"] = (str)(starslocationkeys)

        file1.close()

        file1 = open('clean.txt', 'r', encoding="utf8")
        Lines = file1.readlines()

        count = 0
        # Strips the newline character
        for line in Lines:
            review = line
            scores = sia.polarity_scores(review)
            print(review)
            print("Negative Score:", scores['neg'])
            print("Neutral Score:", scores['neu'])
            print("Positive Score:", scores['pos'])
            print("Compound Score:", scores['compound'])
            print()

            starscleankeys = 0

            if scores["compound"] < 0:
                starscleankeys = 1
            else:

                if scores["compound"] == 0 and scores["neu"] == 1:
                    starscleankeys = 2
                else:
                    if scores["compound"] > 0 and scores["compound"] <= 0.4:
                        starscleankeys = 3
                    else:
                        if scores["compound"] > 0 and scores["compound"] <= 0.6:
                            starscleankeys = 4
                        else:
                            if scores["compound"] > 0.6:
                                starscleankeys = 5;

            print("stars  " + ((str))(starscleankeys))
            stars["starscleankeys"] = (str)(starscleankeys)

            file1.close()

            file1 = open('service.txt', 'r', encoding="utf8")
            Lines = file1.readlines()

            count = 0
            # Strips the newline character
            for line in Lines:
                review = line
                scores = sia.polarity_scores(review)
                print(review)
                print("Negative Score:", scores['neg'])
                print("Neutral Score:", scores['neu'])
                print("Positive Score:", scores['pos'])
                print("Compound Score:", scores['compound'])
                print()

                starsservicekeys = 0

                if scores["compound"] < 0:
                    starsservicekeys = 1
                else:

                    if scores["compound"] == 0 and scores["neu"] == 1:
                        starsservicekeys = 2
                    else:
                        if scores["compound"] > 0 and scores["compound"] <= 0.4:
                            starsservicekeys = 3
                        else:
                            if scores["compound"] > 0 and scores["compound"] <= 0.6:
                                starsservicekeys = 4
                            else:
                                if scores["compound"] > 0.6:
                                    starsservicekeys = 5;

                print("stars  " + ((str))(starsservicekeys))
                stars["starsservicekeys"] = (str)(starsservicekeys)

                file1.close()

                file1 = open('park_food.txt', 'r', encoding="utf8")
                Lines = file1.readlines()

                count = 0
                # Strips the newline character
                for line in Lines:
                    review = line
                    scores = sia.polarity_scores(review)
                    print(review)
                    print("Negative Score:", scores['neg'])
                    print("Neutral Score:", scores['neu'])
                    print("Positive Score:", scores['pos'])
                    print("Compound Score:", scores['compound'])
                    print()

                    foodpark = 0

                    if scores["compound"] < 0:
                        foodpark = 1
                    else:

                        if scores["compound"] == 0 and scores["neu"] == 1:
                            foodpark = 2
                        else:
                            if scores["compound"] > 0 and scores["compound"] <= 0.4:
                                foodpark = 3
                            else:
                                if scores["compound"] > 0 and scores["compound"] <= 0.6:
                                    foodpark = 4
                                else:
                                    if scores["compound"] > 0.6:
                                        foodpark = 5;

                    print("stars  " + ((str))(foodpark))
                    stars["foodpark"] = (str)(foodpark)

                    file1.close()

    return render_template("tours.html",ratingsk=stars)


@app.route('/review')
def review():
    return render_template("review.html")


@app.route('/tours1')
def tours1():
    return render_template("tours1.html")


@app.route('/mumbai')
def mumbai():
    return render_template("mumbai.html")


if __name__ == '__main__':
    app.run(host="localhost",port="8000",debug="true")