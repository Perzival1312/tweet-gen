# FROM python:2.7
# ADD . /todo
# WORKDIR /todo
# RUN pip install -r requirements.txt
FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/