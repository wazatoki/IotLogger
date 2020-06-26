import datetime
from pytz import timezone
import random

from flask import request, jsonify

from infrastructure import flaskSetup
from repositories import cyclic_log
from domain import cyclic_data
from util import util

app = flaskSetup.app

@app.route(flaskSetup.url_prefix + 'find_cyclic_current_state', methods=['GET'])
def find_cyclic_current_state():
    t = datetime.datetime.now(timezone('UTC'))
    f = t - datetime.timedelta(minutes = 5)
    d = util.get_requested_selected_device()

    item = cyclic_log.find_current_state(f, t, d)

    if item != None:
        item.dt = timezone('UTC').localize(item.dt)
        return jsonify(item.get_Data())

    return jsonify(None)



@app.route(flaskSetup.url_prefix + 'find_cyclic_by_event_date', methods=['GET'])
def find_cyclic_by_event_date():
    f = util.get_requested_from_datetime()
    t = util.get_requested_to_datetime()
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

    for k in data:

        if k == 'version':
            log_data.version = data[k]
        elif k == 'dt':
            log_data.dt = util.str_to_datetime_UTC(data[k])
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
        elif k == 'device_id':
            log_data.device_id = data[k]

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
    log_data.speed = 0
    log_data.flow = 0
    log_data.pven = 0
    log_data.pint = 0
    log_data.deltap = 0
    log_data.part=0
    log_data.tven=0
    log_data.tart=0
    log_data.svo2 =0
    log_data.hct =0
    log_data.device_id = device_id

    dataList.append(log_data)

    for i in range(1, 172800):
        print("create data:" + str(i))
        ld = cyclic_data.Log_data()
        base_date = base_date + datetime.timedelta(seconds=1)

        ld.version = 1
        ld.dt = base_date
        a = random.randint(-10,10)
        if dataList[i-1].speed + a < max or dataList[i-1].speed + a > min:
            ld.speed = dataList[i-1].speed + a
        else:
            ld.speed = dataList[i-1].speed
        
        a = random.randint(-10,10)
        if dataList[i-1].flow + a < max or dataList[i-1].flow + a > min:
            ld.flow = dataList[i-1].flow + a
        else:
            ld.flow = dataList[i-1].flow

        a = random.randint(-10,10)
        if dataList[i-1].pven + a < max or dataList[i-1].pven + a > min:
            ld.pven = dataList[i-1].pven + a
        else:
            ld.pven = dataList[i-1].pven

        a = random.randint(-10,10)
        if dataList[i-1].pint + a < max or dataList[i-1].pint + a > min:
            ld.pint = dataList[i-1].pint + a
        else:
            ld.pint = dataList[i-1].pint

        a = random.randint(-10,10)
        if dataList[i-1].deltap + a < max or dataList[i-1].deltap + a > min:
            ld.deltap = dataList[i-1].deltap + a
        else:
            ld.deltap = dataList[i-1].deltap

        a = random.randint(-10,10)
        if dataList[i-1].part + a < max or dataList[i-1].part + a > min:
            ld.part = dataList[i-1].part + a
        else:
            ld.part = dataList[i-1].part

        a = random.randint(-10,10)
        if dataList[i-1].tven + a < max or dataList[i-1].tven + a > min:
            ld.tven = dataList[i-1].tven + a
        else:
            ld.tven = dataList[i-1].tven

        a = random.randint(-10,10)
        if dataList[i-1].tart + a < max or dataList[i-1].tart + a > min:
            ld.tart = dataList[i-1].tart + a
        else:
            ld.tart = dataList[i-1].tart

        a = random.randint(-10,10)
        if dataList[i-1].svo2 + a < max or dataList[i-1].svo2 + a > min:
            ld.svo2 = dataList[i-1].svo2 + a
        else:
            ld.svo2 = dataList[i-1].svo2

        a = random.randint(-10,10)
        if dataList[i-1].hct + a < max or dataList[i-1].hct + a > min:
            ld.hct = dataList[i-1].hct + a
        else:
            ld.hct = dataList[i-1].hct

        ld.device_id = device_id
        
        dataList.append(ld)

    i = 0
    for d in dataList:
        print(i)    
        cyclic_log.add(d)
        i = i + 1
    print('finish')

