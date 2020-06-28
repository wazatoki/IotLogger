from datetime import datetime

class Log_data:
    dt = datetime.strptime('1900/1/1 0:0:0', '%Y/%m/%d %H:%M:%S')
    device_id = '0000'
    item0_max = -32000
    item0_min = -32000
    item1_max = -32000
    item1_min = -32000
    item2_max = -32000
    item2_min = -32000
    item3_max = -32000
    item3_min = -32000
    item4_max = -32000
    item4_min = -32000
    item5_max = -32000
    item5_min = -32000
    item6_max = -32000
    item6_min = -32000
    item7_max = -32000
    item7_min = -32000
    item8_max = -32000
    item8_min = -32000
    item9_max = -32000
    item9_min = -32000
    
    def get_Data(self):

        return {
            "datetime": self.dt,
            "deviceID": self.device_id,
            "item0Max": self.item0_max,
            "item0Min": self.item0_min,
            "item1Max": self.item1_max,
            "item1Min": self.item1_min,
            "item2Max": self.item2_max,
            "item2Min": self.item2_min,
            "item3Max": self.item3_max,
            "item3Min": self.item3_min,
            "item4Max": self.item4_max,
            "item4Min": self.item4_min,
            "item5Max": self.item5_max,
            "item5Min": self.item5_min,
            "item6Max": self.item6_max,
            "item6Min": self.item6_min,
            "item7Max": self.item7_max,
            "item7Min": self.item7_min,
            "item8Max": self.item8_max,
            "item8Min": self.item8_min,
            "item9Max": self.item9_max,
            "item9Min": self.item9_min,
        }