#!/bin/python3

#################################################################################################
# Program:  Python / SQLite Web Application                                                     #
# Filename: __init__.py                                                                         #
# Author:   Jamie Allen                                                                         #
# Course:   BSc Digital Technology and Solutions                                                #
# Module:   Software Engineering and Agile                                                      #
# Version:  1.0                                                                                 #
# Date:     xx/xx/23                                                                            #
#################################################################################################

from os import path
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker, declarative_base
from werkzeug.security import generate_password_hash

DB_NAME = "db/database.db"
SQLALCHEMY_DATABASE_URL = f"sqlite:///{DB_NAME}"

db_base = declarative_base()
db_engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args = {"check_same_thread": False})
session_local = sessionmaker(autocommit = False, autoflush = False, bind = db_engine)

def get_queries():
    with open("db/sql/models/db_setup.sql") as file:
        file_queries = file.read().replace("\n", " ")
    queries = file_queries.split("||")
    return queries

def create_database():
    from web import models
    db = session_local()
    
    if not path.exists(DB_NAME):
        models.db_base.metadata.create_all(bind = db_engine)
        queries = get_queries()
        for query in queries:
            modified_query = query.replace("replace_password", generate_password_hash("password", "sha256"))
            db.execute(text(modified_query))
        db.commit()
    
    db.close()

#################################################################################################
# File: __init__.py                                                                             #
#                                                                                               #
# Disclaimer: The following source code is the sole work of the author unless otherwise stated. #
#                                                                                               #
# Copyright (c) Jamie Allen. All Rights Reserved.                                               #
#################################################################################################