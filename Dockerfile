# syntax=docker/dockerfile:1
FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /sams
COPY requirements.txt /sams/
RUN pip install -r requirements.txt
COPY . /sams/