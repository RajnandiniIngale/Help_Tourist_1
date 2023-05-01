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
    stars={}#dictionary

    file1=open("keys.txt")
    lines=file1.readlines()

    for line in lines:
        review=line.split(":")
        stars[review[0]]=int(review[1])
    file1.close()
    file1 = open("park_plaza.txt")
    lines = file1.readlines()

    for line in lines:
        review = line.split(":")
        stars[review[0]] = int(review[1])


    return render_template("tours.html",ratingsk=stars)


@app.route('/review')
def review():
    return render_template("review.html")


@app.route('/tours1')
def tours1():
    stars = {}

    file1 = open("sayaji.txt")
    lines = file1.readlines()

    for line in lines:
        review = line.split(":")
        stars[review[0].rstrip()] = int(review[1])
    file1.close()
    file1 = open("maratha.txt")
    lines = file1.readlines()

    for line in lines:
        review = line.split(":")
        stars[review[0].rstrip()] = int(review[1])
    file1.close()
    file1 = open("tandoor.txt")
    lines = file1.readlines()

    for line in lines:
        review = line.split(":")
        stars[review[0].rstrip()] = int(review[1])
        file1.close()
        file1 = open("parakh.txt")
        lines = file1.readlines()

        for line in lines:
            review = line.split(":")
            stars[review[0].rstrip()] = int(review[1])
        file1.close()
        file1 = open("mahalaxmi.txt")
        lines = file1.readlines()

        for line in lines:
            review = line.split(":")
            stars[review[0].rstrip()] = int(review[1])
        file1.close()
        file1 = open("newpalace.txt")
        lines = file1.readlines()

        for line in lines:
            review = line.split(":")
            stars[review[0].rstrip()] = int(review[1])
    print(stars)
    return render_template("tours1.html", ratingsk=stars)


@app.route('/insert_csv',methods=['GET', 'POST'])
def insert_keys_csv():
    x=request.form
    print(x)
    name=request.form['nm']
    rev=request.form['reviews2']

    if name=='keys':
        file1 = open('keys_hotel.csv', 'a+')
        file1.writelines("\n")
        file1.writelines(rev+",0,0,0")

        file1.close()
    return render_template("review.html")


@app.route('/mumbai')
def mumbai():
    stars = {}

    file1 = open("silverinn.txt")
    lines = file1.readlines()

    for line in lines:
        review = line.split(":")
        stars[review[0].rstrip()] = int(review[1])
    file1.close()
    file1 = open("jwhotel.txt")
    lines = file1.readlines()

    for line in lines:
        review = line.split(":")
        stars[review[0].rstrip()] = int(review[1])

    file1.close()
    file1 = open("arbab.txt")
    lines = file1.readlines()

    for line in lines:
            review = line.split(":")
            stars[review[0].rstrip()] = int(review[1])
    file1.close()
    file1 = open("cincin.txt")
    lines = file1.readlines()

    for line in lines:
        review = line.split(":")
        stars[review[0].rstrip()] = int(review[1])
    file1.close()
    file1 = open("gatewayindia.txt")
    lines = file1.readlines()

    for line in lines:
        review = line.split(":")
        stars[review[0].rstrip()] = int(review[1])
    file1.close()
    file1 = open("bandrafort.txt")
    lines = file1.readlines()

    for line in lines:
        review = line.split(":")
        stars[review[0].rstrip()] = int(review[1])
    print(stars)
    return render_template("mumbai.html",ratingsk=stars)


if __name__ == '__main__':
    app.run(host="localhost",port="8000",debug="true")