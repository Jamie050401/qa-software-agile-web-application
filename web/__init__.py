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

from os import path, urandom
from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DB_NAME = "sql/database.db"
SQLALCHEMY_DATABASE_URL = f"sqlite:///{DB_NAME}"

db_base = declarative_base()
db_engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args = {"check_same_thread": False})
session_local = sessionmaker(autocommit = False, autoflush = False, bind = db_engine)

def create_database():
    from . import models
    db = session_local()
    
    if not path.exists(DB_NAME):
        models.db_base.metadata.create_all(bind = db_engine)
        # TODO - Populate database ...
    
    db.close()

def create_application():
    application = Flask(__name__)
    application.config['SECRET_KEY'] = urandom(12)
    
    from .views import views
    from .auth import auth
    
    application.register_blueprint(views, url_prefix='/')
    application.register_blueprint(auth, url_prefix='/')
    
    from .models import User
    
    create_database()
    
    # TODO - Implement new login manager
    #login_manager = LoginManager()
    #login_manager.login_view = "auth.login"
    #login_manager.init_app(application)
    
    #@login_manager.user_loader
    #def load_user(id):
    #    return User.query.get(int(id))
    
    return application

def run_application(application : Flask, ip_address, is_debug : bool):
    application.run(host = ip_address, port = 80, debug = is_debug)

#################################################################################################
# File: __init__.py                                                                             #
#                                                                                               #
# Disclaimer: The following source code is the sole work of the author unless otherwise stated. #
#                                                                                               #
# Copyright (c) Jamie Allen. All Rights Reserved.                                               #
#################################################################################################