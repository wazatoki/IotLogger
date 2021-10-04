import datetime
from pytz import timezone

from repositories import parsed_log, cyclic_log, device
from domain import parsed_data

INTERVAL_MINUTE = 5

def fetch_items(f, t, device_id):

    n = 200
    items = parsed_log.find_by_event_date(f, t, device_id)
    items_count = len(items)
    incremental = int(items_count / n) + 1
    r_items = []

    i = 0
    while i < items_count:

        pd = parsed_data.Log_data()
        pd.device_id = device_id
        pd.dt = items[i].dt
        pd.item0_max = items[i].item0_max
        pd.item0_min = items[i].item0_min
        pd.item1_max = items[i].item1_max
        pd.item1_min = items[i].item1_min
        pd.item2_max = items[i].item2_max
        pd.item2_min = items[i].item2_min
        pd.item3_max = items[i].item3_max
        pd.item3_min = items[i].item3_min
        pd.item4_max = items[i].item4_max
        pd.item4_min = items[i].item4_min
        pd.item5_max = items[i].item5_max
        pd.item5_min = items[i].item5_min
        pd.item6_max = items[i].item6_max
        pd.item6_min = items[i].item6_min
        pd.item7_max = items[i].item7_max
        pd.item7_min = items[i].item7_min
        pd.item8_max = items[i].item8_max
        pd.item8_min = items[i].item8_min
        pd.item9_max = items[i].item9_max
        pd.item9_min = items[i].item9_min
        j = 1
        while j < incremental and (i + j) < items_count:

            if pd.item0_max < items[i+j].item0_max:
                 pd.item0_max = items[i+j].item0_max
            if pd.item0_min > items[i+j].item0_min:
                 pd.item0_min = items[i+j].item0_min
            if pd.item1_max < items[i+j].item1_max:
                 pd.item1_max = items[i+j].item1_max
            if pd.item1_min > items[i+j].item1_min:
                 pd.item1_min = items[i+j].item1_min
            if pd.item2_max < items[i+j].item2_max:
                 pd.item2_max = items[i+j].item2_max
            if pd.item2_min > items[i+j].item2_min:
                 pd.item2_min = items[i+j].item2_min
            if pd.item3_max < items[i+j].item3_max:
                 pd.item3_max = items[i+j].item3_max
            if pd.item3_min > items[i+j].item3_min:
                 pd.item3_min = items[i+j].item3_min
            if pd.item4_max < items[i+j].item4_max:
                 pd.item4_max = items[i+j].item4_max
            if pd.item4_min > items[i+j].item4_min:
                 pd.item4_min = items[i+j].item4_min
            if pd.item5_max < items[i+j].item5_max:
                 pd.item5_max = items[i+j].item5_max
            if pd.item5_min > items[i+j].item5_min:
                 pd.item5_min = items[i+j].item5_min
            if pd.item6_max < items[i+j].item6_max:
                 pd.item6_max = items[i+j].item6_max
            if pd.item6_min > items[i+j].item6_min:
                 pd.item6_min = items[i+j].item6_min
            if pd.item7_max < items[i+j].item7_max:
                 pd.item7_max = items[i+j].item7_max
            if pd.item7_min > items[i+j].item7_min:
                 pd.item7_min = items[i+j].item7_min
            if pd.item8_max < items[i+j].item8_max:
                 pd.item8_max = items[i+j].item8_max
            if pd.item8_min > items[i+j].item8_min:
                 pd.item8_min = items[i+j].item8_min
            if pd.item9_max < items[i+j].item9_max:
                 pd.item9_max = items[i+j].item9_max
            if pd.item9_min > items[i+j].item9_min:
                 pd.item9_min = items[i+j].item9_min

            j += 1

        r_items.append(pd)

        i += incremental

    return r_items
    
def add_parsd_data():

    now = datetime.datetime.now(timezone('UTC'))

    device_ids = device.find_all_IDs()

    for device_id in device_ids:
    
        base_date = cyclic_log.find_first_not_Parsed(device_id)
        
        if base_date != None:

            utc_dt = timezone('UTC').localize(base_date.dt)
            fdt = get_from_datetime(utc_dt)
            tdt = get_to_datetime(fdt)
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
