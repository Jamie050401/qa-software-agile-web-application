#!/bin/python3

#################################################################################################
# Program:  Python / SQLite Web Application                                                     #
# Filename: __init__.py                                                                         #
# Author:   Jamie Allen                                                                         #
# Course:   BSc Digital Technology and Solutions                                                #
# Module:   Software Engineering and Agile                                                      #
# Version:  1.0                                                                                 #
# Date:     xx/xx/23                                                                            #
#################################################################################################

from os import urandom
from flask import Flask

from web.views import views
from web.authentication.auth import auth


def create_application():
    application = Flask(__name__)
    application.config['SECRET_KEY'] = urandom(12)

    application.register_blueprint(views, url_prefix='/')
    application.register_blueprint(auth, url_prefix='/')

    return application


def run_application(application: Flask, ip_address, is_debug: bool):
    application.run(host=ip_address, port=80, debug=is_debug)

#################################################################################################
# File: __init__.py                                                                             #
#                                                                                               #
# Disclaimer: The following source code is the sole work of the author unless otherwise stated. #
#                                                                                               #
# Copyright (c) Jamie Allen. All Rights Reserved.                                               #
#################################################################################################
