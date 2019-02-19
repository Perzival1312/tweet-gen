from flask import (Flask, render_template, redirect, url_for, make_response, flash, request)
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', test = "this is a test")