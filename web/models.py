#!/bin/python3

#################################################################################################
# Program:  Python / SQLite Web Application                                                     #
# Filename: models.py                                                                           #
# Author:   Jamie Allen                                                                         #
# Course:   BSc Digital Technology and Solutions                                                #
# Module:   Software Engineering and Agile                                                      #
# Version:  1.0                                                                                 #
# Date:     xx/xx/23                                                                            #
#################################################################################################

from flask import flash
from flask_login import UserMixin
from werkzeug.security import generate_password_hash # NOTE - This comes from flask_login

from . import db

# NOTE - For foreign keys on other DB tables:
#  user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
#  db.relationship("<ClassName>") - Can be used to attribute foreign objects to the current object

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(60), unique = True)
    first_name = db.Column(db.String(60))
    password = db.Column(db.String(60))
    is_valid = True
    
    def __init__(self, email : str, first_name : str, password : str, password_conf : str):
        # TODO - Expand and improve these data validation checks: check for invalid characters, validate emails i.e. must have @ symbol, etc.
        def validate_user(email : str, first_name : str, password : str, password_conf : str):
            is_valid = True
            if len(email) < 4:
                is_valid = False
                flash("Email must be greater than 3 characters.", category="failure")
            if len(email) > 60:
                is_valid = False
                flash("Email cannot exceed 60 characters.", category="failure")
            if len(first_name) < 2:
                is_valid = False
                flash("First name must be greater than 1 character.", category="failure")
            if len(first_name) > 60:
                is_valid = False
                flash("First name cannot exceed 60 characters.", category="failure")
            if password != password_conf:
                is_valid = False
                flash("Passwords don't match!", category="failure")
            if len(password) < 12:
                is_valid = False
                flash("Passwords must be greater than 11 characters.", category="failure")
            if len(password) > 60:
                is_valid = False
                flash("Passwords cannot exceed 60 characters.", category="failure")
            return is_valid
        
        is_valid = validate_user(email, first_name, password, password_conf)
        
        self.email = email
        self.first_name = first_name
        self.password = generate_password_hash(password, method="sha256")
        self.is_valid = is_valid

#################################################################################################
# File: models.py                                                                               #
#                                                                                               #
# Disclaimer: The following source code is the sole work of the author unless otherwise stated. #
#                                                                                               #
# Copyright (c) Jamie Allen. All Rights Reserved.                                               #
#################################################################################################