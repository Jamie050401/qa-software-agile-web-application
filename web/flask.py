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

import os as System
from flask import Flask

import web.index as Index

def CreateApplication(namespace : str):
    application = Flask(namespace)
    
    @application.route("/")
    def index():
        return Index.Contents()
    
    return application

def RunApplication(application : Flask):
    application.run(host="0.0.0.0", port=80)

#################################################################################################
# File: flask.py                                                                                #
#                                                                                               #
# Disclaimer: The following source code is the sole work of the author unless otherwise stated. #
#                                                                                               #
# Copyright (c) Jamie Allen. All Rights Reserved.                                               #
#################################################################################################