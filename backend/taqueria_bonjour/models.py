#!/usr/bin/env python
# -*- coding: utf-8 -*-

from dataclasses import dataclass

from sqlalchemy_utils import PhoneNumber

from taqueria_bonjour import db


@dataclass
class User(db.Model):
    id: int
    name: str
    country_code: str
    sends: int
    responses: int
    delivery_errors: int
    deleted: bool

    __tablename__ = "users"

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.Unicode(255), index=True, unique=True)
    _phone_number = db.Column(db.Unicode(20), index=True, unique=True)
    country_code = db.Column(db.Unicode(8))

    sends = db.Column(db.Integer, default=0)
    responses = db.Column(db.Integer, default=0)
    delivery_errors = db.Column(db.Integer, default=0)
    deleted = db.Column(db.Boolean, default=False)

    phone_number = db.composite(PhoneNumber, _phone_number, country_code)
