from pytz import timezone
import datetime
import os

from flask import request, jsonify, make_response

from infrastructure import flaskSetup
from repositories import asynchronous_log, device_item
from domain import asynchronous
from util import util
from services import export_csv_data

app = flaskSetup.app

@app.route(flaskSetup.url_prefix + 'asynchronous/delete', methods=['DELETE'])
def asynchronous_delete():
    f = util.get_requested_from_datetime()
    t = util.get_requested_to_datetime()
    d = util.get_requested_selected_device()
    asynchronous_log.delete_by_event_date(f, t, d)
    
    return jsonify({ "result": True })

@app.route(flaskSetup.url_prefix + 'asynchronous/csv/download', methods=['GET'])
def asynchronous_csv_download():
    fname: str = util.get_requested_download_filename()
    now: datetime = datetime.datetime.now()
    download_fname: str = 'asynchronous_{0:%Y%m%d%H%M%S}.csv'.format(now)
    temp_file_path = util.get_temp_dir_path() + fname
    response = make_response()
    response.data = open(temp_file_path, "rb").read()
    response.headers['Content-Disposition'] = 'attachment; filename=' + download_fname
    response.mimetype = 'text/csv'
    return response

@app.route(flaskSetup.url_prefix + 'asynchronous/csv/filename', methods=['GET'])
def asynchronous_csv_filename():
    f = util.get_requested_from_datetime()
    t = util.get_requested_to_datetime()
    d = util.get_requested_selected_device()
    items = asynchronous_log.find_by_event_date(f, t, d)
    for item in items:
        item.dt = timezone('UTC').localize(item.dt).astimezone(timezone('Asia/Tokyo'))

    file_name = export_csv_data.output_asynchronous_data(items)
    return jsonify({ "fileName": file_name })

@app.route(flaskSetup.url_prefix + 'find_asynchronous_by_event_date', methods=['GET'])
def find_asynchronous_by_event_date():
    f = util.get_requested_from_datetime()
    t = util.get_requested_to_date()
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
        elif k == 'datetime':
            log_data.dt = util.str_to_datetime_UTC(data[k])
        elif k == 'code':
            log_data.code = data[k]
        elif k == 'category':
            log_data.category = data[k]
        elif k == 'name':
            log_data.name = data[k]
        elif k == 'messageType':
            log_data.message_type = data[k]
        elif k == 'deviceID':
            log_data.device_id = data[k]

    asynchronous_log.add(log_data)
    return jsonify({'result': 'ok'})