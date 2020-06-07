import datetime

from flask import request, jsonify

from infrastructure import flaskSetup
from repositories import cyclic_log
from domain import cyclic_data

app = flaskSetup.app

@app.route(flaskSetup.url_prefix + 'find_cyclic_by_event_date', methods=['GET'])
def find_cyclic_by_event_date():
    f = request.args.get('from', default='1900/1/1')
    t = request.args.get('to', default='2050/12/31')
    t = t + datetime.timedelta(days = 1)
    t = t- datetime.timedelta(microseconds = 1)
    items = cyclic_log.find_by_event_date(f, t)
    result_items = []
    for item in items:
        result_items.append(item.get_Data())

    return jsonify(result_items)


@app.route(flaskSetup.url_prefix + 'cyclic/add', methods=['POST'])
def cyclic_add():
    data = request.json
    log_data = cyclic_data.Log_data()

    for k in data:

        if k == 'version':
            log_data.version = data[k]
        elif k == 'dt':
            log_data.dt = datetime.datetime.strptime(data[k], '%Y/%m/%d %H:%M:%S')
        elif k == 'speed':
            log_data.speed = data[k]
        elif k == 'flow':
            log_data.flow = data[k]
        elif k == 'pven':
            log_data.pven = data[k]
        elif k == 'pint':
            log_data.pint = data[k]
        elif k == 'deltap':
            log_data.deltap = data[k]
        elif k == 'part':
            log_data.part = data[k]
        elif k == 'tven':
            log_data.tven = data[k]
        elif k == 'tart':
            log_data.tart = data[k]
        elif k == 'svo2':
            log_data.svo2 = data[k]
        elif k == 'hct':
            log_data.hct = data[k]

    cyclic_log.add(log_data)

    return jsonify({'result': 'ok'})