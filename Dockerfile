FROM python:3.9-alpine

LABEL org.opencontainers.image.source=https://github.com/paulkiernan/taqueria-bonjour

RUN apk --no-cache add sqlite

COPY requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt

RUN mkdir /storage

WORKDIR /src
COPY taqueria_bonjour /src/taqueria_bonjour

CMD ["waitress-serve", "--call", "taqueria_bonjour:main"]
