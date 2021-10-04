import os
import datetime
from pytz import timezone
import random

from flask import request, jsonify, make_response

from infrastructure import flaskSetup
from repositories import cyclic_log, device_item, parsed_log
from domain import cyclic_data
from util import util
from services import export_csv_data

app = flaskSetup.app

@app.route(flaskSetup.url_prefix + 'cyclic/delete', methods=['DELETE'])
def cyclic_delete():
    f = util.get_requested_from_datetime()
    t = util.get_requested_to_datetime()
    d = util.get_requested_selected_device()
    
    cyclic_log.delete_by_event_date(f, t, d)
    parsed_log.delete_by_event_date(f, t, d)
    return jsonify({ "result": True })

@app.route(flaskSetup.url_prefix + 'cyclic/csv/download', methods=['GET'])
def cyclic_csv_download():
    fname: str = util.get_requested_download_filename()
    now: datetime = datetime.datetime.now()
    download_fname: str = 'cyclic_data_{0:%Y%m%d%H%M%S}.csv'.format(now)
    temp_file_path: str = util.get_temp_dir_path() + fname
    response = make_response()
    response.data = open(temp_file_path, "rb").read()
    response.headers['Content-Disposition'] = 'attachment; filename=' + download_fname
    response.mimetype = 'text/csv'
    return response

@app.route(flaskSetup.url_prefix + 'cyclic/csv/filename', methods=['GET'])
def cyclic_csv_filename():
    f = util.get_requested_from_datetime()
    t = util.get_requested_to_datetime()
    d = util.get_requested_selected_device()
    
    items = cyclic_log.find_by_event_date(f, t, d)
    for item in items:
        item.dt = timezone('UTC').localize(item.dt).astimezone(timezone('Asia/Tokyo'))

    devices = device_item.find_by_deviceID(d)
    file_name = export_csv_data.output_cyclic_data(items, devices)

    return jsonify({ "fileName": file_name })

@app.route(flaskSetup.url_prefix + 'find_cyclic_current_state', methods=['GET'])
def find_cyclic_current_state():
    t = datetime.datetime.now(timezone('UTC'))
    f = t - datetime.timedelta(minutes = 60)
    d = util.get_requested_selected_device()

    item = cyclic_log.find_current_state(f, t, d)

    if item != None:
        item.dt = timezone('UTC').localize(item.dt)
        return jsonify(item.get_Data())

    return jsonify(None)



@app.route(flaskSetup.url_prefix + 'find_cyclic_by_event_date', methods=['GET'])
def find_cyclic_by_event_date():
    f = util.get_requested_from_datetime()
    t = util.get_requested_to_date()
    d = util.get_requested_selected_device()
    items = cyclic_log.find_by_event_date(f, t, d)
    result_items = []
    for item in items:
        item.dt = timezone('UTC').localize(item.dt)
        result_items.append(item.get_Data())
    return jsonify(result_items)


@app.route(flaskSetup.url_prefix + 'cyclic/add', methods=['POST'])
def cyclic_add():
    data = request.json
    log_data = cyclic_data.Log_data()

    deviceID = data['deviceID']

    device_items = device_item.find_by_deviceID(deviceID)

    for k in data:

        if k == 'version':
            log_data.version = data[k]
        elif k == 'datetime':
            log_data.dt = util.str_to_datetime_UTC(data[k])
        elif k == 'deviceID':
            log_data.device_id = data[k]
        else:
            columnID = ''

            for item in device_items:
                if k == item.device_item_id:
                    columnID = item.column_id
                    break
            
            if columnID == 'item0':
                log_data.item0 = data[k]
            elif columnID == 'item1':
                log_data.item1 = data[k]
            elif columnID == 'item2':
                log_data.item2 = data[k]
            elif columnID == 'item3':
                log_data.item3 = data[k]
            elif columnID == 'item4':
                log_data.item4 = data[k]
            elif columnID == 'item5':
                log_data.item5 = data[k]
            elif columnID == 'item6':
                log_data.item6 = data[k]
            elif columnID == 'item7':
                log_data.item7 = data[k]
            elif columnID == 'item8':
                log_data.item8 = data[k]
            elif columnID == 'item9':
                log_data.item9 = data[k]

    cyclic_log.add(log_data)

    return jsonify({'result': 'ok'})

@app.route(flaskSetup.url_prefix + 'cyclic/add/test1', methods=['POST'])
def cyclic_test_data_1_add():
    cyclic_test_data_add('test_device_id_1')

@app.route(flaskSetup.url_prefix + 'cyclic/add/test2', methods=['POST'])
def cyclic_test_data_2_add():
    cyclic_test_data_add('test_device_id_2')

def cyclic_test_data_add(device_id):
    print('start')
    dataList = []
    log_data = cyclic_data.Log_data()

    max = 100
    min = -100
    UTC = timezone('UTC')
    base_date = datetime.datetime.strptime('2020/1/1 0:0:0', '%Y/%m/%d %H:%M:%S').astimezone(UTC)
    log_data.version = 1
    log_data.dt = base_date
    log_data.device_id = device_id
    log_data.item0 = 0
    log_data.item1 = 0
    log_data.item2 = 0
    log_data.item3 = 0
    log_data.item4 = 0
    log_data.item5 = 0
    log_data.item6 = 0
    log_data.item7 = 0
    log_data.item8 = 0
    log_data.item9 = 0
    

    dataList.append(log_data)

    for i in range(1, 172800):
        print("create data:" + str(i))
        ld = cyclic_data.Log_data()
        base_date = base_date + datetime.timedelta(seconds=1)

        ld.version = 1
        ld.dt = base_date
        ld.device_id = device_id
        a = random.randint(-10,10)
        if dataList[i-1].item0 + a < max or dataList[i-1].item0 + a > min:
            ld.item0 = dataList[i-1].item0 + a
        else:
            ld.item0 = dataList[i-1].item0 - a
        
        a = random.randint(-10,10)
        if dataList[i-1].item1 + a < max or dataList[i-1].item1 + a > min:
            ld.item1 = dataList[i-1].item1 + a
        else:
            ld.item1 = dataList[i-1].item1 - a

        a = random.randint(-10,10)
        if dataList[i-1].item2 + a < max or dataList[i-1].item2 + a > min:
            ld.item2 = dataList[i-1].item2 + a
        else:
            ld.item2 = dataList[i-1].item2 - a

        a = random.randint(-10,10)
        if dataList[i-1].item3 + a < max or dataList[i-1].item3 + a > min:
            ld.item3 = dataList[i-1].item3 + a
        else:
            ld.item3 = dataList[i-1].item3 - a

        a = random.randint(-10,10)
        if dataList[i-1].item4 + a < max or dataList[i-1].item4 + a > min:
            ld.item4 = dataList[i-1].item4 + a
        else:
            ld.item4 = dataList[i-1].item4 - a

        a = random.randint(-10,10)
        if dataList[i-1].item5 + a < max or dataList[i-1].item5 + a > min:
            ld.item5 = dataList[i-1].item5 + a
        else:
            ld.item5 = dataList[i-1].item5 - a

        a = random.randint(-10,10)
        if dataList[i-1].item6 + a < max or dataList[i-1].item6 + a > min:
            ld.item6 = dataList[i-1].item6 + a
        else:
            ld.item6 = dataList[i-1].item6 - a

        a = random.randint(-10,10)
        if dataList[i-1].item7 + a < max or dataList[i-1].item7 + a > min:
            ld.item7 = dataList[i-1].item7 + a
        else:
            ld.item7 = dataList[i-1].item7 - a

        a = random.randint(-10,10)
        if dataList[i-1].item8 + a < max or dataList[i-1].item8 + a > min:
            ld.item8 = dataList[i-1].item8 + a
        else:
            ld.item8 = dataList[i-1].item8 - a

        a = random.randint(-10,10)
        if dataList[i-1].item9 + a < max or dataList[i-1].item9 + a > min:
            ld.item9 = dataList[i-1].item9 + a
        else:
            ld.item9 = dataList[i-1].item9 - a

        dataList.append(ld)

    i = 0
    for d in dataList:
        print(i)    
        cyclic_log.add(d)
        i = i + 1
    print('finish')
    
    return jsonify({'result': 'ok'})

