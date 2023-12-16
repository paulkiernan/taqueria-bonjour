#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests

numbers = {
    "Paul": ("+16463696726", "US"),
}

if __name__ == "__main__":
    for _name, (_number, _code) in numbers.items():
        req = requests.post(
            "http://localhost:8080/add",
            json={
                "name": _name,
                "number": _number,
                "code": _code,
            },
        )
        print(req.text)
