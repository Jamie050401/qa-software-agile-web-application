# docker build -t qa_web_application ./
FROM alpine:latest

ENV IP_ADDRESS=0.0.0.0 \
    PORT=8000 \
    IS_DEBUG=FALSE \
    WORKER_THREADS=1

CMD ["gunicorn", "-w", "${WORKER_THREADS}", "-b", "${IP_ADDRESS}:${PORT}", "main:application"]

EXPOSE ${PORT}