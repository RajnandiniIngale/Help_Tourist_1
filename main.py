import os
import csv
import os
import nltk

import smtplib
from email.message import EmailMessage


from nltk import word_tokenize
from flask_mysqldb import MySQL
from flask_mail import Mail,Message
from nltk.corpus import stopwords

import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
# nltk.download('vader_lexicon')


import ssl

import mimetypes
from flask import Flask, render_template, request
app = Flask(__name__)
mail = Mail(app)        #initialize var

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'hotel'

mysql = MySQL(app)


mimetypes.add_type("text/css", ".css", True)


# @app.route('/send_email')
# def send_email():
#     msg = EmailMessage()
#
#     my_address = "ingalerajnandini22@gmail.com"  # sender address
#
#     app_generated_password = "ufuxfknvlisptbuk"  # gmail generated password
#
#     msg["Subject"] = "HelpTourist"  # email subject
#
#     msg["From"] = my_address  # sender address
#
#     msg["To"] = "siyaingale2002@gmail.com"  # reciver address
#
#     msg.set_content("A new hotel has been added")  # message body
#
#     with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
#         smtp.login(my_address, app_generated_password)  # login gmail account
#
#         print("sending mail")
#         smtp.send_message(msg)  # send message
#         print("mail has sent")


@app.route('/review_us',methods=['GET', 'POST'])
def review_us():
    x = request.form
    print(x)

    mycursor = mysql.connection.cursor()

    params = {
        'name': request.form.get('name', False),
        'feedback': request.form.get('feedback', False),
    }

    sql = """INSERT INTO  reviewus(name,feedback) VALUES ( %(name)s, %(feedback)s)""";

    mycursor.execute(sql, params)

    mysql.connection.commit()
    msg = EmailMessage()

    my_address = "ingalerajnandini22@gmail.com"  # sender address

    app_generated_password = "ufuxfknvlisptbuk"  # gmail generated password

    msg["Subject"] = "HelpTourist"  # email subject

    msg["From"] = my_address  # sender address

    msg["To"] = "siyaingale2002@gmail.com"  # reciver address

    msg.set_content("Dear Admin, a new review has been added!!")  # message body

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(my_address, app_generated_password)  # login gmail account

        print("sending mail")
        smtp.send_message(msg)  # send message
        print("mail has sent")

    return render_template("feedback.html")


@app.route('/register_hotel',methods=['GET', 'POST'])
def register_hotel():
    x = request.form
    print(x)

    mycursor = mysql.connection.cursor()


    params = {
        'name': request.form.get('name',False),
        'address': request.form.get('address',False),
        'image': request.form.get('uimg',False),
        'price': request.form.get('price',False),
        'phno': request.form.get('phno',False)
    }


    sql = """INSERT INTO  registerhotel(name,address,price,image,phno) VALUES ( %(name)s, %(address)s, %(price)s, %(image)s, %(phno)s)""";

    mycursor.execute(sql,params)

    mysql.connection.commit()

    msg = EmailMessage()

    my_address = "ingalerajnandini22@gmail.com"  # sender address

    app_generated_password = "ufuxfknvlisptbuk"  # gmail generated password

    msg["Subject"] = "HelpTourist"  # email subject

    msg["From"] = my_address  # sender address

    msg["To"] = "siyaingale2002@gmail.com"  # reciver address


    msg.set_content("Dear Admin, a new hotel has been added")  # message body

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(my_address, app_generated_password)  # login gmail account

        print("sending mail")
        smtp.send_message(msg)  # send message
        print("mail has sent")

    return render_template("newhotel.html")





@app.route('/newhotel')
def newhotel():
    return render_template("newhotel.html")

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/feedback')
def feedback():
    return render_template("feedback.html")

@app.route('/contacts')
def contacts():
    return render_template("contacts.html")


@app.route('/gallery')
def gallery():
    return render_template("gallery.html")




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
    file1.close()

    file1 = open("chingari.txt")
    lines = file1.readlines()

    for line in lines:
        review = line.split(":")
        stars[review[0]] = int(review[1])
    file1.close()

    file1 = open("barbeque.txt")
    lines = file1.readlines()

    for line in lines:
        review = line.split(":")
        stars[review[0]] = int(review[1])
    file1.close()

    file1 = open("wilson.txt")
    lines = file1.readlines()

    for line in lines:
        review = line.split(":")
        stars[review[0]] = int(review[1])
    file1.close()

    file1 = open("venna.txt")
    lines = file1.readlines()

    for line in lines:
        review = line.split(":")
        stars[review[0]] = int(review[1])
    file1.close()

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

    if name=='keys':            #write new review added by user
        file1 = open('keys_hotel.csv', 'a+')
        file1.writelines("\n")
        file1.writelines(rev+",0,0,0")

        file1.close()
    os.system('python C:\\Users\\USER\\PycharmProjects\\Help_Tourist_2\\preprocess1-2.py')

    if name=='park':
        file1 = open('park.csv', 'a+')
        file1.writelines("\n")
        file1.writelines(rev+"  ")

        file1.close()
        os.system('python C:\\Users\\USER\\PycharmProjects\\Help_Tourist_2\\park_plaza_preprocess.py')
    if name=='barbeque':
        file1 = open('barbequebay.csv', 'a+')
        file1.writelines("\n")
        file1.writelines(rev+"  ")

        file1.close()
        os.system('C:\\Users\\Admin\\PycharmProjects\\Help_Tourist_2\\barbeque-preprocess.py')

    if name=='chingari':
        file1 = open('chingari.csv', 'a+')
        file1.writelines("\n")
        file1.writelines(rev+"  ")

        file1.close()
        os.system('python C:\\Users\\USER\\PycharmProjects\\Help_Tourist_2\\chingari-preprocess.py')

    if name=='wilson':
        file1 = open('wilson.csv', 'a+')
        file1.writelines("\n")
        file1.writelines(rev+"  ")

        file1.close()
    os.system('python C:\\Users\\USER\\PycharmProjects\\Help_Tourist_2\\wilson-preprocess.py')
    if name=='venna':
        file1 = open('venna.csv', 'a+')
        file1.writelines("\n")
        file1.writelines(rev+"  ")

        file1.close()
        os.system('python C:\\Users\\USER\\PycharmProjects\\Help_Tourist_2\\preprocess-venna.py')

    if name=='sayaji':
        file1 = open('sayaji.csv', 'a+')
        file1.writelines("\n")
        file1.writelines(rev+"  ")

        file1.close()
        os.system('python C:\\Users\\USER\\PycharmProjects\\Help_Tourist_1\\sayaji_preprocess.py')
    if name=='maratha':
        file1 = open('maratha.csv', 'a+')
        file1.writelines("\n")
        file1.writelines(rev+"  ")

        file1.close()

    os.system('python C:\\Users\\USER\\PycharmProjects\\Help_Tourist_1\\maratha_preprocess.py')
    if name=='parakh':
        file1 = open('parakh.csv', 'a+')
        file1.writelines("\n")
        file1.writelines(rev+"  ")

        file1.close()
    os.system('python C:\\Users\\USER\\PycharmProjects\\Help_Tourist_1\\parakh_preprocess.py')
    if name=='tandoor':
        file1 = open('Tandoor.csv', 'a+')
        file1.writelines("\n")
        file1.writelines(rev+"  ")

        file1.close()
        os.system('python C:\\Users\\USER\\PycharmProjects\\Help_Tourist_1\\tandoor_preprocess.py')
    if name=='mahalaxmi':
        file1 = open('mahalaxmi.csv', 'a+')
        file1.writelines("\n")
        file1.writelines(rev+"  ")

        file1.close()
        os.system('python C:\\Users\\USER\\PycharmProjects\\Help_Tourist_1\\mahalakshmi_preprocess.py')
    if name=='newpalace':
        file1 = open('newpalace.csv', 'a+')
        file1.writelines("\n")
        file1.writelines(rev+"  ")

        file1.close()
        os.system('python C:\\Users\\USER\\PycharmProjects\\Help_Tourist_1\\newpalace_preprocess.py')

    if name=='chingari':
        file1 = open('chingari.csv', 'a+')
        file1.writelines("\n")
        file1.writelines(rev+"  ")
        file1.close()

    if name=='jwhotel':
        file1 = open('jwhotel.csv', 'a+')
        file1.writelines("\n")
        file1.writelines(rev+"  ")

        file1.close()
        os.system('python C:\\Users\\USER\\PycharmProjects\\Help_Tourist_1\\jwhotel_preprocess.py')

    if name=='silverinn':
        file1 = open('silverinn.csv', 'a+')
        file1.writelines("\n")
        file1.writelines(rev+"  ")

        file1.close()
        os.system('python C:\\Users\\USER\\PycharmProjects\\Help_Tourist_1\\silverinn_preprocess.py')

    if name=='gateway':
        file1 = open('gatewayindia.csv', 'a+')
        file1.writelines("\n")
        file1.writelines(rev+"  ")
        file1.close()
        os.system('python C:\\Users\\USER\\PycharmProjects\\Help_Tourist_1\\gatewayindia_preprocess.py')
    if name=='cincin':
        file1 = open('cincin.csv.csv', 'a+')
        file1.writelines("\n")
        file1.writelines(rev+"  ")
        file1.close()
        os.system('python C:\\Users\\USER\\PycharmProjects\\Help_Tourist_1\\cincin_preprocess.py')
    if name=='arbab':
        file1 = open('Arbab.csv', 'a+')
        file1.writelines("\n")
        file1.writelines(rev+"  ")
        file1.close()
        os.system('python C:\\Users\\USER\\PycharmProjects\\Help_Tourist_1\\arbab_preprocess.py')
    if name=='bandrafort':
        file1 = open('bandrafort.csv', 'a+')
        file1.writelines("\n")
        file1.writelines(rev+"  ")

        file1.close()
        os.system('python C:\\Users\\USER\\PycharmProjects\\Help_Tourist_1\\bandrafort_preprocess.py')

    return render_template("index.html")

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