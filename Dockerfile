FROM alpine:latest

ARG ip_address
ARG port
ARG is_debug
ARG worker_threads

ENV IP_ADDRESS $ip_address \
    PORT $port \
    IS_DEBUG $is_debug \
    WORKER_THREADS $worker_threads

# Need to test manually executing the command before uncommenting the below:
#CMD ["gunicorn", "-w", "${WORKER_THREADS}", "-b", "${IP_ADDRESS}:${PORT}", "main:application"]

EXPOSE ${PORT}