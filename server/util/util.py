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
    t = str_to_datetime_UTC(request.args.get('to', default='2100-12-31T00:00:00.000Z'))
    t = t + timedelta(days = 1)
    t = t - timedelta(microseconds = 1)
    return t