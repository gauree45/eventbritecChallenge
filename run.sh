#!/usr/bin/sh
docker build -t gauree45/eventbrite:v1 .
docker run -it -p 8000:8000 gauree45/eventbrite:v1