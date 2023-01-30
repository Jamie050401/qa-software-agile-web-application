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
    
    id = Column(Integer, primary_key = True, index = True)
    name = Column(String(60), unique = True, nullable = False)

class User(db_base):
    __tablename__ = "user"
    
    id = Column(Integer, primary_key = True, index = True)
    role_id = Column(Integer, ForeignKey("role.id"), nullable = False)
    email = Column(String(60), unique = True, nullable = False)
    first_name = Column(String(60), nullable = False)
    password = Column(String(255), nullable = False)
    is_valid = True
    
    def __init__(self, email : str, first_name : str, password : str, password_conf : str, role_id : int):
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
        
        self.role_id = role_id
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