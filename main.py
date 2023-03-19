
import mimetypes
from flask import Flask, render_template, request
app = Flask(__name__)

mimetypes.add_type("text/css", ".css", True)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/tours')
def tours():
    return render_template("tours.html")


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