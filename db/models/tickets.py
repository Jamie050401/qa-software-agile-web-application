#!/bin/python3

#################################################################################################
# Program:  Python / SQLite Web Application                                                     #
# Filename: tickets.py                                                                          #
# Author:   Jamie Allen                                                                         #
# Course:   BSc Digital Technology and Solutions                                                #
# Module:   Software Engineering and Agile                                                      #
# Version:  1.0                                                                                 #
#################################################################################################

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base

from db.validation import validate_ticket
from db.models.users import User

database_declarative_base = declarative_base()

class Ticket(database_declarative_base):
    __tablename__ = "tickets"

    # NOTE: Display id (primary_key) as SPRT-nnnn where nnnn = id
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey(User.id), nullable=False)
    team = Column(String(60), nullable=False)
    issue_type = Column(String(60), nullable=False)
    issue_desc = Column(String(255), nullable=False)
    is_valid = True

    def __init__(self, user_id : int, team : str, issue_type : str, issue_desc : str):
        is_valid = validate_ticket(team, issue_type, issue_desc)

        self.user_id = user_id
        self.team = team
        self.issue_type = issue_type
        self.issue_desc = issue_desc
        self.is_valid = is_valid

#################################################################################################
# File: users.py                                                                                #
#                                                                                               #
# Disclaimer: The following source code is the sole work of the author unless otherwise stated. #
#                                                                                               #
# Copyright (c) Jamie Allen. All Rights Reserved.                                               #
#################################################################################################
