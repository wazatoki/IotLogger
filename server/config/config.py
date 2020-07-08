import os
import logging

# coding: utf-8
import configparser

# --------------------------------------------------
# configparserの宣言とiniファイルの読み込み
# --------------------------------------------------
config_ini = configparser.ConfigParser()
config_ini.read('config.ini', encoding='utf-8')
config_default = config_ini['default']

http_port = config_default.get('port')
temp_file_delete_time = config_default.get('temp_file_delete_time')
logging.basicConfig(filename= '.' + os.sep + 'log' + os.sep + 'logger.log')