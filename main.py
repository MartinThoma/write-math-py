#!/usr/bin/env python

"""Backend of write-math.com"""

import os
import logging
import sys

logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s',
                    level=logging.DEBUG,
                    stream=sys.stdout)

from flask import Flask
from flask import jsonify
from flask import request
from flask import render_template
from flask import send_from_directory
from werkzeug.exceptions import default_exceptions
from werkzeug.exceptions import HTTPException
from utils.misc import json_response

__all__ = ['make_json_app']


def make_json_app(import_name, **kwargs):
    """
    Creates a JSON-oriented Flask app.

    All error responses that you don't specifically
    manage yourself will have application/json content
    type, and will contain JSON like this (just an example):

    { "message": "405: Method Not Allowed" }
    """
    def make_json_error(ex):
        response = jsonify(message=str(ex))
        response.status_code = (ex.code
                                if isinstance(ex, HTTPException)
                                else 500)
        return response

    app = Flask(import_name, **kwargs)

    for code in default_exceptions.keys():
        app.error_handler_spec[None][code] = make_json_error

    return app

app = make_json_app(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/docs/')
def send_js_nopath():
    return send_from_directory('docs', 'index.html')


@app.route('/docs/<path:path>')
def send_js(path):
    return send_from_directory('docs', path)


@app.route('/api/classification/<int:recording_id>', methods=['GET'])
def get_classification(recording_id):
    return 'TODO: Get classification of %i' % (recording_id)


@app.route('/api/recording', methods=['POST'])
def create_recording():
    if 'recording' not in request.form:
        return json_response(400, {'error': 'recording has to be send.'})
    if 'recording_id' not in request.form:
        return json_response(400, {'error': ("recording_id has to be send. "
                                             "If it is the first request, "
                                             "send recording_id='None'")})
    recording = request.form['recording']
    recording_id = request.form['recording_id']
    if recording_id == 'None':
        return 'create recording'
    else:
        recording_id = int(recording_id)
        return 'edit recording with %i' % recording_id


# User administration
@app.route('/api/user', methods=['POST'])
def user_create():
    return 'TODO: user_create'


@app.route('/api/user/login', methods=['POST'])
def user_login():
    email = request.form['email']
    password = request.form['password']
    return "do_the_login()"


# Error handlers
@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404


# Front-End
@app.route('/login', methods=['GET'])
def login_form():
    return "show_the_login_form()"


if __name__ == '__main__':
    if 'ENV' in os.environ and os.environ['ENV'] == 'development':
        app.logger.info("ENV: development")
        app.debug = True
    else:
        app.logger.info("ENV: production")
    app.run(host='0.0.0.0')
