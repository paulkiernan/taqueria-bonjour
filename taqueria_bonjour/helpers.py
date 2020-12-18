#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging

from taqueria_bonjour import app


def _send_message(twilio_client, name, number):
    _msg = "Bonjour, {0}!".format(name)
    print(_msg)
    logging.info(_msg)
    twilio_client.api.account.messages.create(
        to=number,
        from_=app.conf["TWILIO_ORIGIN_NUMBER"],
        body=_msg,
        # media_url='https://www.gannett-cdn.com/-mm-/392f5ecaf14a53bc35fd090a5e028b2d8df329ad/c=0-197-3869-2383&r=x803&c=1600x800/local/-/media/2015/11/17/FortMyers/FortMyers/635833579420916211-turkey.jpg'
    )
    return _msg
