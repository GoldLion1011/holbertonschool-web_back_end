#!/usr/bin/env python3
""" i18n Flask App """


from flask import Flask, render_template
app = Flask(__name__)


@app.route('/', methods=['GET'], strict_slashes=False)
def index():
    """ Index page """
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run('0.0.0.0', 5000, threaded=True, debug=True)
