import datetime
import dateutil.parser
import random

from flask import request, jsonify

from infrastructure import flaskSetup
from repositories import cyclic_log
from domain import cyclic_data

app = flaskSetup.app

@app.route(flaskSetup.url_prefix + 'find_cyclic_by_event_date', methods=['GET'])
def find_cyclic_by_event_date():
    f = dateutil.parser.parse(request.args.get('from', default='1900/1/1'))
    t = dateutil.parser.parse(request.args.get('to', default='2050/12/31'))
    t = t + datetime.timedelta(days = 1)
    t = t - datetime.timedelta(microseconds = 1)

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

@app.route(flaskSetup.url_prefix + 'cyclic/add/test', methods=['POST'])
def cyclic_test_data_add():
    print('start')
    dataList = []
    log_data = cyclic_data.Log_data()

    max = 100
    min = -100
    base_date = datetime.datetime.strptime('2020/1/1 0:0:0', '%Y/%m/%d %H:%M:%S')
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
      
        
        dataList.append(ld)

    i = 0
    for d in dataList:
        print(i)    
        cyclic_log.add(d)
        i = i + 1
    print('finish')

