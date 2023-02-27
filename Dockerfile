# Command to execute Dockerfile (when inside root directory): docker build -t qa-web-application ./
FROM alpine:latest

# Declaring environment variables for the container
ENV IP_ADDRESS=0.0.0.0 \
    PORT=80 \
    IS_DEBUG=FALSE \
    WORKERS=1 \
    WORKER_THREADS=1 \
    USER=root \
    PUID=1000 \
    PGID=1000 \
    TZ=Europe/London

# TODO - Need to test this ...
# Setting up the desired user (defaults to root)
RUN groupadd -g $PGID -o $USER && \
    useradd -m -u $PUID -g $PGID -o -s /bin/bash $USER

USER $USER

# Copies application source code into the container's file system
COPY . /app

# Declares the /data folder as a volume mount point
VOLUME /app/data

# Sets the application source code as the working directory for the rest of this file
WORKDIR /app

# Fetching generic alpine packages
RUN apk add --update --no-cache bash && \
    apk add --no-cache \
        nano

# Setting up Python
RUN apk add --no-cache python3 && ln -sf python3 /usr/bin/python && \
    python3 -m ensurepip && \
    pip3 install --no-cache --upgrade \
        pip \
        setuptools

# Setting up packages required for Python Web Application
RUN pip3 install --no-cache \
        iniconfig==2.0.0 \
        Jinja2==3.1.2 \
        Werkzeug==2.2.2 \
        Flask==2.2.2 \
        SQLAlchemy==2.0.0 \
        pytest==7.2.1 \
        greenlet==2.0.2 \
        gunicorn==20.1.0

EXPOSE ${PORT}

CMD /usr/bin/gunicorn -b "${IP_ADDRESS}:${PORT}" --workers=${WORKERS} --threads=${WORKER_THREADS} "main:app"
