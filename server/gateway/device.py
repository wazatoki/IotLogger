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