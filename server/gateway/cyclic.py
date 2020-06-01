from flask import request, jsonify

from infrastructure import flaskSetup
from repositories import cyclic_log
from domain import cyclic_data

app = flaskSetup.app

@app.route(flaskSetup.url_prefix + 'find_cyclic_by_event_date', methods=['GET'])
def find_cyclic_by_event_date():
    f = request.args.get('from', default='1900/1/1')
    t = request.args.get('to', default='2050/12/31')
    items = cyclic_log.find_by_event_date(f, t)
    result_items = []
    for item in items:
        result_items.append(item.get_Data())

    return jsonify(result_items)


@app.route(flaskSetup.url_prefix + 'cyclic/add', methods=['POST'])
def add():
    data = request.json
    log_data = cyclic_data.Log_data()
    log_data.version = data['version']
    log_data.dt = data['dt']
    log_data.speed = data['speed']
    log_data.flow = data['flow']
    log_data.pven = data['pven']
    log_data.pint = data['pint']
    log_data.deltap = data['deltap']
    log_data.part = data['part']
    log_data.tven = data['tven']
    log_data.tart = data['tart']
    log_data.svo2 = data['svo2']
    log_data.hct = data['hct']
    cyclic_log.add(log_data)
    
    return jsonify({'result', 'ok'})