from flask import Flask, render_template

__author__ = 'andres'


app = Flask(__name__)
app.config.from_object('src.config')
app.secret_key = "123"


@app.route('/')
def home():
    return render_template('home.html', title='Projektikaust')
