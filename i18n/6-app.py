#/usr/bin/env python3
""" i18n Flask App """


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


@app.before_request
def before_request():
    """ Sets a user as a global on flask.g.user """
    g.user = get_user()


@babel.localeselector
def get_locale():
    """ Select the best match for supported languages """
    locale = request.args.get("locale")
    if locale and locale in app.config['LANGUAGES']:
        return locale
    if g.user:
        user_locale = g.user.get("locale")
        if user_locale and user_locale in app.config['LANGUAGES']:
            return user_locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """ Rendering the index.html file """
    return render_template('6-index.html')


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, threaded=True, debug=True)
