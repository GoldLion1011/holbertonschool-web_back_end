#!/usr/bin/env python3
""" Flask App """


from flask import Flask, render_template, request, g
from flask_babel import Babel, gettext


app = Flask(__name__)
babel = Babel(app)
gettext.__doc__ = """ gettext doc string """
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config(object):
    """ Config app class """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


def get_user():
    """ get user """
    user_id = request.args.get('login_as')
    if user_id and int(user_id) in users:
        return users[int(user_id)]
    return None


@babel.localeselector
def get_locale():
    """ get locale """
    locale = request.args.get('locale')
    if locale and locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


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
