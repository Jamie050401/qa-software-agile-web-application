#!/bin/python3

#################################################################################################
# Program:  Python / SQLite Web Application                                                     #
# Filename: models.py                                                                           #
# Author:   Jamie Allen                                                                         #
# Course:   BSc Digital Technology and Solutions                                                #
# Module:   Software Engineering and Agile                                                      #
# Version:  1.0                                                                                 #
#################################################################################################

from flask import flash
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base
from werkzeug.security import generate_password_hash

database_declarative_base = declarative_base()

roles = ["User", "Admin"]

# class Ticket(database_declarative_base):
#    __tablename__ = "ticket"


class User(database_declarative_base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    role_name = Column(String(5), nullable=False)
    email = Column(String(60), unique=True, nullable=False)
    first_name = Column(String(60), nullable=False)
    password = Column(String(255), nullable=False)
    profile_image = Column(String(255), nullable=True)
    is_valid = True

    def __init__(self, email, first_name, password, password_conf, role_name):
        def validate_user(email: str, first_name, password, password_conf, role_name):
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
            elif not email.__contains__("@"):
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

        is_valid = validate_user(
            email, first_name, password, password_conf, role_name)

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
