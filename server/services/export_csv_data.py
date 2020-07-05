import os
import glob
import time
from util import util
import csv
import logging

def output_asynchronous_data(asynchronous_log_data, device_items):

    remove_temp_dir()

    file_name = util.createUUID()
    file_path  = util.get_temp_dir_path() + file_name
    os_name = util.user_os()
    encoding = ''
    lineterminator = ''

    if os_name.find('Windows') > -1:
        encoding = 'cp932'
        lineterminator = '\r\n'
    else:
        encoding = 'utf-8'
        lineterminator = '\n'

    try:
        with open(file_path, 'w', encoding) as file:
            writer = csv.writer(file, lineterminator)
            create_asynchronous_header(writer)
            create_asynchronous_data(asynchronous_log_data, writer)

    except (FileNotFoundError, csv.Error) as e:
        file_name = ''
        raise e

    finally:
        file.close()
        return file_name


def output_cyclic_data(cyclic_log_data, device_items):

    remove_temp_dir()

    file_name = util.createUUID()
    file_path  = util.get_temp_dir_path() + file_name
    os_name = util.user_os()
    encoding = ''
    lineterminator = ''

    if os_name.find('Windows') > -1:
        encoding = 'cp932'
        lineterminator = '\r\n'
    else:
        encoding = 'utf-8'
        lineterminator = '\n'

    try:
        with open(file_path, 'w', encoding=encoding) as csvfile:
            writer = csv.writer(csvfile, lineterminator=lineterminator)
            create_cyclic_header(device_items, writer)
            create_cyclic_data(cyclic_log_data, device_items, writer)

    except (FileNotFoundError, csv.Error) as e:
        file_name = ''
        raise e

    finally:
        return file_name

def create_asynchronous_data(asynchronous_log_data, writer):

    for row_data in asynchronous_log_data:

        writer.writerow([row_data.dt.strftime('%Y%m%d %H:%M:%S'), row_data.code, row_data.category , row_data.name])

def create_asynchronous_header(writer):

        writer.writerow(['datetime', 'code', 'category', 'name'])

def create_cyclic_data(cyclic_log_data, device_items, writer):

    for row_data in cyclic_log_data:

        row = []
        log_dic = row_data.get_Data()

        row.append(log_dic['datetime'].strftime('%Y%m%d %H:%M:%S'))

        for item in device_items:
            
            row.append(log_dic[item.column_id])

        writer.writerow(row)

def create_cyclic_header(device_items, writer):
    
    row = []

    row.append('date')

    for item in device_items:

        row.append(item.name)

    writer.writerow(row)
        
def remove_temp_dir():

    files = glob.glob(util.get_temp_dir_path() + '*')
    now = time.time()

    for f in files:
        st = os.stat(f)
        # １時間以上前に作成されたファイルを削除
        if st.st_atime < (now - 3600):
            try:
                os.remove(f)
            except OSError as e:
                logging.info('can not remove file : ' + f)
