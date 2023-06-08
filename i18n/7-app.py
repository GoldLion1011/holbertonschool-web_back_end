#!/usr/bin/env python3
""" Flask App """


from flask import Flask, render_template, request, g
from flask_babel import Babel, gettext
import pytz


app = Flask(__name__)
babel = Babel(app)
gettext.__doc__ = """ gettext doc string """
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


def get_user():
    """ Returns a user dictionary or None """
    user_id = request.args.get("login_as")
    if user_id:
        return users.get(int(user_id))
    return None


@babel.localeselector
def get_locale() -> str:
    """ users preferred locale """
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    user = getattr(g, 'user', None)
    if user is not None:
        locale = user.locale
        if locale in app.config['LANGUAGES']:
            return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])
    # locale = request.args.get('locale')
    # if locale and locale in app.config['LANGUAGES']:
    #     return locale
    # return request.accept_languages.best_match(app.config['LANGUAGES'])


@babel.timezoneselector
def get_timezone() -> str:
    """ users preferred timezone """
    timezone = request.args.get('timezone')
    if timezone:
        try:
            return timezone
        except pytz.exceptions.UnknownTimeZoneError:
            pass
    user = getattr(g, 'user', None)
    if user is not None:
        timezone = user.timezone
        if timezone:
            try:
                return timezone
            except pytz.exceptions.UnknownTimeZoneError:
                pass
    return app.config['BABEL_DEFAULT_TIMEZONE']


@app.before_request
def before_request():
    """ Sets a user as a global on flask.g.user """
    g.user = get_user()


@app.route('/', methods=['GET'], strict_slashes=False)
def index():
    """ Index page """
    return render_template('7-index.html')

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, threaded=True, debug=True)
