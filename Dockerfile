FROM python:3.8-slim
ENV PYTHONUNBUFFERED 1
RUN apt-get update && apt-get -y install gcc
RUN /usr/local/bin/python -m pip install --upgrade pip
COPY ./requirements.in /requirements.in
RUN pip install -r /requirements.in
RUN mkdir -p /app
COPY . /app
WORKDIR /app