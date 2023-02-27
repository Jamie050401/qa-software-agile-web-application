#!/bin/python3

#################################################################################################
# Program:  Python / SQLite Web Application                                                     #
# Filename: __init__.py                                                                         #
# Author:   Jamie Allen                                                                         #
# Course:   BSc Digital Technology and Solutions                                                #
# Module:   Software Engineering and Agile                                                      #
# Version:  1.0                                                                                 #
#################################################################################################

from os import path
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from werkzeug.security import generate_password_hash

from db.models import users

DB_NAME = "./data/database.db"
SQLALCHEMY_DATABASE_URL = f"sqlite:///{DB_NAME}"

database_engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={
                                "check_same_thread": False})

session_local = sessionmaker(
    autocommit=False, autoflush=False, bind=database_engine)


def get_queries():
    with open("db/sql/models/db_setup.sql", encoding="utf-8") as file:
        file_queries = file.read().replace("\n", " ")
    queries = file_queries.split("||")

    return queries


def create_database():
    if path.exists(DB_NAME):
        return None

    database = session_local()

    # Creates the tables within the database
    users.database_declarative_base.metadata.create_all(
        bind=database_engine)

    # Populates the database tables with initial data
    queries = get_queries()
    for query in queries:
        modified_query = query.replace(
            "replace_password", generate_password_hash("password", "sha256"))
        database.execute(text(modified_query))
    database.commit()

    database.close()

    return None

#################################################################################################
# File: __init__.py                                                                             #
#                                                                                               #
# Disclaimer: The following source code is the sole work of the author unless otherwise stated. #
#                                                                                               #
# Copyright (c) Jamie Allen. All Rights Reserved.                                               #
#################################################################################################
