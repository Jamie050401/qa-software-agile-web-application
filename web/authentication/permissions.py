#!/bin/python3

#################################################################################################
# Program:  Python / SQLite Web Application                                                     #
# Filename: permissions.py                                                                      #
# Author:   Jamie Allen                                                                         #
# Course:   BSc Digital Technology and Solutions                                                #
# Module:   Software Engineering and Agile                                                      #
# Version:  1.0                                                                                 #
#################################################################################################

from db.models import roles
from web.authentication.auth import current_user

permissions = ["create", "read", "update", "delete"]


def is_authorised(permission):
    if permission not in permissions:
        return False

    # TODO - Implement user based access
    match permission:
        case "create":
            has_role_based_access = current_user.role_name in roles
            return has_role_based_access
        case "read":
            has_role_based_access = current_user.role_name in roles
            return has_role_based_access
        case "update":
            has_role_based_access = current_user.role_name in roles
            return has_role_based_access
        case "delete":
            has_role_based_access = current_user.role_name in ["Admin"]
            return has_role_based_access

#################################################################################################
# File: permissions.py                                                                          #
#                                                                                               #
# Disclaimer: The following source code is the sole work of the author unless otherwise stated. #
#                                                                                               #
# Copyright (c) Jamie Allen. All Rights Reserved.                                               #
#################################################################################################
