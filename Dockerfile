# syntax=docker/dockerfile:1
FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /attendance
COPY requirements.txt /attendance/
RUN pip install -r requirements.txt
COPY . /attendance/