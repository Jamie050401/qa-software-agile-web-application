#!/bin/bash

export DOCKER_HOST_NONPROD="tcp://10.0.0.10:2375"

echo "Executing docker-compose file ..."
docker -H $DOCKER_HOST_NONPROD compose up -d