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
from werkzeug.security import check_password_hash

from db import session_local
from .models import User

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        db = session_local()
        
        email = request.form.get("email")
        password = request.form.get("password")
        
        user = db.query(User).filter(User.email == email).first()
        if user:
            if check_password_hash(user.password, password):
                flash("Logged in successfully!", category = "success")
                # TODO - Login user here ...
                db.close()
                return redirect(url_for("views.index"))
            else:
                flash("Incorrect email or password, please try again.", category = "failure")
        else:
            flash("Incorrect email or password, please try again.", category = "failure")
        
        db.close()
            
    return render_template("login.html")

@auth.route('/logout')
def logout():
    # TODO - Logout user here ...
    return redirect(url_for("auth.login"))

@auth.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "POST":
        db = session_local()
        
        email = request.form.get("email")
        first_name = request.form.get("first_name")
        password = request.form.get("password_first")
        password_conf = request.form.get("password_second")
        
        user = db.query(User).filter(User.email == email).first()
        if user:
            flash("Email already exists!", category = "failure")
            db.close()
            return redirect(url_for("auth.register"))
        
        # Here 'role_id = 1' represents the 'User' role
        new_user = User(email = email, first_name = first_name, password = password, password_conf = password_conf, role_id = 1)
        if new_user.is_valid:
            db.add(new_user)
            db.commit()
            flash("User created!", category="success")
            # TODO - Login user here ...
            db.close()
            return redirect(url_for("views.index"))
        
        db.close()
        
    return render_template("register.html")

#################################################################################################
# File: auth.py                                                                                 #
#                                                                                               #
# Disclaimer: The following source code is the sole work of the author unless otherwise stated. #
#                                                                                               #
# Copyright (c) Jamie Allen. All Rights Reserved.                                               #
#################################################################################################