FROM python:3.8-alpine

RUN mkdir /server

WORKDIR /server

COPY requirements.txt /server

RUN \
 apk add --no-cache python3 postgresql-libs && \
 apk add --no-cache --virtual .build-deps gcc python3-dev musl-dev postgresql-dev && \
 python3 -m pip install -r requirements.txt --no-cache-dir && \
 apk --purge del .build-deps

COPY . /server

ENV PYTHONPATH=/server

RUN mkdir /server/data

RUN mkdir /server/logs

WORKDIR /server/src/api

CMD ["python3", "app.py"]
