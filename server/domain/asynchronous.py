from datetime import datetime

class Log_data:
    version = 0
    dt = datetime.strptime('1900/1/1 0:0:0', '%Y/%m/%d %H:%M:%S')
    device_id = '0000'
    code = ''
    category = ''
    name = ''
    message_type = 'info'

    def get_Data(self):

        return {
            "version": self.version,
            "datetime": self.dt,
            "deviceID": self.device_id,
            "code": self.code,
            "category": self.category,
            "name": self.name,
            "messageType": self.message_type
        }
