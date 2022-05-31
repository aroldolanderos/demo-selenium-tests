#!/usr/bin/env bash

docker-compose up --build -d
echo "Please wait 60 seg while service running..." && \
echo "You can open http://localhost:4444" && \
#sleep 60 && \
#docker-compose down