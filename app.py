from flask import (Flask, render_template, redirect, url_for, make_response, flash, request)
app = Flask(__name__)
from dictogram_official import Dictogram
import utility
from pymongo import MongoClient 
from mongoengine import *

# connect('mongoengine_test', host='localhost', port=27017)

client = MongoClient('localhost', 27017)
db = client['markov_data']

class sources(Document):
    title = StringField(required=True, max_length=200)
    content = StringField(required=True)

class sentences(Document):
    content = StringField(required=True)

@app.route('/')
def home():
    # words = utility.read('sources/frankenstien.txt')
    words = "one fish two fish red fish blue fish."
    words = utility.cleanse(words)
    histogram = Dictogram(words)
    histogram.count_to_possibility()
    histogram.get_sentence()
    sentence = histogram.print_sentence()
    return render_template('index.html', test = sentence)