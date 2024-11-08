#!/usr/bin/env python3
"""
The main file to get locale from request
"""

from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)

class Config(object):
    """
    A class to configure the application
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)

@babel.localeselector
def get_locale() -> str:
    """
    A function to select the language
    Returns:
    str: the language
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])

@app.route('/', methods=['GET'], strict_slashes=False)
def home() -> str:
    """
    Main Application page. Renders template
    Returns:
    str: rendered template
    """

    return render_template('2-index.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
