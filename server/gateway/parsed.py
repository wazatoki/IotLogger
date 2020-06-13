import datetime
import dateutil.parser

from flask import request, jsonify

from infrastructure import flaskSetup
from repositories import parsed_log

app = flaskSetup.app

@app.route(flaskSetup.url_prefix + 'find_parsed_by_event_date', methods=['GET'])
def find_parsed_by_event_date():
    f = dateutil.parser.parse(request.args.get('from', default='1900/1/1'))
    t = dateutil.parser.parse(request.args.get('to', default='2050/12/31'))
    t = t + datetime.timedelta(days = 1)
    t = t - datetime.timedelta(microseconds = 1)
    items = parsed_log.find_by_event_date(f, t)
    result_items = []
    for item in items:
        result_items.append(item.get_Data())

    return jsonify(result_items)