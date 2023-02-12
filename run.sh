#!/bin/bash

gunicorn -w "$WORKER_THREADS" -b "$IP_ADDRESS:$PORT", "main:app"