export default class DeviceItem {
    constructor(column_id = '', device_id = '', device_item_id = '', name = '', unit = '') {
        this.column_id = column_id
        this.device_id = device_id
        this.device_item_id = device_item_id
        this.name = name
        this.unit = unit
        this.isVisible = true
    }
}