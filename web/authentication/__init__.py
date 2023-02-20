#!/bin/python3

#################################################################################################
# Program:  Python / SQLite Web Application                                                     #
# Filename: __init__.py                                                                         #
# Author:   Jamie Allen                                                                         #
# Course:   BSc Digital Technology and Solutions                                                #
# Module:   Software Engineering and Agile                                                      #
# Version:  1.0                                                                                 #
#################################################################################################

from db.models import User


class AuthUser():
    id = 0
    email = ""
    role_name = ""
    first_name = "Anonymous"
    profile_image = ""
    is_authenticated = False
    is_existing_user = False

    def login(self, user: User):
        self.id = user.id
        self.email = user.email
        self.role_name = user.role_name
        self.first_name = user.first_name
        self.profile_image = user.profile_image
        self.is_authenticated = True
        self.is_existing_user = True

    def logout(self):
        self.id = 0
        self.email = ""
        self.role_name = ""
        self.first_name = "Anonymous"
        self.profile_image = ""
        self.is_authenticated = False

    def get_user(self):
        return self


#################################################################################################
# File: __init__.py                                                                             #
#                                                                                               #
# Disclaimer: The following source code is the sole work of the author unless otherwise stated. #
#                                                                                               #
# Copyright (c) Jamie Allen. All Rights Reserved.                                               #
#################################################################################################
