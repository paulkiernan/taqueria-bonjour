FROM python:3.9-alpine

COPY requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt

RUN mkdir /storage

WORKDIR /src
COPY . /src

CMD ["flask", "run", "--host=0.0.0.0"]
