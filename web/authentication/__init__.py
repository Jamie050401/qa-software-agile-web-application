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

from db.models import User


class AuthUser():
    user_id = 0
    role_name = ""
    first_name = "Anonymous"
    profile_image = ""
    is_authenticated = False
    is_existing_user = False

    def login(self, user: User):
        self.user_id = user.id
        self.role_name = user.role_name
        self.first_name = user.first_name
        self.profile_image = user.profile_image
        self.is_authenticated = True

    def logout(self):
        self.user_id = 0
        self.role_name = ""
        self.first_name = "Anonymous"
        self.profile_image = ""
        self.is_authenticated = False
        self.is_existing_user = True


# TODO - Determine if this is appropriate - may result in only one user across the entire website
current_user = AuthUser()

#################################################################################################
# File: __init__.py                                                                             #
#                                                                                               #
# Disclaimer: The following source code is the sole work of the author unless otherwise stated. #
#                                                                                               #
# Copyright (c) Jamie Allen. All Rights Reserved.                                               #
#################################################################################################
