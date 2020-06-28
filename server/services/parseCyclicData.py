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
                    pd.item0_max = get_max_value(logs, 'item0')
                    pd.item0_min = get_min_value(logs, 'item0')
                    pd.item1_max = get_max_value(logs, 'item1')
                    pd.item1_min = get_min_value(logs, 'item1')
                    pd.item2_max = get_max_value(logs, 'item2')
                    pd.item2_min = get_min_value(logs, 'item2')
                    pd.item3_max = get_max_value(logs, 'item3')
                    pd.item3_min = get_min_value(logs, 'item3')
                    pd.item4_max = get_max_value(logs, 'item4')
                    pd.item4_min = get_min_value(logs, 'item4')
                    pd.item5_max = get_max_value(logs, 'item5')
                    pd.item5_min = get_min_value(logs, 'item5')
                    pd.item6_max = get_max_value(logs, 'item6')
                    pd.item6_min = get_min_value(logs, 'item6')
                    pd.item7_max = get_max_value(logs, 'item7')
                    pd.item7_min = get_min_value(logs, 'item7')
                    pd.item8_max = get_max_value(logs, 'item8')
                    pd.item8_min = get_min_value(logs, 'item8')
                    pd.item9_max = get_max_value(logs, 'item9')
                    pd.item9_min = get_min_value(logs, 'item9')

                    parsed_log.add(pd)
                    cyclic_log.mark_parsed_logs(fdt, tdt, device_id)
        
def get_max_value(items, key):

    baseObj = items[0].get_Data()
    v = baseObj[key]
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
