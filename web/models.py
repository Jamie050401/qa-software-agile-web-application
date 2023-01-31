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
from sqlalchemy import Column, Integer, String, ForeignKey
from werkzeug.security import generate_password_hash

from db import db_base

class Role(db_base):
    __tablename__ = "role"
    
    name = Column(String(60), primary_key = True)

class User(db_base):
    __tablename__ = "user"
    
    id = Column(Integer, primary_key = True, index = True)
    role_name = Column(String, ForeignKey("role.name"), nullable = False)
    email = Column(String(60), unique = True, nullable = False)
    first_name = Column(String(60), nullable = False)
    password = Column(String(255), nullable = False)
    is_valid = True
    
    def __init__(self):
        self.role_name = "User"
        self.email = "name@email.com"
        self.first_name = "Name"
        self.password = generate_password_hash("password", "sha256")
        self.is_valid = True
    
    def __init__(self, email, first_name, password, password_conf, role_name):
        def validate_user(email : str, first_name, password, password_conf):
            is_valid = True
            if len(email) < 4:
                is_valid = False
                flash("Email must be greater than 3 characters.", category="failure")
            if len(email) > 60:
                is_valid = False
                flash("Email cannot exceed 60 characters.", category="failure")
            if not email.__contains__("@"):
                is_valid = False
                flash("Email provided is not valid!", category = "failure")
            # TODO - Implement check to ensure email does not contain any other special characters
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
            # TODO - Implement check to ensure there is at least 1 upper case letter
            # TODO - Implement check to ensure there is at least 1 lower case letter
            # TODO - Implement check to ensure there is at least 1 number
            # TODO - Implement check to ensure there is at least 1 special character
            
            return is_valid
        
        is_valid = validate_user(email, first_name, password, password_conf)
        
        self.role_name = role_name
        self.email = email
        self.first_name = first_name
        self.password = generate_password_hash(password, "sha256")
        self.is_valid = is_valid

#################################################################################################
# File: models.py                                                                               #
#                                                                                               #
# Disclaimer: The following source code is the sole work of the author unless otherwise stated. #
#                                                                                               #
# Copyright (c) Jamie Allen. All Rights Reserved.                                               #
#################################################################################################