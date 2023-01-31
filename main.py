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

import db as Database
import web as Website

application = Website.create_application()

if __name__ == '__main__':
    Database.create_database()
    
    ip_address = "127.0.0.1"
    is_debug = True
    Website.run_application(application, ip_address, is_debug)

#################################################################################################
# File: main.py                                                                                 #
#                                                                                               #
# Disclaimer: The following source code is the sole work of the author unless otherwise stated. #
#                                                                                               #
# Copyright (c) Jamie Allen. All Rights Reserved.                                               #
#################################################################################################

#################################################################################################
# References:                                                                                   #
#                                                                                               #
# Python is used throughout this application. Other Packages are as follows:                    #
#                                                                                               #
# Python (xxxx) TODO - Finish Python reference here ...                                         #
#                                                                                               #
# Flask (xxxx) TODO - Finish reference here ...                                                 #
#                                                                                               #
# Flask SQL Alchemy (xxxx) TODO - Finish reference here ...                                     #
#                                                                                               #
# Flask Login (xxxx) TODO - Finish reference here ...                                           #
#                                                                                               #
# pytest (xxxx) TODO - Finish reference here ...                                                #
#                                                                                               #
# Bootstrap (xxxx) TODO - Finish reference here ...                                             #
#                                                                                               #
# TODO - Add references to other packages here ...                                              #
#                                                                                               #
# References used within this application are as follows:                                       #
#                                                                                               #
# Flask Tutorial for Beginners (2022) TODO - Finish reference here ...                          #
#                                                                                               #
# HTML and CSS Tutorial (xxxx) TODO - Finish reference here ...                                 #
#                                                                                               #
# Python Website Tutorial (xxxx) TODO - Finish reference here ...                               #
#                                                                                               #
# TODO - Add other references here ...                                                          #
#                                                                                               #
#################################################################################################