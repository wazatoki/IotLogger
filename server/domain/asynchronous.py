from datetime import datetime

class Log_data:
    version = 0
    dt = datetime.strptime('1900/1/1 0:0:0', '%Y/%m/%d %H:%M:%S')
    code = ''
    category = ''
    name = ''
    device_id = '0000'

    def get_Data(self):

        return {
            "version": self.version,
            "datetime": self.dt,
            "code": self.code,
            "category": self.category,
            "name": self.name,
            "deviceID": self.device_id,
        }

index = [
    {"code": "1000", "category": "P-Ven", "name": "OK"},
    {"code": "1001", "category": "P-Ven", "name": "Over upper warning limit"},
    {"code": "1002", "category": "P-Ven", "name": "Under lower warning limit"},
    {"code": "1003", "category": "P-Ven", "name": "Over upper alarm limit"},
    {"code": "1004", "category": "P-Ven", "name": "Under lower alarm limit"},
    {"code": "1005", "category": "P-Ven", "name": "Over upper stop limit"},
    {"code": "1006", "category": "P-Ven", "name": "Under lower stop limit"},
    {"code": "1008", "category": "P-Ven", "name": "Disconnected"},
    {"code": "1009", "category": "P-Ven", "name": "Out of range"},
    {"code": "100A", "category": "P-Ven", "name": "Defect"},
    {"code": "2000", "category": "P-Int", "name": "OK"},
    {"code": "2001", "category": "P-Int", "name": "Over upper warning limit"},
    {"code": "2002", "category": "P-Int", "name": "Under lower warning limit"},
    {"code": "2003", "category": "P-Int", "name": "Over upper alarm limit"},
    {"code": "2004", "category": "P-Int", "name": "Under lower alarm limit"},
    {"code": "2005", "category": "P-Int", "name": "Over upper stop limit"},
    {"code": "2006", "category": "P-Int", "name": "Under lower stop limit"},
    {"code": "2008", "category": "P-Int", "name": "Disconnected"},
    {"code": "2009", "category": "P-Int", "name": "Out of range"},
    {"code": "200A", "category": "P-Int", "name": "Defect"},
    {"code": "3000", "category": "P-Art", "name": "OK"},
    {"code": "3001", "category": "P-Art", "name": "Over upper warning limit"},
    {"code": "3002", "category": "P-Art", "name": "Under lower warning limit"},
    {"code": "3003", "category": "P-Art", "name": "Over upper alarm limit"},
    {"code": "3004", "category": "P-Art", "name": "Under lower alarm limit"},
    {"code": "3005", "category": "P-Art", "name": "Over upper stop limit"},
    {"code": "3006", "category": "P-Art", "name": "Under lower stop limit"},
    {"code": "3008", "category": "P-Art", "name": "Disconnected"},
    {"code": "3009", "category": "P-Art", "name": "Out of range"},
    {"code": "300A", "category": "P-Art", "name": "Defect"},
    {"code": "4000", "category": "P-Aux", "name": "OK"},
    {"code": "4001", "category": "P-Aux", "name": "Over upper warning limit"},
    {"code": "4002", "category": "P-Aux", "name": "Under lower warning limit"},
    {"code": "4003", "category": "P-Aux", "name": "Over upper alarm limit"},
    {"code": "4004", "category": "P-Aux", "name": "Under lower alarm limit"},
    {"code": "4005", "category": "P-Aux", "name": "Over upper stop limit"},
    {"code": "4006", "category": "P-Aux", "name": "Under lower stop limit"},
    {"code": "4008", "category": "P-Aux", "name": "Disconnected"},
    {"code": "4009", "category": "P-Aux", "name": "Out of range"},
    {"code": "400A", "category": "P-Aux", "name": "Defect"},
    {"code": "5000", "category": "⊿P", "name": "OK"},
    {"code": "5001", "category": "⊿P", "name": "Over warning limit"},
    {"code": "5002", "category": "⊿P", "name": "Under warning limit"},
    {"code": "5004", "category": "P-Aux", "name": "Out of range"},
    {"code": "6000", "category": "Flow", "name": "OK"},
    {"code": "6001", "category": "Flow", "name": "Over warning limit"},
    {"code": "6002", "category": "Flow", "name": "Under warning limit"},
    {"code": "6005", "category": "Flow", "name": "Over stop limit"},
    {"code": "6006", "category": "Flow", "name": "Under stop limit"},
    {"code": "6008", "category": "Flow", "name": "Disconnected"},
    {"code": "6009", "category": "Flow", "name": "Out of range"},
    {"code": "600A", "category": "Flow", "name": "Defect"},
    {"code": "600B", "category": "Flow", "name": "Negative"},
    {"code": "600C", "category": "Flow", "name": "Temperature too high"},
    {"code": "600D", "category": "Flow", "name": "Amplitude too small"},
    {"code": "600E", "category": "Flow", "name": "Offset too high"},
    {"code": "600F", "category": "Flow", "name": "Wrong calibration"},
    {"code": "7000", "category": "T-Ven", "name": "OK"},
    {"code": "7001", "category": "T-Ven", "name": "Over warning limit"},
    {"code": "7002", "category": "T-Ven", "name": "Under warning limit"},
    {"code": "7004", "category": "T-Ven", "name": "Disconnected"},
    {"code": "7005", "category": "T-Ven", "name": "Out of range"},
    {"code": "7006", "category": "T-Ven", "name": "Defect"},
    {"code": "8000", "category": "T-Art", "name": "OK"},
    {"code": "8001", "category": "T-Art", "name": "Over warning limit"},
    {"code": "8002", "category": "T-Art", "name": "Under warning limit"},
    {"code": "8004", "category": "T-Art", "name": "Disconnected"},
    {"code": "8005", "category": "T-Art", "name": "Out of range"},
    {"code": "8006", "category": "T-Art", "name": "Defect"},
    {"code": "9000", "category": "SvO2", "name": "OK"},
    {"code": "9001", "category": "SvO2", "name": "Over warning limit"},
    {"code": "9002", "category": "SvO2", "name": "Under warning limit"},
    {"code": "9003", "category": "SvO2", "name": "Out of range"},
    {"code": "9004", "category": "SvO2", "name": "Defect"},
    {"code": "9006", "category": "SvO2", "name": "Disconnected"},
    {"code": "A000", "category": "Bubble", "name": "OK"},
    {"code": "A001", "category": "Bubble", "name": "Bubble detected without intervention"},
    {"code": "A002", "category": "Bubble", "name": "Bubble detected with intervention"},
    {"code": "A003", "category": "Bubble", "name": "Disconnected"},
    {"code": "A004", "category": "Bubble", "name": "Out of range"},
    {"code": "A005", "category": "Bubble", "name": "Defect"},
    {"code": "A008", "category": "Bubble", "name": "Reset"},
    {"code": "C000", "category": "Level", "name": "OK"},
    {"code": "C001", "category": "Level", "name": "Level detected without intervention"},
    {"code": "C002", "category": "Level", "name": "Level detected with intervention"},
    {"code": "C003", "category": "Level", "name": "Disconnected"},
    {"code": "C004", "category": "Level", "name": "Out of range"},
    {"code": "C005", "category": "Level", "name": "Defect"},
    {"code": "D000", "category": "Speed(RPM)", "name": "OK"},
    {"code": "D001", "category": "Speed(RPM)", "name": "Over warning limit"},
    {"code": "D002", "category": "Speed(RPM)", "name": "Under warning limit"},
    {"code": "D003", "category": "Speed(RPM)", "name": "Over stop limit"},
    {"code": "D004", "category": "Speed(RPM)", "name": "Under stop limit"},
    {"code": "D007", "category": "Speed(RPM)", "name": "Out of range"},
    {"code": "D00C", "category": "Pump status", "name": "Running"},
    {"code": "D00D", "category": "Pump status", "name": "Stopped"},
    {"code": "E000", "category": "Hct", "name": "OK"},
    {"code": "E001", "category": "Hct", "name": "Over warning limit"},
    {"code": "E002", "category": "Hct", "name": "Under warning limit"},
    {"code": "E003", "category": "Hct", "name": "Out of range"},
    {"code": "E004", "category": "Hct", "name": "Defect"},
    {"code": "E005", "category": "Hct", "name": "Disconnected"},
    {"code": "F000", "category": "Hb", "name": "OK"},
    {"code": "F001", "category": "Hb", "name": "Over warning limit"},
    {"code": "F002", "category": "Hb", "name": "Under warning limit"},
    {"code": "F003", "category": "Hb", "name": "Out of range"},
    {"code": "F004", "category": "Hb", "name": "Defect"},
    {"code": "F005", "category": "Hb", "name": "Disconnected"},
    {"code": "F006", "category": "Hb", "name": "Limit changed"},
]