from datetime import datetime

class Log_data:
    dt = datetime.strptime('1900/1/1 0:0:0', '%Y/%m/%d %H:%M:%S')
    speed_max = -32000
    speed_min = -32000
    flow_max = -32000
    flow_min = -32000
    pven_max = -32000
    pven_min = -32000
    pint_max = -32000
    pint_min = -32000
    deltap_max = -32000
    deltap_min = -32000
    part_max = -32000
    part_min = -32000
    tven_max = -32000
    tven_min = -32000
    tart_max = -32000
    tart_min = -32000
    svo2_max = -32000
    svo2_min = -32000
    hct_max = -32000
    hct_min = -32000
    device_id = '0000'
    
    def get_Data(self):

        return {
            "datetime": self.dt,
            "speedMax": self.speed_max,
            "speedMin": self.speed_min,
            "flowMax": self.flow_max,
            "flowMin": self.flow_min,
            "pvenMax": self.pven_max,
            "pvenMin": self.pven_min,
            "pintMax": self.pint_max,
            "pintMin": self.pint_min,
            "deltapMax": self.deltap_max,
            "deltapMin": self.deltap_min,
            "partMax": self.part_max,
            "partMin": self.part_min,
            "tvenMax": self.tven_max,
            "tvenMin": self.tven_min,
            "tartMax": self.tart_max,
            "tartMin": self.tart_min,
            "svo2Max": self.svo2_max,
            "svo2Min": self.svo2_min,
            "hctMax": self.hct_max,
            "hctMin": self.hct_min,
            "deviceID": self.device_id,
        }