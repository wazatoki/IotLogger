from uuid import uuid4
from datetime import datetime, timezone, timedelta
from dateutil import parser
import os

from flask import request

from util import util

def createUUID():
    return str(uuid4())+datetime.now().strftime('%Y%m%d%H%M%S%f')

def str_to_datetime_UTC(str_date):
    
    UTC = timezone(timedelta(hours=+0), 'UTC')

    if str_date == "":

        return datetime.now().astimezone(UTC)

    else:
        t = parser.parse(str_date).astimezone(UTC)
        return t

def get_requested_from_datetime():
    if request.method == 'GET':
        f = str_to_datetime_UTC(request.args.get('from', default='1900-01-01T00:00:00.000Z'))
    else:
        f = str_to_datetime_UTC(request.json['from'])
    return f

def get_requested_to_datetime():
    if request.method == 'GET':
        t = str_to_datetime_UTC(request.args.get('to', default='1900-01-01T00:00:00.000Z'))
    else:
        t = str_to_datetime_UTC(request.json['to'])
    return t

def get_requested_to_date():
    if request.method == 'GET':
        t = str_to_datetime_UTC(request.args.get('to', default='2100-12-31T00:00:00.000Z'))
    else:
        t = str_to_datetime_UTC(request.json['to'])
    
    t = t + timedelta(days = 1)
    t = t - timedelta(microseconds = 1)
    return t

def get_requested_selected_device():
    if request.method == 'GET':
        d = request.args.get('selectedDevice', default='')
    else:
        d = request.json['selectedDevice']
        
    return d

def get_requested_download_filename():
    if request.method == 'GET':
        fname = request.args.get('fileName', default='')
    else:
        fname = request.json['fileName']

    return fname

def get_temp_dir_path():
    return 'temp' + os.sep

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