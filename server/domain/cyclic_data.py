from datetime import datetime

class Log_data:
    version = 0
    dt = datetime.strptime('1900/1/1 0:0:0', '%Y/%m/%d %H:%M:%S')
    device_id = '0000'
    item0 = -32000
    item1 = -32000
    item2 = -32000
    item3 = -32000
    item4 = -32000
    item5 = -32000
    item6 = -32000
    item7 = -32000
    item8 = -32000
    item9 = -32000
    
    
    def get_Data(self):

        return {
            "version": self.version,
            "datetime": self.dt,
            "deviceID": self.device_id,
            "item0": self.item0,
            "item1": self.item1,
            "item2": self.item2,
            "item3": self.item3,
            "item4": self.item4,
            "item5": self.item5,
            "item6": self.item6,
            "item7": self.item7,
            "item8": self.item8,
            "item9": self.item9,
            
        }