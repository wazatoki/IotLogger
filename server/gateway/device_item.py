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

@app.route(flaskSetup.url_prefix + 'device_item/add/test1', methods=['POST'])
def device_item_test_data_1_add():
    
    di = device_item.Device_item()
    di.column_id = 'item0'
    di.device_id = 'test_device_id_1'
    di.device_item_id = 'speed'
    di.name = 'speed'
    di.unit = ''
    device_item_repo.add(di)
    di.column_id = 'item1'
    di.device_item_id = 'flow'
    di.name = 'flow'
    device_item_repo.add(di)
    di.column_id = 'item2'
    di.device_item_id = 'pven'
    di.name = 'pven'
    device_item_repo.add(di)
    di.column_id = 'item3'
    di.device_item_id = 'pint'
    di.name = 'pint'
    device_item_repo.add(di)
    di.column_id = 'item4'
    di.device_item_id = 'deltap'
    di.name = '⊿p'
    device_item_repo.add(di)
    di.column_id = 'item5'
    di.device_item_id = 'part'
    di.name = 'part'
    device_item_repo.add(di)
    di.column_id = 'item6'
    di.device_item_id = 'tven'
    di.name = 'tven'
    device_item_repo.add(di)
    di.column_id = 'item7'
    di.device_item_id = 'tart'
    di.name = 'tart'
    device_item_repo.add(di)
    di.column_id = 'item8'
    di.device_item_id = 'svo2'
    di.name = 'svo2'
    device_item_repo.add(di)
    di.column_id = 'item9'
    di.device_item_id = 'hct'
    di.name = 'hct'
    device_item_repo.add(di)

    return jsonify({'result': 'ok'})