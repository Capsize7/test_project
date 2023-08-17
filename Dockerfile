FROM python:3.9-alpine3.16

WORKDIR /project

COPY requirements.txt /temp/requirements.txt

RUN apk add postgresql-client build-base postgresql-dev
RUN pip install -r /temp/requirements.txt
RUN adduser --disabled-password project_user



EXPOSE 8000

USER project_user

COPY project /project