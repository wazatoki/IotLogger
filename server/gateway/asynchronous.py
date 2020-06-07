from datetime import datetime
import dateutil.parser

from flask import request, jsonify
import json

from infrastructure import flaskSetup
from repositories import asynchronous_log
from domain import asynchronous

app = flaskSetup.app

@app.route(flaskSetup.url_prefix + 'asynchronous/find_by_event_date', methods=['GET'])
def find_asynchronous_by_event_date():
    f = dateutil.parser.parse(request.args.get('from', default='1900/1/1'))
    t = dateutil.parser.parse(request.args.get('to', default='2050/12/31'))
    t = t + datetime.timedelta(days = 1)
    t = t- datetime.timedelta(microseconds = 1)
    items = asynchronous_log.find_by_event_date(f, t)
    result_items = []
    for item in items:
        result_items.append(item.get_Data())

    return jsonify(result_items)

@app.route(flaskSetup.url_prefix + 'asynchronous/add', methods=['POST'])
def asynchronous_add():
    data = request.json
    log_data = asynchronous.Log_data()

    for k in data:

        if k == 'version':
            log_data.version = data[k]
        elif k == 'dt':
            log_data.dt = datetime.strptime(data[k], '%Y/%m/%d %H:%M:%S')
        elif k == 'code':
            log_data.code = data[k]
        elif k == 'category':
            log_data.category = data[k]
        elif k == 'name':
            log_data.name = data[k]

    asynchronous_log.add(log_data)
    return jsonify({'result': 'ok'})