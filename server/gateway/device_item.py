from flask import request, jsonify

from infrastructure import flaskSetup
from domain import device_item
from repositories import device_item as device_item_repo
from util import util

app = flaskSetup.app

@app.route(flaskSetup.url_prefix + 'find_device_items_by_deviceID', methods=['GET'])
def find_by_deviceID():
    results = []
    d = util.get_requested_selected_device()
    
    items = device_item_repo.find_by_deviceID(d)

    for item in items:
        results.append(item.get_Data())
    
    return jsonify(results)

@app.route(flaskSetup.url_prefix + 'device_item/save', methods=['POST'])
def device_item_save():
    data = request.json
    di_list = []

    for item in data:

        di = device_item.Device_item()

        for key in item:
            if key == 'id':
                di.column_id = item[key]
            elif key == 'deviceID':
                di.device_id = item[key]
            elif key == 'deviceItemID':
                di.device_item_id = item[key]
            elif key == 'name':
                di.name = item[key]
            elif key == 'unit':
                di.unit = item[key]

        di_list.append(di)

    device_item_repo.delete_by_deviceID(di.device_id)

    for o in di_list:
        device_item_repo.add(o)
    
    return jsonify({'result': 'ok'})