# coding: utf-8
import json

import requests

class Base:

    headers = {
        'Authorization': 'token 43b53fa46441e3c88980e95840dfe8096443716de5f3048ff537605b1dc5aa73',
        'Content-Type': 'application/json'
    }

    @classmethod
    def fetch(cls, url, method, data=None):
        resp = getattr(requests, method.lower())(url, data=json.dumps(data), headers=cls.headers)
        return resp
