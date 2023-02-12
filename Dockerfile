# docker build -t qa_web_application ./
FROM alpine:latest

RUN apk add --update --no-cache python3 && ln -sf python3 /usr/bin/python && \
    python3 -m ensurepip && \
    pip3 install --no-cache --upgrade \
        pip \
        setuptools

RUN pip3 install --no-cache \
    Flask==2.2.2 \
    SQLAlchemy==2.0.0 \
    pytest==7.2.1 \
    gunicorn==20.1.0

ENV IP_ADDRESS=0.0.0.0 \
    PORT=8000 \
    IS_DEBUG=FALSE \
    WORKER_THREADS=1

CMD ["gunicorn", "-w", "${WORKER_THREADS}", "-b", "${IP_ADDRESS}:${PORT}", "main:application"]

EXPOSE ${PORT}