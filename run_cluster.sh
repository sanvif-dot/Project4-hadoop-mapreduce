#!/bin/bash

# create new network
docker network create hadoop_network

# build docker image with image name hadoop-base:3.3.1. find dockerfile file
docker build -t hadoop-base:3.3.1 .
# running image to container, -d to run it in daemon mode, find docker compose file
docker-compose up -d
