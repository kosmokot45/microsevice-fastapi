FROM python:3.11

RUN python -m pip install fastapi httpx scrapy gunicorn uvicorn uvloop httptools

WORKDIR /app

ADD simple-microservice.py simple-microservice.py