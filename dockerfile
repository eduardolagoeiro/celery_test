FROM python:3.6-alpine

ENV PYTHONUNBUFFERED 1

WORKDIR /srv/app

COPY requirements.txt src /srv/app/

RUN apk update && \
   apk upgrade && \
   apk add --update --no-cache \
   openssh-client \
   build-base \
   bash \
   python3-dev \
   curl-dev \
   py-pip \
   gfortran \
   lapack-dev \
   libxml2-dev \
   libxslt-dev \
   libffi-dev && \
   rm /var/cache/apk/*

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD python3 celery_example.py