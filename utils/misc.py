#!/usr/bin/env python

from flask import jsonify


def json_response(statuscode, data):
    response = jsonify(data)
    response.status_code = statuscode
    return response
