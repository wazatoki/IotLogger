from datetime import datetime

from flask import request, jsonify
import json

from infrastructure import flaskSetup
from repositories import asynchronous_log
from domain import asynchronous

app = flaskSetup.app

@app.route(flaskSetup.url_prefix + 'asynchronous/find_by_event_date', methods=['GET'])
def find_asynchronous_by_event_date():
    f = request.args.get('from', default='1900/1/1')
    t = request.args.get('to', default='2050/12/31')
    items = asynchronous_log.find_by_event_date(f, t)
    result_items = []
    for item in items:
        result_items.append(item.get_Data())

    return jsonify(result_items)

@app.route(flaskSetup.url_prefix + 'asynchronous/add', methods=['POST'])
def asynchronous_add():
    print(request.json)
    data = request.json
    log_data = asynchronous.Log_data()
    log_data.version = data['version']
    log_data.dt = datetime.strptime(data['dt'], '%Y/%m/%d %H:%M:%S')
    log_data.code = data['code']
    log_data.category = data['category']
    log_data.name = data['name']

    asynchronous_log.add(log_data)
    return jsonify({'result': 'ok'})