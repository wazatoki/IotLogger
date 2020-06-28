from flask import request, jsonify

from infrastructure import flaskSetup
from repositories import device

app = flaskSetup.app

@app.route(flaskSetup.url_prefix + 'find_all_devices', methods=['GET'])
def find_all():
    items = device.find_all_IDs()
    return jsonify(items)

@app.route(flaskSetup.url_prefix + 'device/save', methods=['POST'])
def device_save():
    data = request.json

    device.delete_all()
    for id in data:
        device.add(id)

    return jsonify({'result': 'ok'})

@app.route(flaskSetup.url_prefix + 'device/add/test1', methods=['POST'])
def device_test_data_1_add():
    device.add('test_device_id_1')
    device.add('test_device_id_2')

    return jsonify({'result': 'ok'})