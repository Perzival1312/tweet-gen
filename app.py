from flask import (Flask, render_template, redirect, url_for, make_response, flash, request)
app = Flask(__name__)
from dictogram_official import Dictogram
import utility
import mongoengine
# import os, dotenv
# URI = app.config.from_envvar()
# app.config.from_object('config_module.ProductionConfig')
from pymongo import MongoClient 
from mongoengine import (Document, connect, StringField)
from flask_mongoengine import QuerySet
# try:
# connect('markov_data', host='localhost:27017')
# except:
connect('markov_data', host='mongodb://heroku_v2s9b483:ou678psipceiq0dr9vlnilreos@ds351455.mlab.com:51455/heroku_v2s9b483')
    # app.config['MONGODB_SETTINGS'] = {'db': 'markov_data', 'host': 'mongodb://heroku_v2s9b483:ou678psipceiq0dr9vlnilreos@ds351455.mlab.com:51455/heroku_v2s9b483'}
    # db = connect('markov_data')

# client = MongoClient(os.getenv("URI"),
#                     #  'markov_data',
#                      connectTimeoutMS=300000,
#                      socketTimeoutMS=None,
#                     socketKeepAlive=True)
# db = client['markov_data']

class sources(Document):
    title = StringField(required=True, max_length=200)
    content = StringField(required=True)

class sentences(Document):
    content = StringField(required=True)

@app.route('/')
def home():
    for source in sources.objects:
        source = source.to_mongo().to_dict()
        if source['title'] == 'sources/modestproposal.txt\n':
            words = source['content']
            break
    words = utility.cleanse(words)
    histogram = Dictogram(words)
    histogram.count_to_possibility()
    histogram.get_sentence()
    sentence = histogram.print_sentence()
    return render_template('index.html', test = sentence)

@app.route('/', methods=['POST'])
def save():
    data = request.form
    possible_sent = sentences(content= data['sentence'])
    print(possible_sent.content)
    possible_sent.save()
    return redirect('/', code=302)

@app.route('/load_sources')
def load_sources():
    texts_list, word_list = [], []
    f = open('texts.txt', 'r')
    texts_list = f.readlines()
    f.close()
    for text in texts_list:
        g = open(text.strip(), 'r')
        word_list = g.readlines()
        g.close()
        new_text = sources(title=text, content=" ".join(word_list))
        new_text.save()