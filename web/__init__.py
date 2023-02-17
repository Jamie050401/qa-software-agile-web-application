#!/bin/python3

#################################################################################################
# Program:  Python / SQLite Web Application                                                     #
# Filename: __init__.py                                                                         #
# Author:   Jamie Allen                                                                         #
# Course:   BSc Digital Technology and Solutions                                                #
# Module:   Software Engineering and Agile                                                      #
# Version:  1.0                                                                                 #
#################################################################################################

from os import urandom
from flask import Flask

from web.views import views
from web.authentication.auth import auth


def create_application():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = urandom(12)

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    return app


def run_application(app: Flask, ip_address, is_debug: bool):
    app.run(host=ip_address, port=80, debug=is_debug)

#################################################################################################
# File: __init__.py                                                                             #
#                                                                                               #
# Disclaimer: The following source code is the sole work of the author unless otherwise stated. #
#                                                                                               #
# Copyright (c) Jamie Allen. All Rights Reserved.                                               #
#################################################################################################
