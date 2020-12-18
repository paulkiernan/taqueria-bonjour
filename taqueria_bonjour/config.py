#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os


class Config(object):

    # SQLite
    if os.environ.get('DATABASE_URL'):
        SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    else:
        SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(
            os.path.abspath(os.path.dirname(__file__)),
            'taco.db'
        )
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Twilio Auth
    TWILIO_ACCOUNT_SID = os.environ['TWILIO_ACCOUNT_SID']
    TWILIO_AUTH_TOKEN = os.environ['TWILIO_AUTH_TOKEN']
    TWILIO_ORIGIN_NUMBER = os.environ['TWILIO_ORIGIN_NUMBER']
