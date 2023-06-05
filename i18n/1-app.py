#!/usr/bin/env python3
""" Flask App """


from flask import Flask, render_template
from flask_babel import Babel


app = Flask(__name__)
babel = Babel(app)


class Config:
    """ Config app class """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@app.route('/', methods=['GET'], strict_slashes=False)
def index():
    """ Index page """
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run('0.0.0.0', 5000, threaded=True, debug=True)
