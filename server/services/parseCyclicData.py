import datetime

from repositories import parsed_log, cyclic_log, device
from domain import parsed_data

INTERVAL_MINUTE = 5

def add_parsd_data():

    now = datetime.datetime.now()

    device_ids = device.find_all_IDs()

    for device_id in device_ids:
    
        base_date = cyclic_log.find_first_not_Parsed(device_id)
        
        if base_date != None:

            fdt = get_from_datetime(base_date.dt)
            tdt = get_to_datetime(fdt)
            print(now)
            print(fdt)
            print(tdt)
            if tdt < now :
                logs = cyclic_log.find_by_event_date(fdt, tdt, device_id)

                if len(logs) > 0:
                    pd = parsed_data.Log_data()
                    pd.device_id = logs[0].device_id
                    pd.dt = fdt
                    pd.speed_max = get_max_value(logs, 'speed')
                    pd.speed_min = get_min_value(logs, 'speed')
                    pd.flow_max = get_max_value(logs, 'flow')
                    pd.flow_min = get_min_value(logs, 'flow')
                    pd.pven_max = get_max_value(logs, 'pven')
                    pd.pven_min = get_min_value(logs, 'pven')
                    pd.pint_max = get_max_value(logs, 'pint')
                    pd.pint_min = get_min_value(logs, 'pint')
                    pd.deltap_max = get_max_value(logs, 'deltap')
                    pd.deltap_min = get_min_value(logs, 'deltap')
                    pd.part_max = get_max_value(logs, 'part')
                    pd.part_min = get_min_value(logs, 'part')
                    pd.tven_max = get_max_value(logs, 'tven')
                    pd.tven_min = get_min_value(logs, 'tven')
                    pd.tart_max = get_max_value(logs, 'tart')
                    pd.tart_min = get_min_value(logs, 'tart')
                    pd.svo2_max = get_max_value(logs, 'svo2')
                    pd.svo2_min = get_min_value(logs, 'svo2')
                    pd.hct_max = get_max_value(logs, 'hct')
                    pd.hct_min = get_min_value(logs, 'hct')

                    parsed_log.add(pd)
                    cyclic_log.mark_parsed_logs(fdt, tdt, device_id)
        
def get_max_value(items, key):

    v = 0
    for item in items:
        itemObj = item.get_Data()
        if v < itemObj[key] :
            v = itemObj[key]
    return v

def get_min_value(items, key):

    baseObj = items[0].get_Data()
    v = baseObj[key]
    for item in items:
        itemObj = item.get_Data()
        if v > itemObj[key] :
            v = itemObj[key]
    return v

def get_from_datetime(base_date):

    from_datetime = base_date.replace(minute=base_date.minute - base_date.minute % INTERVAL_MINUTE, second=0, microsecond=0)
    
    return from_datetime

def get_to_datetime(f):
    to_datetime = f + datetime.timedelta(minutes = INTERVAL_MINUTE)
    to_datetime = to_datetime - datetime.timedelta(microseconds = 1)

    return to_datetime
