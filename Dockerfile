# docker build -t qa_web_application ./
FROM alpine:latest

# Copies application source code into the container's file system
COPY . /app

# Sets the application source code as the working directory for the rest of this file
WORKDIR /app

# Fetching generic alpine packages
RUN apk add --update --no-cache \
    bash

# Setting up Python
RUN apk add --update --no-cache python3 && ln -sf python3 /usr/bin/python && \
    python3 -m ensurepip && \
    pip3 install --no-cache --upgrade \
        pip \
        setuptools

# Setting up packages required for Python Web Application
RUN pip3 install --no-cache \
    Flask==2.2.2 \
    SQLAlchemy==2.0.0 \
    pytest==7.2.1 \
    gunicorn==20.1.0

# Declaring environment variables for the container
ENV IP_ADDRESS=0.0.0.0 \
    PORT=8000 \
    IS_DEBUG=FALSE \
    WORKER_THREADS=1

EXPOSE ${PORT}

CMD run.sh
#CMD ["gunicorn", "-w", ${WORKER_THREADS}, "-b", "${IP_ADDRESS}:${PORT}", "main:app"]

