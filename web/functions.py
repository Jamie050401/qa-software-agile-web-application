#!/bin/python3

#################################################################################################
# Program:  Python / SQLite Web Application                                                     #
# Filename: functions.py                                                                        #
# Author:   Jamie Allen                                                                         #
# Course:   BSc Digital Technology and Solutions                                                #
# Module:   Software Engineering and Agile                                                      #
# Version:  1.0                                                                                 #
#################################################################################################

from datetime import datetime
from math import trunc
from flask import redirect, url_for

from web.authentication.auth import current_user as AuthUser
from db import session_local
from db.models.users import User

current_user = AuthUser.get_user()

def redirects(display_login: bool):
    if display_login:
        return redirect(url_for("auth.login"))

    return redirect(url_for("auth.register"))

def get_user_profile_image(user_id):
    database = session_local()
    profile_image = database.query(User).filter(User.id == user_id).first().profile_image
    database.close()
    return profile_image

def get_difference_between_dates(earlier_date, later_date):
    diff = (later_date - earlier_date).seconds

    if diff < 60:
        return f"{trunc(diff)}s"
    elif diff < 3600:
        return f"{trunc(diff / 60)}m"
    elif diff < 86400:
        return f"{trunc(diff / 3600)}h"
    elif diff < 604800:
        return f"{trunc(diff / 86400)}d"
    elif diff < 2419200:
        return f"{trunc(diff / 604800)}w"
    else:
        return ">1M"

def convert_ticket_created_datetime(creation_date):
    diff = get_difference_between_dates(creation_date, datetime.now())
    return diff

def get_user(user_id):
    database = session_local()
    user = database.query(User).filter(User.id == user_id).first()
    database.close()
    return user

def get_users():
    database = session_local()
    users = database.query(User).all()
    database.close()
    return users

#################################################################################################
# File: functions.py                                                                            #
#                                                                                               #
# Disclaimer: The following source code is the sole work of the author unless otherwise stated. #
#                                                                                               #
# Copyright (c) Jamie Allen. All Rights Reserved.                                               #
#################################################################################################
