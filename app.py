from flask import (
    Flask,
    render_template,
    redirect,
    url_for,
    make_response,
    flash,
    request,
    session,
    jsonify,
)
import mongoengine
from pymongo import MongoClient
from mongoengine import Document, connect, StringField
from flask_mongoengine import QuerySet
from flask_scss import Scss
import os, json, requests, PIL
from PIL import Image, ImageDraw
import utility, config_module, twitter, imgur
from nth_order_markov_for_web import Markov
from flask_assets import Environment, Bundle

app = Flask(__name__)

## ------------------------------------ ##
## ------------------------------------ ##

assets = Environment(app)
assets.url = app.static_url_path
scss = Bundle("style.scss", filters="pyscss", output="all.css")
assets.config["SECRET_KEY"] = os.environ["SESSION_KEY"]
assets.config["PYSCSS_LOAD_PATHS"] = assets.load_path
assets.config["PYSCSS_STATIC_URL"] = assets.url
assets.config["PYSCSS_STATIC_ROOT"] = assets.directory
assets.config["PYSCSS_ASSETS_URL"] = assets.url
assets.config["PYSCSS_ASSETS_ROOT"] = assets.directory
assets.register("scss_all", scss)

## ------------------------------------ ##

SESSION_TYPE = config_module.Config.SESSION_TYPE
app.secret_key = os.environ["SESSION_KEY"]

if os.environ["SETTINGS"] == "DevelopmentConfig":
    connect("markov_data", host=config_module.DevelopmentConfig.DATABASE_URI)
elif os.environ["SETTINGS"] == "ProductionConfig":
    connect("markov_data", host=config_module.ProductionConfig.DATABASE_URI)
else:
    connect("markov_data", host=config_module.Config.DATABASE_URI)

## ------------------------------------ ##


class sources(Document):
    title = StringField(required=True)
    content = StringField(required=True)
    markov_model = StringField(required=True)


class sentences(Document):
    content = StringField(required=True)
    source = StringField(required=True)


## ------------------------------------ ##
## ------------------------------------ ##


def get_new_sentence(source_name):
    source = sources.objects(title__icontains=source_name).first()
    histogram = Markov.from_dict(json.loads(source["markov_model"]))
    sentence = histogram.get_sentence()
    title = source["title"]
    return sentence, title


## ------------------------------------ ##
## ------------------------------------ ##


@app.route("/")
def reroute():
    return redirect("/sentence/frankenstein", code=302)


## ------------------------------------ ##


@app.route("/", methods=["POST"])
def save():
    data = request.form
    possible_sent = sentences(content=data["sentence"], source=data["source"])
    possible_sent.save()
    return redirect(request.referrer, code=302)


## ------------------------------------ ##


@app.route("/sentence/<source_name>")
def new_sentence(source_name):
    session["source"] = source_name
    sentence, title = get_new_sentence(source_name)
    return render_template("index.html", test=sentence, sentence_source=title)


## ------------------------------------ ##


@app.route("/sentence/<source_name>", methods=["POST"])
def AJAX_new_sentence(source_name):
    sentence, title = get_new_sentence(source_name)
    return sentence


## ------------------------------------ ##


@app.route("/saved")
def show_saved():
    saved = []
    for sentence in sentences.objects:
        sentence = sentence.to_mongo().to_dict()
        saved.append(sentence["content"])
        # remove excess text so as to only have the name of the source
        source_name = sentence["source"][8:-4]
        saved.append(source_name)
    return render_template("saved.html", sentences=saved, return_to=session["source"])


## ------------------------------------ ##


@app.route("/share/twitter", methods=["POST"])
def Twitter_share():
    data = request.form
    sentence = data["sentence"]
    source = data["source"]
    twitter.tweet(sentence, source)
    return redirect(request.referrer, code=302)


## ------------------------------------ ##


@app.route("/share/imgur", methods=["POST"])
def Imgur_share():
    data = request.form
    sentence = data["sentence"]
    image = imgur.prepare(sentence)
    imgur.post(image)
    return redirect(request.referrer, code=302)


## ------------------------------------ ##


@app.route("/load_sources")
def load_sources():
    sources.drop_collection()
    texts_list, word_list = [], []
    f = open("texts.txt", "r")
    texts_list = f.readlines()
    f.close()
    print(texts_list)
    for text in texts_list:
        g = open(text.strip(), "r")
        word_list = g.readlines()
        g.close()
        words = utility.cleanse(word_list)
        histogram_third = Markov(words, 3)
        histogram_third.count_to_possibility()
        new_text = sources(
            title=text,
            content=" ".join(word_list),
            markov_model=json.dumps(histogram_third),
        )
        new_text.save()
    return redirect("/", code=302)
