#!/bin/python3

#################################################################################################
# Program:  Python / SQLite Web Application                                                     #
# Filename: tickets.py                                                                          #
# Author:   Jamie Allen                                                                         #
# Course:   BSc Digital Technology and Solutions                                                #
# Module:   Software Engineering and Agile                                                      #
# Version:  1.0                                                                                 #
#################################################################################################

from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import declarative_base

from db.validation import validate_ticket
from db.models.users import User

database_declarative_base = declarative_base()

class Ticket(database_declarative_base):
    __tablename__ = "tickets"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey(User.id), nullable=False)
    team = Column(String(60), nullable=False)
    issue_type = Column(String(60), nullable=False)
    issue_desc = Column(String(255), nullable=False)
    time_created = Column(DateTime(timezone=True))
    time_updated = Column(DateTime(timezone=True))
    is_valid = True

    def __init__(self, user_id : int, team : str, issue_type : str, issue_desc : str):
        is_valid = validate_ticket(team, issue_type, issue_desc)

        self.user_id = user_id
        self.team = team
        self.issue_type = issue_type
        self.issue_desc = issue_desc
        self.time_created = datetime.now()
        self.time_updated = datetime.now()
        self.is_valid = is_valid

    def get_id(self):
        if self.id < 10:
            return f"SPRT-000{self.id}"
        elif self.id < 100:
            return f"SPRT-00{self.id}"
        elif self.id < 1000:
            return f"SPRT-0{self.id}"
        else:
            return f"SPRT-{self.id}"

#################################################################################################
# File: users.py                                                                                #
#                                                                                               #
# Disclaimer: The following source code is the sole work of the author unless otherwise stated. #
#                                                                                               #
# Copyright (c) Jamie Allen. All Rights Reserved.                                               #
#################################################################################################
