#!/bin/python3

#################################################################################################
# Program:  Python / SQLite Web Application                                                     #
# Filename: views.py                                                                            #
# Author:   Jamie Allen                                                                         #
# Course:   BSc Digital Technology and Solutions                                                #
# Module:   Software Engineering and Agile                                                      #
# Version:  1.0                                                                                 #
#################################################################################################

#################################################################################################
# File: views.py                                                                                #
#                                                                                               #
# Disclaimer: The following source code is the sole work of the author unless otherwise stated. #
#                                                                                               #
# Copyright (c) Jamie Allen. All Rights Reserved.                                               #
#################################################################################################

from flask import Blueprint, render_template, request, flash, redirect, url_for

from web.functions import redirects, get_user_profile_image, convert_ticket_created_datetime, get_user, get_users
from web.authentication.auth import current_user as AuthUser
from db import session_local
from db.models.users import User
from db.models.tickets import Ticket

views = Blueprint('views', __name__)
current_user = AuthUser.get_user()

@views.route('/', methods=["GET"])
def index():
    if current_user.is_authenticated:
        return render_template("index.html", user=current_user)

    return redirects(display_login=False)

@views.route('/tickets', methods=["GET"])
def tickets():
    if current_user.is_authenticated:
        database = session_local()
        tickets_in_db = database.query(Ticket).all()
        database.close()
        return render_template("tickets.html", user=current_user, create=False, view=False, edit=False, tickets=tickets_in_db, get_user_profile_image=get_user_profile_image, convert_ticket_created_datetime=convert_ticket_created_datetime, edit_ticket=edit_ticket)
    return redirects(display_login=True)

@views.route('/tickets/create', methods=["GET", "POST"])
def create_ticket():
    if current_user.is_authenticated:
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
                    return redirect(url_for("views.tickets"))
            else:
                flash("Failed to create ticket! Specified user does not exist.", category="failure")
            database.close()
        return render_template("tickets.html", user=current_user, create=True, view=False, edit=False)
    return redirects(display_login=True)

@views.route('/tickets/view', methods=["GET"])
def view_ticket():
    if current_user.is_authenticated:
        # Getting the ticket ID as an argument from the URL
        ticket_id = request.args.get('ticket_id', None)
        if ticket_id is None:
            flash("Ticket not found!", category="failure")
            return redirect(url_for("views.tickets"))

        # Fetching the ticket from the database
        database = session_local()
        ticket = database.query(Ticket).filter(Ticket.id == ticket_id).first()
        database.close()
        if ticket is None:
            flash("Ticket not found!", category="failure")
            return redirect(url_for("views.tickets"))

        return render_template("tickets.html", user=current_user, create=False, view=True, edit=False, ticket=ticket, get_user=get_user)
    return redirects(display_login=True)

@views.route('/tickets/edit', methods=["GET", "POST"])
def edit_ticket():
    if current_user.is_authenticated:
        # Getting the ticket ID as an argument from the URL
        ticket_id = request.args.get('ticket_id', None)
        if ticket_id is None:
            flash("Ticket not found!", category="failure")
            return redirect(url_for("views.tickets"))

        # Fetching the ticket from the database
        database = session_local()
        ticket = database.query(Ticket).filter(Ticket.id == ticket_id).first()
        database.close()
        if ticket is None:
            flash("Ticket not found!", category="failure")
            return redirect(url_for("views.tickets"))

        # Displaying the edit screen to the user
        if request.method == "GET":
            return render_template("tickets.html", user=current_user, create=False, view=False, edit=True, ticket=ticket, get_users=get_users)
        # Updating the ticket in the database
        else:
            database = session_local()

            assignee = request.form.get("assignee")
            team = request.form.get("team")
            issue_type = request.form.get("type_of_issue")
            issue_desc = request.form.get("issue_desc")
            database.delete(ticket)

            ticket.assignee_id = assignee
            ticket.team = team
            ticket.issue_type = issue_type
            ticket.issue_desc = issue_desc
            database.add(ticket)

            database.commit()
            flash("Ticket updated!", category="success")
            database.close()

            return redirect(url_for("views.tickets"))
    return redirects(display_login=True)

@views.route('/tickets/delete', methods=["GET"])
def delete_ticket():
    if current_user.is_authenticated:
        if current_user.role_name == "Admin":
            # Getting the ticket ID as an argument from the URL
            ticket_id = request.args.get('ticket_id', None)
            if ticket_id is None:
                flash("Ticket not found!", category="failure")
                return redirect(url_for("views.tickets"))

            # Fetching the ticket from the database
            database = session_local()
            ticket = database.query(Ticket).filter(Ticket.id == ticket_id).first()
            database.close()
            if ticket is None:
                flash("Ticket not found!", category="failure")
                return redirect(url_for("views.tickets"))

            database = session_local()
            database.delete(ticket)
            database.commit()
            flash("Ticket deleted!", category="success")
            database.close()
            return redirect(url_for("views.tickets"))
        flash("Only 'Admin' users can delete tickets!", category="failure")
        return redirect(url_for("views.tickets"))
    return redirects(display_login=True)
