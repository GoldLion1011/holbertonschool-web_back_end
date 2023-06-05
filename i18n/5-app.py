#!/usr/bin/env python3
""" Flask App """


from flask import Flask, render_template, request
from flask_babel import Babel


app = Flask(__name__)
babel = Babel(app)
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config:
    """ Config app class """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@babel.localeselector
def get_locale():
    """ get locale """
    locale = request.args.get('locale')
    if locale and locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


def get_user(login_as):
    """ get user """
    if login_as in users:
        return users.get(login_as)
    return None


@app.before_request
def before_request():
    """ before request """
    user = get_user(request.args.get('login_as'))
    if user:
        g.user = user
    else:
        g.user = None


@app.route('/', methods=['GET'], strict_slashes=False)
def index():
    """ Index page """
    return render_template('5-index.html')


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, threaded=True, debug=True)
