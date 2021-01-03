#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import random
from collections import Counter

from flask import request
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy_utils import PhoneNumber
from twilio.twiml.messaging_response import MessagingResponse
from twilio.twiml.voice_response import VoiceResponse

from taqueria_bonjour import app, db, twilio_client
from taqueria_bonjour.models import User
from taqueria_bonjour.helpers import _send_message


RESPONSE_COUNTER = Counter()
POTENTIAL_RESPONSES = [
    "Bonjour, {person}?",
    "Bonjour, {person}!",
    "Bonjour, {person}.",
    "Bonjour, {person}...",
    "¡Bonjour, {person}!",
    "¿Bonjour, {person}?",
    "¡Bonjour, {person}?",
    "¿Bonjour, {person}!",
    "#Bonjour, {person}",
    "∴Bonjour, {person}",
]
SPECIAL_RESPONSES = [
    "Pamplemousse, {person}!",
    "Sacre le bleu, {person}!",
]


@app.route("/", methods=["GET"])
def index():
    return "bonjour"


@app.route("/healthz", methods=["GET"])
def healthcheck():
    return "healthy"


@app.route("/sms", methods=["GET", "POST"])
def sms():

    number = request.form.get("From")
    responder = User.query.filter_by(phone_number=PhoneNumber(number, "US")).one()
    logging.info("Received message from: {0}".format(number))
    responder.responses += 1
    db.session.commit()

    resp = MessagingResponse()
    message = random.choice(
        SPECIAL_RESPONSES if responder.responses % 5 == 0 else POTENTIAL_RESPONSES
    )
    logging.info("That person is: {0}".format(responder.name))

    total_message = message.format(person=responder.name)
    if responder.name == "stranger":
        total_message += (
            "\n\nPS: Don't be a stranger! Sign up for the forthcoming radical new "
            "concept in food at http://www.taqueriabonjour.com"
        )
    logging.info("Response: {0}".format(total_message))
    resp.message(total_message)

    return str(resp)


@app.route("/bonjour", methods=["GET"])
def bonjour():
    for user in User.query.all():
        try:
            _send_message(twilio_client, user.name, user.phone_number.e164)
            user.sends += 1
        except Exception:
            logging.exception(
                f"Error sending message to {user.name} @ {user.phone_number.e164}"
            )
            user.delivery_errors += 1
    db.session.commit()
    return "Bonjours sent."


@app.route("/add", methods=["POST"])
def add():

    post_data = request.get_json()

    u = User(
        name=post_data["name"],
        phone_number=PhoneNumber(post_data["number"], post_data["code"].upper()),
    )
    db.session.add(u)

    try:
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        return {
            "message": "That name or number already exists!",
            "status": "error",
        }

    return {"message": f"Successfully added {u.name}!", "status": "success"}


@app.route("/team", methods=["GET"])
def team():
    return {
        "data": [user for user in User.query.all()],
    }


@app.route("/speak", methods=["POST"])
def speak():
    number = request.form.get("From")
    logging.info("Received voice call from: {0}".format(number))
    db.session.commit()

    try:
        user = User.query.filter_by(phone_number=PhoneNumber(number, "US")).one()
        user.responses += 1

        try:
            db.session.commit()
        except Exception:
            logging.exception("error committing response inc")

        name = user.name

    except NoResultFound:
        name = "stranger"

    response = VoiceResponse()
    response.say("Bonjour, {0}!".format(name))

    return str(response)
