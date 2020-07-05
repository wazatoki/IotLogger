from uuid import uuid4
from datetime import datetime, timezone, timedelta
from dateutil import parser

from flask import request

from util import util

def createUUID():
    return str(uuid4())+datetime.now().strftime('%Y%m%d%H%M%S%f')

def str_to_datetime_UTC(str_date):
    UTC = timezone(timedelta(hours=+0), 'UTC')
    t = parser.parse(str_date).astimezone(UTC)
    return t

def get_requested_from_datetime():
    f = str_to_datetime_UTC(request.args.get('from', default='1900-01-01T00:00:00.000Z'))
    return f

def get_requested_to_datetime():
    t = str_to_datetime_UTC(request.args.get('to', default='1900-01-01T00:00:00.000Z'))
    return t

def get_requested_to_date():
    t = str_to_datetime_UTC(request.args.get('to', default='2100-12-31T00:00:00.000Z'))
    t = t + timedelta(days = 1)
    t = t - timedelta(microseconds = 1)
    return t

def get_requested_selected_device():
    d = request.args.get('selectedDevice', default='')
    return d

def get_requested_download_filename():
    fname = request.args.get('filename', default='')
    return fname

def accessed_browser():

    http_user_agent = request.headers.get('User-Agent').lower()

    keywords = {
        'trident': 'IE11',
        'edge': 'Edge',
        'chrome': 'Chrome', 
        'opr': 'Opera', 
        'firefox': 'Firefox',
        'safari': 'safari'
    }
    for key, val in keywords.items():
        if http_user_agent.find(key) > -1:
            return val
    return 'othres'

def user_os():
    
    http_user_agent = request.headers.get('User-Agent').lower()

    keywords = {
        'nt 10.0': 'Windows 10',
        'mac': 'Mac', 
        'android': 'Android',
        'iphone': 'iPhone',
        'nt 6.1': 'Windows 7',
        'nt 5': 'Windows XP', 
        'linux': 'Linux'
    }
    for key, val in keywords.items():
        if http_user_agent.find(key) > -1:
            return val
    return 'othres'