#!/bin/bash

echo "Logging into Docker Hub ..."
docker -H $DOCKER_HOST login -u $DOCKER_USERNAME -p $DOCKER_PASSWORD

echo "Building docker image ..."
docker -H $DOCKER_HOST build -t jamie050401/qa-web-application:"$DOCKER_VERSION_TAG" ./

echo "Pushing docker image ..."
docker -H $DOCKER_HOST push jamie050401/qa-web-application:"$DOCKER_VERSION_TAG"

echo "Pruning docker ..."
docker -H $DOCKER_HOST image prune -f
docker -H $DOCKER_HOST container prune -f