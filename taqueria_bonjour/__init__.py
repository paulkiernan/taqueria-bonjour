#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from twilio.rest import Client as TwilioClient

from taqueria_bonjour.config import Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
twilio_client = TwilioClient(
    app.config["TWILIO_ACCOUNT_SID"], app.config["TWILIO_AUTH_TOKEN"]
)

from taqueria_bonjour import routes, models  # noqa


def main():
    return app


if __name__ == "__main__":
    main().run(host="0.0.0.0", debug=True)
