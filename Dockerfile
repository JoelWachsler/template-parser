FROM python:3.9-buster

WORKDIR /root
ENV PIPENV_PIPFILE /root/Pipfile

COPY Pipfile .
RUN pip install pipenv
RUN pipenv install

COPY main.py .
