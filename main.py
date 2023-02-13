#!/bin/python3

#################################################################################################
# Program:  Python / SQLite Web Application                                                     #
# Filename: main.py                                                                             #
# Author:   Jamie Allen                                                                         #
# Course:   BSc Digital Technology and Solutions                                                #
# Module:   Software Engineering and Agile                                                      #
# Version:  1.0                                                                                 #
# Date:     xx/xx/23                                                                            #
#################################################################################################

from os import environ
from werkzeug.middleware.proxy_fix import ProxyFix
from iniconfig import IniConfig

import web as Website
import db as Database

config = IniConfig("config.ini")

app = Website.create_application()

if __name__ == '__main__':
    IS_PRODUCTION = config["SETTINGS"]["IS_PRODUCTION"] == "True"
    IP_ADDRESS = config["SETTINGS"]["IP_ADDRESS"]
    IS_DEBUG = config["SETTINGS"]["IS_DEBUG"] == "True"

    if IS_PRODUCTION:
        IP_ADDRESS = environ['IP_ADDRESS']
        IS_DEBUG = environ['IS_DEBUG']
        app.wsgi_app = ProxyFix(app.wsgi_app,
                                x_for=1, x_proto=1, x_host=1, x_prefix=1)

    Database.create_database()
    Website.run_application(app, IP_ADDRESS, IS_DEBUG)


#################################################################################################
# File: main.py                                                                                 #
#                                                                                               #
# Disclaimer: The following source code is the sole work of the author unless otherwise stated. #
#                                                                                               #
# Copyright (c) Jamie Allen. All Rights Reserved.                                               #
#################################################################################################

# TODO - Finish adding references here

#################################################################################################
# References:                                                                                   #
#                                                                                               #
# Python is used throughout this application. Other Packages are as follows:                    #
#                                                                                               #
# Python (xxxx) Finish Python reference here ...                                                #
#                                                                                               #
# Flask (xxxx) Finish reference here ...                                                        #
#                                                                                               #
# Flask SQL Alchemy (xxxx) Finish reference here ...                                            #
#                                                                                               #
# Flask Login (xxxx) Finish reference here ...                                                  #
#                                                                                               #
# pytest (xxxx) Finish reference here ...                                                       #
#                                                                                               #
# Bootstrap (xxxx) Finish reference here ...                                                    #
#                                                                                               #
# Add references to other packages here ...                                                     #
#                                                                                               #
# References used within this application are as follows:                                       #
#                                                                                               #
# Flask Tutorial for Beginners (2022) Finish reference here ...                                 #
#                                                                                               #
# HTML and CSS Tutorial (xxxx) Finish reference here ...                                        #
#                                                                                               #
# Python Website Tutorial (xxxx) Finish reference here ...                                      #
#                                                                                               #
# Add other references here ...                                                                 #
#                                                                                               #
#################################################################################################
