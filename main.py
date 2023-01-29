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

import os as System

import web as Website

application = Website.create_application()

# TODO - Replace the favicon.ico with actual favicon ...
# TODO - Implement external config file to house options e.g. is_debug
# TODO - Configure logic to allow passing of config file via dependency injection
if __name__ == '__main__':
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