#!/bin/python3

#################################################################################################
# Program:  Python / SQLite Web Application                                                     #
# Filename: views.py                                                                            #
# Author:   Jamie Allen                                                                         #
# Course:   BSc Digital Technology and Solutions                                                #
# Module:   Software Engineering and Agile                                                      #
# Version:  1.0                                                                                 #
#################################################################################################

from flask import Blueprint, render_template, request, flash, redirect, url_for

from web.authentication.auth import current_user as AuthUser
from db import session_local
from db.models.users import User
from db.models.tickets import Ticket

views = Blueprint('views', __name__)
current_user = AuthUser.get_user()

def redirects(display_login: bool):
    if display_login:
        return redirect(url_for("auth.login"))

    return redirect(url_for("auth.register"))

def display(screen: str, display_login: bool):
    if current_user.is_authenticated:
        return render_template(screen, user=current_user)

    return redirects(display_login)

@views.route('/')
def index():
    return display("index.html", display_login=False)

@views.route('/tickets')
def tickets():
    return display("tickets.html", display_login=True)

@views.route('/tickets/create', methods=["GET", "POST"])
def create_ticket():
    if request.method == "POST":
        database = session_local()

        email = request.form.get("email")
        if email == "":
            email = current_user.email
        team = request.form.get("team")
        issue_type = request.form.get("typeOfIssue")
        issue_desc = request.form.get("issueDescription")

        ticket_user = database.query(User).filter(User.email == email).first()
        if ticket_user:
            user_id = ticket_user.id
            new_ticket = Ticket(user_id, team, issue_type, issue_desc)
            if new_ticket.is_valid:
                database.add(new_ticket)
                database.commit()
                flash("Ticket created!", category="success")
                database.close()
                return render_template("tickets.html", user=current_user)
        else:
            flash("Failed to create ticket! Specified user does not exist.", category="failure")
        database.close()

    if current_user.is_authenticated:
        return render_template("tickets.html", user=current_user, create=True)
    return redirects(display_login=True)

@views.route('/users')
def users():
    return display("users.html", display_login=True)

@views.route('/users/create')
def create_user():
    if current_user.is_authenticated:
        return render_template("users.html", user=current_user, create=True)

    return redirects(display_login=True)

@views.route('/profile')
def profile():
    return display("profile.html", display_login=True)

@views.route('/settings')
def settings():
    return display("settings.html", display_login=True)

#################################################################################################
# File: views.py                                                                                #
#                                                                                               #
# Disclaimer: The following source code is the sole work of the author unless otherwise stated. #
#                                                                                               #
# Copyright (c) Jamie Allen. All Rights Reserved.                                               #
#################################################################################################
