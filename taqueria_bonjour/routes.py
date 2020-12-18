#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import logging
import random
from collections import Counter

from flask import request
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy_utils import PhoneNumber
from twilio.twiml.messaging_response import MessagingResponse
from twilio.twiml.voice_response import VoiceResponse

from taqueria_bonjour import app, db, twilio_client
from taqueria_bonjour.models import User
from taqueria_bonjour.helpers import _send_message


RESPONSE_COUNTER = Counter()
POTENTIAL_RESPONSES = [
    'Bonjour, {person}?',
    'Bonjour, {person}!',
    'Bonjour, {person}.',
    'Bonjour, {person}...',
    '¡Bonjour, {person}!',
    '¿Bonjour, {person}?',
    '¡Bonjour, {person}?',
    '¿Bonjour, {person}!',
    '#Bonjour, {person}',
    '∴Bonjour, {person}',
]
SPECIAL_RESPONSES = [
    'Pamplemousse, {person}!',
    'Sacre le bleu, {person}!',
]


@app.route('/', methods=['GET'])
def index():
    return 'Bonjour'


@app.route('/sms', methods=['GET', 'POST'])
def sms():

    number = request.form.get('From')
    responder = User.query.filter_by(phone_number=PhoneNumber(number, 'US')).one()
    logging.info("Received message from: {0}".format(number))
    responder.responses += 1
    db.session.commit()

    resp = MessagingResponse()
    message = random.choice(
        SPECIAL_RESPONSES
        if responder.responses % 5 == 0
        else POTENTIAL_RESPONSES
    )
    logging.info("That person is: {0}".format(responder.name))

    total_message = message.format(person=responder.name)
    if responder.name == 'stranger':
        total_message += (
            "\n\nPS: Don't be a stranger! Sign up for the forthcoming radical new "
            "concept in food at http://www.taqueriabonjour.com"
        )
    logging.info("Response: {0}".format(total_message))
    resp.message(total_message)

    return str(resp)


@app.route('/bonjour', methods=['GET'])
def meow():
    for user in User.query.all():
        _send_message(twilio_client, user.name, user.phone_number.e164)
    return 'Bonjours sent.'


@app.route('/add', methods=['POST'])
def add():
    name = request.form['name']
    phone_number = request.form['number']
    code = request.form.get('code', 'US')

    u = User(
        name=name,
        phone_number=PhoneNumber(phone_number, code)
    )
    db.session.add(u)
    db.session.commit()

    return {
        "msg": f"Added {u}",
        "status": "ok"
    }


@app.route('/team', methods=['GET'])
def team():
    return json.dumps([
        {
            'id': user.id,
            'name': user.name,
            'phone_number': user.phone_number.e164
        }
        for user in User.query.all()
    ])


@app.route('/speak', methods=['POST'])
def speak():
    number = request.form.get('From')
    response = VoiceResponse()
    try:
        name = User.query.filter_by(phone_number=PhoneNumber(number, 'US')).one().name
    except NoResultFound:
        name = "stranger"
    response.say("Bonjour, {0}!".format(name))
    return str(response)
