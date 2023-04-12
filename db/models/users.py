#!/bin/python3

#################################################################################################
# Program:  Python / SQLite Web Application                                                     #
# Filename: users.py                                                                            #
# Author:   Jamie Allen                                                                         #
# Course:   BSc Digital Technology and Solutions                                                #
# Module:   Software Engineering and Agile                                                      #
# Version:  1.0                                                                                 #
#################################################################################################

#################################################################################################
# File: users.py                                                                                #
#                                                                                               #
# Disclaimer: The following source code is the sole work of the author unless otherwise stated. #
#                                                                                               #
# Copyright (c) Jamie Allen. All Rights Reserved.                                               #
#################################################################################################

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base
from werkzeug.security import generate_password_hash

from db.validation import validate_user

database_declarative_base = declarative_base()

class User(database_declarative_base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    role_name = Column(String(5), nullable=False)
    email = Column(String(60), unique=True, nullable=False)
    first_name = Column(String(60), nullable=False)
    password = Column(String(255), nullable=False)
    profile_image = Column(String(255), nullable=True)
    is_valid = True

    def __init__(self, email, first_name, password, password_conf, role_name):
        is_valid = validate_user(email, first_name, password, password_conf, role_name)

        self.role_name = role_name
        self.email = email
        self.first_name = first_name
        self.password = generate_password_hash(password, "sha256")
        self.is_valid = is_valid
