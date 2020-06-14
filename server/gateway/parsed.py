from pytz import timezone

from flask import jsonify

from infrastructure import flaskSetup
from repositories import parsed_log
from util import util

app = flaskSetup.app

@app.route(flaskSetup.url_prefix + 'find_parsed_by_event_date', methods=['GET'])
def find_parsed_by_event_date():
    f = util.get_requested_from_datetime()
    t = util.get_requested_to_datetime()
    items = parsed_log.find_by_event_date(f, t)
    result_items = []
    for item in items:
        item.dt = timezone('UTC').localize(item.dt)
        result_items.append(item.get_Data())

    return jsonify(result_items)