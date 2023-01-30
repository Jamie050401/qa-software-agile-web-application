#!/bin/python3

#################################################################################################
# Program:  Python / SQLite Web Application                                                     #
# Filename: auth.py                                                                             #
# Author:   Jamie Allen                                                                         #
# Course:   BSc Digital Technology and Solutions                                                #
# Module:   Software Engineering and Agile                                                      #
# Version:  1.0                                                                                 #
# Date:     xx/xx/23                                                                            #
#################################################################################################

from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_user, login_required, logout_user, current_user
from werkzeug.security import check_password_hash # NOTE - This comes from flask_login

from . import db
from .models import User

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        
        user = User.query.filter_by(email = email).first()
        if user:
            if check_password_hash(user.password, password):
                flash("Logged in successfully!", category = "success")
                login_user(user, remember = True) # TODO - Replace boolean with check box on screen to remember user
                return redirect(url_for("views.index"))
            else:
                flash("Incorrect email or password, please try again.", category = "failure")
        else:
            flash("Incorrect email or password, please try again.", category = "failure")
            
    return render_template("login.html", user = current_user)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for("auth.login"))

@auth.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "POST":
        email = request.form.get("email")
        first_name = request.form.get("first_name")
        password = request.form.get("password_first")
        password_conf = request.form.get("password_second")
        
        user = User.query.filter_by(email = email).first()
        if user:
            flash("Email already exists!", category = "failure")
            return redirect(url_for("auth.register"))
        
        new_user = User(email = email, first_name = first_name, password = password, password_conf = password_conf)
        if new_user.is_valid:
            db.session.add(new_user)
            db.session.commit()
            flash("User created!", category="success")
            login_user(user, remember = True) # TODO - Replace boolean with check box on screen to remember user
            return redirect(url_for("views.index"))
        
    return render_template("register.html", user = current_user)

#################################################################################################
# File: auth.py                                                                                 #
#                                                                                               #
# Disclaimer: The following source code is the sole work of the author unless otherwise stated. #
#                                                                                               #
# Copyright (c) Jamie Allen. All Rights Reserved.                                               #
#################################################################################################