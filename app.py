from flask import (Flask, render_template, redirect, url_for, make_response, flash, request, session)
import mongoengine
from pymongo import MongoClient 
from mongoengine import (Document, connect, StringField)
from flask_mongoengine import QuerySet
import os, json
import utility
from nth_order_markov_for_web import Dictogram
import config_module

app = Flask(__name__)

if(os.environ['SETTINGS'] == 'DevelopmentConfig'):
    connect('markov_data', host=config_module.DevelopmentConfig.DATABASE_URI)
elif(os.environ['SETTINGS'] == 'ProductionConfig'):
    connect('markov_data', host=config_module.ProductionConfig.DATABASE_URI)
else:
    connect('markov_data', host=config_module.Config.DATABASE_URI)
    
class sources(Document):
    title = StringField(required=True)
    content = StringField(required=True)
    third_order = StringField(required=True)
    fourth_order = StringField(required=True)

class sentences(Document):
    content = StringField(required=True)
    source = StringField(required=True)

@app.route('/')
def reroute():
    return redirect('/sentence/frankenstein', code=302)

@app.route('/', methods=['POST'])
def save():
    data = request.form
    possible_sent = sentences(content= data['sentence'], source = data['source'])
    possible_sent.save()
    return redirect(request.referrer, code=302)

@app.route('/sentence/<source_name>')
def new_sentence(source_name):
    source = sources.objects(title__exact = 'sources/'+source_name+'.txt\n').first()
    histogram = Dictogram.from_dict(json.loads(source['third_order']))
    sentence = histogram.get_sentence()
    print(sentence)
    return render_template('index.html', test = sentence, sentence_source = source['title'])

@app.route('/saved')
def show_saved():
    saved = []
    for sentence in sentences.objects:
        sentence = sentence.to_mongo().to_dict()
        saved.append(sentence['content'])
        source_name = sentence['source'][8:-5]
        saved.append(source_name)
    return render_template('saved.html', sentences = saved, source = sources)

# @app.route('/load_sources')
# def load_sources():
#     # sources.drop_collection()
#     texts_list, word_list = [], []
#     f = open('texts.txt', 'r')
#     texts_list = f.readlines()
#     f.close()
#     for text in texts_list:
#         g = open(text.strip(), 'r')
#         word_list = g.readlines()
#         g.close()
#         words = utility.cleanse(word_list)
#         histogram_third = Dictogram(words, 3)
#         histogram_third.count_to_possibility()
#         histogram_fourth = Dictogram(words, 4)
#         histogram_fourth.count_to_possibility()
#         new_text = sources(title=text, content=" ".join(word_list), 
#                             third_order=json.dumps(histogram_third),
#                             fourth_order=json.dumps(histogram_fourth))
#         new_text.save()
#     return redirect('/', code=302)
