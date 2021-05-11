FROM python:3.7-alpine as prereqs

ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
EXPOSE 5000

RUN apk add --no-cache gcc musl-dev linux-headers

COPY ./requirements.txt /
RUN pip install -r requirements.txt

FROM prereqs as development

COPY . /srv/app
WORKDIR /srv/app

CMD flask run
