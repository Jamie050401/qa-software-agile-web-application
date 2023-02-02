#!/bin/python3

#################################################################################################
# Program:  Python / SQLite Web Application                                                     #
# Filename: views.py                                                                            #
# Author:   Jamie Allen                                                                         #
# Course:   BSc Digital Technology and Solutions                                                #
# Module:   Software Engineering and Agile                                                      #
# Version:  1.0                                                                                 #
# Date:     xx/xx/23                                                                            #
#################################################################################################

from flask import Blueprint, render_template, redirect, url_for

from web.authentication import current_user

views = Blueprint('views', __name__)


def redirects():
    if current_user.is_existing_user:
        return redirect(url_for("auth.login"))

    return redirect(url_for("auth.register"))


def display(screen):
    if current_user.is_authenticated:
        return render_template(screen, user=current_user)

    return redirects()


@views.route('/')
def index():
    return display("index.html")


@views.route('/tickets')
def ticket():
    return display("tickets.html")


@views.route('/tickets/create')
def create_ticket():
    if current_user.is_authenticated:
        return render_template("tickets.html", user=current_user, create=True)

    return redirects()


@views.route('/users')
def user():
    return display("users.html")


@views.route('/users/create')
def create_user():
    if current_user.is_authenticated:
        return render_template("users.html", user=current_user, create=True)

    return redirects()


@views.route('/profile')
def profile():
    return display("profile.html")


@views.route('/settings')
def settings():
    return display("settings.html")

#################################################################################################
# File: views.py                                                                                #
#                                                                                               #
# Disclaimer: The following source code is the sole work of the author unless otherwise stated. #
#                                                                                               #
# Copyright (c) Jamie Allen. All Rights Reserved.                                               #
#################################################################################################
