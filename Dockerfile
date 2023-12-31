FROM python:3.9-alpine3.16

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir -p /home/app


RUN addgroup -S app && adduser -S app -G app

ENV HOME=/home/app
ENV APP_HOME=/home/app/web
RUN mkdir $APP_HOME
RUN mkdir $APP_HOME/staticfiles
RUN mkdir $APP_HOME/media
WORKDIR $APP_HOME

RUN apk update && apk add libpq
COPY requirements.txt /temp/requirements.txt
RUN apk add postgresql-client build-base postgresql-dev
RUN pip install -r /temp/requirements.txt

COPY /project $APP_HOME

RUN chown -R app:app $APP_HOME
USER app


