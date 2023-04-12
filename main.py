#!/bin/python3

#################################################################################################
# Program:  Python / SQLite Web Application                                                     #
# Filename: main.py                                                                             #
# Author:   Jamie Allen                                                                         #
# Course:   BSc Digital Technology and Solutions                                                #
# Module:   Software Engineering and Agile                                                      #
# Version:  1.0                                                                                 #
#################################################################################################

#################################################################################################
# File: main.py                                                                                 #
#                                                                                               #
# Disclaimer: The following source code is the sole work of the author unless otherwise stated. #
#                                                                                               #
# Copyright (c) Jamie Allen. All Rights Reserved.                                               #
#################################################################################################

from os import environ, path
from werkzeug.middleware.proxy_fix import ProxyFix
from iniconfig import IniConfig

import web as Website
import db as Database

config = IniConfig("./data/config.ini")
app = Website.create_application()

# Identify Docker Environment (2021)
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

##################################################################################################################################
# References:                                                                                                                    #
#                                                                                                                                #
# Python is used throughout this application. Other Packages are as follows:                                                     #
#                                                                                                                                #
#   Flask (2023) Available from:                                                                                                 #
#     https://pypi.org/project/Flask/                                                                                            #
#                                                                                                                                #
#   SQL Alchemy (2023) Available from:                                                                                           #
#     https://pypi.org/project/SQLAlchemy/                                                                                       #
#                                                                                                                                #
#   Werkzeug (2023) Available from:                                                                                              #
#     https://pypi.org/project/Werkzeug/                                                                                         #
#                                                                                                                                #
#   iniconfig (2023) Available from:                                                                                             #
#     https://pypi.org/project/iniconfig/                                                                                        #
#                                                                                                                                #
#   Gunicorn (2023) Available from:                                                                                              #
#     https://pypi.org/project/gunicorn/                                                                                         #
#                                                                                                                                #
#   pytest (2023) Available from:                                                                                                #
#     https://pypi.org/project/pytest/                                                                                           #
#                                                                                                                                #
#   Bootstrap (2023) Available from                                                                                              #
#     https://getbootstrap.com/                                                                                                  #
#                                                                                                                                #
#   Plus any and all dependencies required by the above packages.                                                                #
#                                                                                                                                #
# References used within this application are as follows:                                                                        #
#                                                                                                                                #
#   Flask Documentation (2010) Available from:                                                                                   #
#     https://flask.palletsprojects.com/en/2.2.x/                                                                                #
#                                                                                                                                #
#   Flask Tutorial for Beginners (2022) Available from:                                                                          #
#     https://www.youtube.com/watch?v=5aYpkLfkgRE&t                                                                              #
#                                                                                                                                #
#   Flask-SQLAlchemy vs SQLAlchemy (2020) Available from:                                                                        #
#     https://towardsdatascience.com/use-flask-and-sqlalchemy-not-flask-sqlalchemy-5a64fafe22a4                                  #
#                                                                                                                                #
#   SQLAlchemy Documentation (2023) Available from:                                                                              #
#     https://docs.sqlalchemy.org/en/20/                                                                                         #
#                                                                                                                                #
#   HTML and CSS Tutorial (2021) Available from:                                                                                 #
#     https://www.youtube.com/watch?v=lIGKKnfLobA                                                                                #
#                                                                                                                                #
#   Gunicorn Documentation (2021) Available from:                                                                                #
#     https://docs.gunicorn.org/en/stable/                                                                                       #
#                                                                                                                                #
#   Python Website Tutorial (2021) Available from:                                                                               #
#     https://www.youtube.com/watch?v=dam0GPOAvVI                                                                                #
#                                                                                                                                #
#   Boostrap Documentation (2023) Available from:                                                                                #
#     https://getbootstrap.com/docs/5.0/getting-started/introduction/                                                            #
#                                                                                                                                #
#   Guide to Markdown (2023) Available from:                                                                                     #
#     https://www.markdownguide.org/basic-syntax/                                                                                #
#                                                                                                                                #
#   Identify Docker Environment (2021) Available from:                                                                           #
#     https://stackoverflow.com/questions/43878953/how-does-one-detect-if-one-is-running-within-a-docker-container-within-python #
#                                                                                                                                #
##################################################################################################################################
