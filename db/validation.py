#!/bin/python3

#################################################################################################
# Program:  Python / SQLite Web Application                                                     #
# Filename: validation.py                                                                       #
# Author:   Jamie Allen                                                                         #
# Course:   BSc Digital Technology and Solutions                                                #
# Module:   Software Engineering and Agile                                                      #
# Version:  1.0                                                                                 #
#################################################################################################

from flask import flash

from db.models.roles import roles

def validate_user(email: str, first_name : str, password : str, password_conf : str, role_name : str):
    is_valid = False
    if len(email) == 0:
        flash("You must provide an email address!", category="failure")
    elif len(first_name) == 0:
        flash("You must provide a first name!", category="failure")
    elif len(password) == 0:
        flash("You must provide a password!", category="failure")
    elif len(email) < 4:
        flash("Email must be greater than 3 characters.",
              category="failure")
    elif len(email) > 60:
        flash("Email cannot exceed 60 characters.", category="failure")
    elif not "@" in email:
        flash("Email provided is not valid!", category="failure")
    # TODO - Implement check to ensure email does not contain any other special characters
    elif len(first_name) < 2:
        flash("First name must be greater than 1 character.",
              category="failure")
    elif len(first_name) > 60:
        flash("First name cannot exceed 60 characters.",
              category="failure")
    elif password != password_conf:
        flash("Passwords don't match!", category="failure")
    elif len(password) < 12:
        flash("Passwords must be greater than 11 characters.",
              category="failure")
    elif len(password) > 60:
        flash("Passwords cannot exceed 60 characters.", category="failure")
    # TODO - Implement check to ensure there is at least 1 upper case letter
    # TODO - Implement check to ensure there is at least 1 lower case letter
    # TODO - Implement check to ensure there is at least 1 number
    # TODO - Implement check to ensure there is at least 1 special character
    elif role_name not in roles:
        flash("Invalid role assigned to user!", category="failure")
    else:
        is_valid = True

    return is_valid

def validate_ticket(team : str, issue_type : str, issue_desc : str):
    is_valid = True # This should be False
    # TODO - Implement validation logic
    return is_valid

#################################################################################################
# File: validation.py                                                                           #
#                                                                                               #
# Disclaimer: The following source code is the sole work of the author unless otherwise stated. #
#                                                                                               #
# Copyright (c) Jamie Allen. All Rights Reserved.                                               #
#################################################################################################
