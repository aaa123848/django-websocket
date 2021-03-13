FROM  python:3.9.1-alpine

WORKDIR ./srv/django-ws
RUN   apk add gcc musl-dev libffi-dev libressl-dev cargo openssl-dev libxslt-dev libxml2 libxml2-dev linux-headers

# copy requirements
COPY . .
RUN pip install --no-cache-dir -U pip setuptools
RUN pip install -r requirements.txt



 