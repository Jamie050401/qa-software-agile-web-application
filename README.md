# QA Web Application

## Summary of the Application

This is a Python web application developed using Flask.

The application exists to log and track tickets. New users are able to register to gain access to the application whilst Admin users need to be manually created/updated within the SQLite database. All users can then create and edit tickets - designed to report and track issues as support tickets that one might find within an organisation. Only Admin users possess the ability to delete tickets (the option to do so is completely hidden from standard users).

The application leverages bootstrap to provide built in Javascript and CSS to enhance the aesthetic and functionality of the front-end, allowing development activities to be focussed moreso on the back-end. Thanks to bootstrap - there are many notifications - or 'flashes' - that notify the user based on their actions i.e. 'ticket created successfully' or 'ticket not found'. Additionally, attempting to delete a ticket will provide a confirmation prompt to prevent accidental deletions.

The back-end logic includes validation and restrictions to ensure that unauthenticated users cannot access parts of the web application by targetting specific URLs or attempting to pass in rogue data as part of a URL. Equally, it ensures standard users cannot perform actions otherwise blocked to them. Additionally, user passwords are hashed using the functionality present in Werkzeug - which is required by Flask. However, there isn't any salting functionality currently - this would be a much needed improvement were the application to be used in a true production environment.

## Dependencies

### Environment Requirements

1. Python 3.11.0

### Python Packages

1. pip 23.0
2. setuptools 67.0.0
3. Werkzeug 2.2.2
4. Flask 2.2.2
5. Gunicorn 20.1.0
6. SQLAlchemy 2.0.0
7. iniconfig 2.0.0
8. pytest 7.2.1

## To Install/Run

### Option A

1. Install Python 3.11.0 into your environment (ensure that pip is also installed at this point).
2. Execute the 'install.py' script to have the required packages automatically installed inside your environment.
3. Run the application using main.py OR deploy it using the provided Dockerfile and docker-compose.yml.

### Option B

1. Install Python 3.11.0 into your environment.
2. Manually install the packages listed under Dependencies.
3. Run the application using main.py OR deploy it using the provided Dockerfile and docker-compose.yml.
