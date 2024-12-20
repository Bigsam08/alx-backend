#!/usr/bin/env python3
''' babel configuration for language'''
from flask import Flask, render_template
from flask_babel import Babel


class Config:
    ''' class to configure and set default time nd lang'''
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@app.route('/')
def home():
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run(debug=True)
