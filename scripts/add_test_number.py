#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests

if __name__ == "__main__":

    req = requests.post(
        "http://localhost:8080/add",
        data={
            "name": "Paul",
            "number": "+16463696726",
        },
    )

    print(req.text)
