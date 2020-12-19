#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sqlalchemy_utils import PhoneNumber

from taqueria_bonjour import db


class User(db.Model):

    __tablename__ = "user"

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.Unicode(255), index=True, unique=True)
    _phone_number = db.Column(db.Unicode(20), index=True, unique=True)
    country_code = db.Column(db.Unicode(8), default="US")
    sends = db.Column(db.Integer, default=0)
    responses = db.Column(db.Integer, default=0)

    phone_number = db.composite(PhoneNumber, _phone_number, country_code)

    def __repr__(self):
        return f"<User name:{self.name} phone_number:{self.phone_number.e164}>"
