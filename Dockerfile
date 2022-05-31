FROM python:3.8.6-buster

WORKDIR /usr/src/app

COPY . /usr/src/app

RUN chmod 775 bootstrap.sh