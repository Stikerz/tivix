FROM python:3

ENV PYTHONUNBUFFERED 1

COPY . /tivix

WORKDIR /tivix

RUN pip install  -r requirements.txt

WORKDIR /tivix/tivix
