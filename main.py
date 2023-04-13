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

    return render_template("tours.html",ratingsk=stars)


@app.route('/review')
def review():
    return render_template("review.html")


@app.route('/tours1')
def tours1():


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

                    starsfoodmaratha = 0

                    if scores["compound"] < 0:
                        starsfoodmaratha = 1
                    else:

                        if scores["compound"] == 0 and scores["neu"] == 1:
                            starsfoodmaratha = 2
                        else:
                            if scores["compound"] > 0 and scores["compound"] <= 0.4:
                                starsfoodmaratha = 3
                            else:
                                if scores["compound"] > 0 and scores["compound"] <= 0.6:
                                    starsfoodmaratha = 4
                                else:
                                    if scores["compound"] > 0.6:
                                        starsfoodmaratha = 5;

                    print("stars  " + ((str))(starsfoodmaratha))
                    stars["starsfoodmaratha"] = (str)(starsfoodmaratha)

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

                    starslocationmaratha = 0

                    if scores["compound"] < 0:
                        starslocationmaratha = 1
                    else:

                        if scores["compound"] == 0 and scores["neu"] == 1:
                            starslocationmaratha = 2
                        else:
                            if scores["compound"] > 0 and scores["compound"] <= 0.4:
                                starslocationmaratha = 3
                            else:
                                if scores["compound"] > 0 and scores["compound"] <= 0.6:
                                    starslocationmaratha = 4
                                else:
                                    if scores["compound"] > 0.6:
                                        starslocationmaratha = 5;

                    print("stars  " + ((str))(starslocationmaratha))
                    stars["starslocationmaratha"] = (str)(starslocationmaratha)

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

                        starsservicemaratha = 0

                        if scores["compound"] < 0:
                            starsservicemaratha = 1
                        else:

                            if scores["compound"] == 0 and scores["neu"] == 1:
                                starsservicemaratha = 2
                            else:
                                if scores["compound"] > 0 and scores["compound"] <= 0.4:
                                    starsservicemaratha = 3
                                else:
                                    if scores["compound"] > 0 and scores["compound"] <= 0.6:
                                        starsservicemaratha = 4
                                    else:
                                        if scores["compound"] > 0.6:
                                            starsservicemaratha = 5;

                        print("stars  " + ((str))(starsservicemaratha))
                        stars["starsservicemaratha"] = (str)(starsservicemaratha)
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

                            starscleanmaratha = 0

                            if scores["compound"] < 0:
                                starscleanmaratha = 1
                            else:

                                if scores["compound"] == 0 and scores["neu"] == 1:
                                    starscleanmaratha = 2
                                else:
                                    if scores["compound"] > 0 and scores["compound"] <= 0.4:
                                        starscleanmaratha = 3
                                    else:
                                        if scores["compound"] > 0 and scores["compound"] <= 0.6:
                                            starscleanmaratha = 4
                                        else:
                                            if scores["compound"] > 0.6:
                                                starscleanmaratha = 5;

                            print("stars  " + ((str))(starscleanmaratha))
                            stars["starscleanmaratha"] = (str)(starscleanmaratha)
                return render_template("tours1.html",ratingsk=stars)


@app.route('/mumbai')
def mumbai():
    return render_template("mumbai.html")


if __name__ == '__main__':
    app.run(host="localhost",port="8000",debug="true")