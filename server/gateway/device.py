from flask import jsonify

from infrastructure import flaskSetup
from repositories import device

app = flaskSetup.app

@app.route(flaskSetup.url_prefix + 'find_all_devices', methods=['GET'])
def find_all():
    items = device.find_all_IDs()
    return jsonify(items)