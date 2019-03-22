from flask import (Flask, render_template, redirect, url_for, make_response, flash, request, session)
import mongoengine
from pymongo import MongoClient 
from mongoengine import (Document, connect, StringField)
from flask_mongoengine import QuerySet
from flask_scss import Scss
import os, json, requests, PIL
from PIL import Image, ImageDraw
import utility, config_module, twitter, imgur
from nth_order_markov_for_web import Markov
from flask_assets import Environment, Bundle

app = Flask(__name__)

assets     = Environment(app)
assets.url = app.static_url_path
scss       = Bundle('style.scss', filters='pyscss', output='all.css')

assets.config['SECRET_KEY'] = os.environ['SESSION_KEY']
assets.config['PYSCSS_LOAD_PATHS'] = assets.load_path
assets.config['PYSCSS_STATIC_URL'] = assets.url
assets.config['PYSCSS_STATIC_ROOT'] = assets.directory
assets.config['PYSCSS_ASSETS_URL'] = assets.url
assets.config['PYSCSS_ASSETS_ROOT'] = assets.directory

assets.register('scss_all', scss)
# Scss(app)#, static_dir='static', asset_dir='assets')
SESSION_TYPE = config_module.Config.SESSION_TYPE
app.secret_key = os.environ['SESSION_KEY']

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
    session['source'] = source_name
    source = sources.objects(title__icontains = source_name).first()
    histogram = Markov.from_dict(json.loads(source['fourth_order']))
    sentence = histogram.get_sentence()
    return render_template('index.html', test = sentence, sentence_source = source['title'])

@app.route('/saved')
def show_saved():
    saved = []
    for sentence in sentences.objects:
        sentence = sentence.to_mongo().to_dict()
        saved.append(sentence['content'])
        source_name = sentence['source'][8:-4]
        saved.append(source_name)
    return render_template('saved.html', sentences = saved, source = sources, return_to = session['source'])

@app.route('/share/twitter', methods=['POST'])
def Twitter_share():
    data = request.form 
    sentence = data['sentence']
    twitter.tweet(sentence)
    return redirect(request.referrer, code=302)

@app.route('/share/imgur', methods=['POST'])
def Imgur_share():
    data = request.form 
    sentence = data['sentence']
    image = imgur.prepare(sentence)
    imgur.post(image)
    return redirect(request.referrer, code=302)

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
#         histogram_third = Markov(words, 3)
#         histogram_third.count_to_possibility()
#         histogram_fourth = Markov(words, 4)
#         histogram_fourth.count_to_possibility()
#         new_text = sources(title=text, content=" ".join(word_list), 
#                             third_order=json.dumps(histogram_third),
#                             fourth_order=json.dumps(histogram_fourth))
#         new_text.save()
#     return redirect('/', code=302)
