class Device_item:
    column_id = ''
    device_id = ''
    device_item_id = ''
    name = ''
    unit = ''

    def get_Data(self):
        return {
            "id": self.column_id,
            "deviceID": self.device_id,
            "deviceItemID": self.device_item_id,
            "name": self.name,
            "unit": self.unit
        }