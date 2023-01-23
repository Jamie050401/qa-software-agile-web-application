#!/bin/python3

#################################################################################################
# Program:  Python / SQLite Web Application                                                     #
# Filename: flask.py                                                                            #
# Author:   Jamie Allen                                                                         #
# Course:   BSc Digital Technology and Solutions                                                #
# Module:   Software Engineering and Agile                                                      #
# Version:  1.0                                                                                 #
# Date:     xx/xx/23                                                                            #
#################################################################################################

from flask import Flask

def indexContents():
    return "Hello World!"

def createApplication():
    application = Flask(__name__)
    
    @application.route("/")
    def index():
        return indexContents()
    
    return application

def runApplication(application : Flask):
    application.run(host="0.0.0.0", port=80)

#################################################################################################
# File: index.py                                                                                #
#                                                                                               #
# Disclaimer: The following source code is the sole work of the author unless otherwise stated. #
#                                                                                               #
# Copyright (c) Jamie Allen. All Rights Reserved.                                               #
#################################################################################################