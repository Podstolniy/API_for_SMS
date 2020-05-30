import json
import re

import requests
from requests import ConnectTimeout
from requests.exceptions import ProxyError
import common
from common import LogicError
phone = "79306051080"
session = 'https://api.grab.com/grabid/v1/oauth2/otp'
from bs4 import BeautifulSoup

def try_register_phone(phone, session: requests.Session):
    try:
        r=requests.post(session,
        timeout=20,
        headers={'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0',
        'Accept': 'text/html, application/xhtml+xml, application/xml;q=0.9, */*;q=0.8',
        'Accept-Language': 'ru-RU, ru;q=0.9, en-US;q=0.8, en;q=0.7, fr;q=0.6',},

        data={'client_id': "4da4649307cc4bfaa16b08d03432535e",
        'country_code': "RU",
        'method': "SMS",
        'num_digits': 6,
        'phone_number': "{}".format(phone),}
        )
    except ConnectTimeout:
        raise ProxyError()
    except json.JSONDecodeError:
        raise LogicError('unexpected answer: %d' % r.status_code)

try_register_phone(phone,session)
#print(r)
#soup1 = BeautifulSoup(r.text, 'html.parser')
#print(soup1)
