FROM python:3.8.10-alpine

RUN mkdir /usr/src/app

WORKDIR /usr/src/app

COPY ./requirements.txt .

RUN pip install -r requirements.txt

COPY . .