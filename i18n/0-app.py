#!/usr/bin/env python3
""" Flask App """


from flask import Flask
app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello world'


if __name__ == '__main__':
    app.run()
