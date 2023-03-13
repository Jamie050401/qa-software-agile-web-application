#!/bin/python3

#################################################################################################
# Program:  Python / SQLite Web Application                                                     #
# Filename: main.py                                                                             #
# Author:   Jamie Allen                                                                         #
# Course:   BSc Digital Technology and Solutions                                                #
# Module:   Software Engineering and Agile                                                      #
# Version:  1.0                                                                                 #
#################################################################################################

from os import environ, path
from werkzeug.middleware.proxy_fix import ProxyFix
from iniconfig import IniConfig

import web as Website
import db as Database

config = IniConfig("./data/config.ini")
app = Website.create_application()

# https://stackoverflow.com/questions/43878953/how-does-one-detect-if-one-is-running-within-a-docker-container-within-python
def is_docker():
    file_path = '/proc/self/cgroup'
    has_docker_env = path.exists('/.dockerenv')
    in_docker_env = path.isfile(file_path) and any('docker' in line for line in open(file_path, encoding="utf-8"))
    return (has_docker_env or in_docker_env)

if __name__ == '__main__':
    IS_PRODUCTION = is_docker()
    IP_ADDRESS = config["SETTINGS"]["IP_ADDRESS"]
    IS_DEBUG = config["SETTINGS"]["IS_DEBUG"] == "TRUE"

    Database.create_database()

    if IS_PRODUCTION:
        IP_ADDRESS = environ['IP_ADDRESS']
        IS_DEBUG = environ['IS_DEBUG'] == "TRUE"
        app.wsgi_app = ProxyFix(app.wsgi_app)
    else:
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
# SQL Alchemy (xxxx) Finish reference here ...                                                  #
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

# Other references:
#   - Flask docs
#   - Gunicorn docs
#   - SQLAlchemy docs
#   - Bootstrap docs
