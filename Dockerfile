FROM python:3.9-buster

WORKDIR /root

COPY Pipfile .
RUN pip install pipenv
RUN pipenv install

COPY main.py .
