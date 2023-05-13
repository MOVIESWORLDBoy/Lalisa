FROM python:3.8-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt
RUN apt update && apt upgrade -y
RUN pip3 install -U pip
RUN pip3 install --upgrade pip
RUN pip3 install -U -r requirements.
COPY . .
CMD python3 bot.py
