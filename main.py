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
# from werkzeug.middleware.proxy_fix import ProxyFix

import web as Website
import db as Database

application = Website.create_application()

if __name__ == '__main__':
    IS_PRODUCTION = True

    if IS_PRODUCTION:
        Database.create_database()

        # application.wsgi_app = ProxyFix(application.wsgi_app, x_for=1, x_proto=1, x_host=1, x_prefix=1)

        Website.run_application(
            application, environ['IP_ADDRESS'], environ['IS_DEBUG'])
    else:
        IP_ADDRESS = "127.0.0.1"
        IS_DEBUG = True
        Database.create_database()
        Website.run_application(application, IP_ADDRESS, IS_DEBUG)


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
