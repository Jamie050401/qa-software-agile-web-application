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

from flask import Flask

import web.views as Views

def CreateApplication(namespace : str):
    application = Flask(namespace)
    
    @application.route("/")
    def index():
        return Views.Index()
    
    return application

def RunApplication(application : Flask):
    application.run(host="0.0.0.0", port=80)
    
application = CreateApplication(__name__)
RunApplication(application)

#################################################################################################
# File: __init__.py                                                                             #
#                                                                                               #
# Disclaimer: The following source code is the sole work of the author unless otherwise stated. #
#                                                                                               #
# Copyright (c) Jamie Allen. All Rights Reserved.                                               #
#################################################################################################