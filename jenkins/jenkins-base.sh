#!/bin/bash

echo "Build Information:"
echo "Build ID: ${BUILD_ID}"
echo "Build URL: ${BUILD_URL}"

echo "Pruning docker ..."
docker -H $DOCKER_HOST image prune -f
docker -H $DOCKER_HOST container prune -f