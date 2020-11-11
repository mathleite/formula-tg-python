FROM python:latest

RUN apt-get update

COPY requirements.txt .

RUN pip install -r requirements.txt