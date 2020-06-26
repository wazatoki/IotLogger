from pytz import timezone

from flask import request, jsonify

from infrastructure import flaskSetup
from repositories import asynchronous_log
from domain import asynchronous
from util import util

app = flaskSetup.app

@app.route(flaskSetup.url_prefix + 'find_asynchronous_by_event_date', methods=['GET'])
def find_asynchronous_by_event_date():
    f = util.get_requested_from_datetime()
    t = util.get_requested_to_datetime()
    d = util.get_requested_selected_device()
    items = asynchronous_log.find_by_event_date(f, t, d)
    result_items = []
    for item in items:
        item.dt = timezone('UTC').localize(item.dt)
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
            log_data.dt = util.str_to_datetime_UTC(data[k])
        elif k == 'code':
            log_data.code = data[k]
        elif k == 'category':
            log_data.category = data[k]
        elif k == 'name':
            log_data.name = data[k]
        elif k == 'device_id':
            log_data.device_id = data[k]

    asynchronous_log.add(log_data)
    return jsonify({'result': 'ok'})