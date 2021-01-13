<template>
  <div class="base-wrapper">
    <el-row>
      <el-col :span="2">
        <chart-select v-bind:deviceItems="deviceItems"></chart-select>
        <div class="clear"></div>
        <div class="master-maintenance-button">
          <span v-on:click="deviceMasterVisible = true">device マスター</span>
        </div>
        <div class="master-maintenance-button">
          <span v-on:click="onClickItemMaster">item マスター</span>
        </div>
        <div class="csv-download-button">
          <span v-on:click="onClickCsvDownload">CSV ダウンロード</span>
        </div>
      </el-col>
      <el-col :span="22">
        <el-row>
          <el-col :span="17">
            <select-date
              v-bind:devices="devices"
              v-on:parsed-data-fetched="setCyclicData"
              v-on:asynchronous-data-fetched="setAlertData"
              v-on:current-state-fetched="setCurrentState"
              v-on:from-date-changed="fromDateChanged"
              v-on:to-date-changed="toDateChanged"
              v-on:selected-device-changed="selectedDeviceChanged"
              v-on:device-message-fetched="setDeviceMessage"
            ></select-date>
          </el-col>
          <el-col :span="7">
            <span class="device-message">{{deviceMessage}}<span>
          </el-col>
        </el-row>
        <el-row>
          <el-col :span="17">
            <cyclic-logs
              v-bind:device="selectedDevice"
              v-bind:fromDate="fromDate"
              v-bind:toDate="toDate"
              v-bind:cyclickData="cyclickData"
              v-bind:currentState="currentState"
              v-bind:deviceItems="deviceItems"
            ></cyclic-logs>
          </el-col>
          <el-col :span="7">
            <alert-logs v-bind:alertData="alertData"></alert-logs>
          </el-col>
        </el-row>
      </el-col>
    </el-row>
    <el-dialog title="device マスターメンテナンス" :visible.sync="deviceMasterVisible" width="40%">
      <device-master v-on:device-data-saved="deviceDataSaved"></device-master>
      <span slot="footer" class="dialog-footer">
        <el-button @click="deviceMasterVisible = false">Cancel</el-button>
      </span>
    </el-dialog>
    <el-dialog title="item マスターメンテナンス" :visible.sync="itemMasterVisible" width="50%">
      <item-master :devices="devices" v-on:device-item-data-saved="deviceItemDataSaved"></item-master>
      <span slot="footer" class="dialog-footer">
        <el-button @click="itemMasterVisible = false">Cancel</el-button>
      </span>
    </el-dialog>
    <el-dialog title="CSV ダウンロード" :visible.sync="csvDownloadVisible" width="70%">
      <csv-download :devices="devices" :device="selectedDevice" :fromDate="fromDate" :toDate="toDate"></csv-download>
      <span slot="footer" class="dialog-footer">
        <el-button @click="csvDownloadVisible = false">Cancel</el-button>
      </span>
    </el-dialog>
  </div>
</template>

<script>
import axios from "axios";

import SelectDate from "./SelectDate";
import AlertLogs from "./AlertLogs";
import CyclicLogs from "./CyclicLogs";
import ChartSelect from "./ChartSelect";
import DeviceMaster from "./DeviceMaster";
import ItemMaster from "./ItemMaster";
import CsvDownload from "./CsvDownload.vue";

import DeviceItem from "../domain/DeviceItem";

export default {
  name: "BaseWrapper",
  components: {
    SelectDate,
    AlertLogs,
    CyclicLogs,
    ChartSelect,
    DeviceMaster,
    ItemMaster,
    CsvDownload
  },
  mounted: function() {
    this.fetchAllDevices();
  },
  data() {
    return {
      alertData: [],
      cyclickData: [],
      currentState: {},
      deviceItems: this.createDefaultDeviceItems(),
      selectedDevice: "",
      fromDate: Date,
      toDate: Date,
      devices: [],
      deviceMasterVisible: false,
      itemMasterVisible: false,
      csvDownloadVisible: false
    };
  },
  methods: {
    fetchDeviceItems() {
      axios
        .get("api/find_device_items_by_deviceID", {
          params: {
            selectedDevice: this.selectedDevice
          }
        })
        .then(res => {
          this.setDeviceItems(res.data);
        });
    },
    onClickCsvDownload() {
      this.fetchAllDevices();
      this.csvDownloadVisible = true;
    },
    onClickItemMaster() {
      this.fetchAllDevices();
      this.itemMasterVisible = true;
    },
    fetchAllDevices() {
      axios.get("api/find_all_devices").then(res => {
        if (res.data && res.data.length > 0) {
          this.devices = res.data;
        }
      });
    },
    deviceDataSaved() {
      this.fetchAllDevices();
      this.deviceMasterVisible = false;
      this.noticeMessage = "deviceデータの保存に成功しました。";
      this.noticeDialogVisible = true;
    },
    deviceItemDataSaved() {
      this.itemMasterVisible = false;
      this.noticeMessage = "itemデータの保存に成功しました。";
      this.noticeDialogVisible = true;
    },
    selectedDeviceChanged(val) {
      this.selectedDevice = val;
      this.fetchDeviceItems();
    },
    fromDateChanged(val) {
      this.fromDate = val;
    },
    toDateChanged(val) {
      this.toDate = val;
    },
    setCyclicData(data) {
      this.cyclickData = data;
    },
    setAlertData(data) {
      this.alertData = data;
    },
    setCurrentState(data) {
      if (data == null) {
        data = {};
      }
      this.currentState = data;
    },
    setDeviceItems(data) {
      this.deviceItems = [];
      data.forEach(item => {
        const deviceItem = new DeviceItem(
          item.id,
          item.deviceID,
          item.deviceItemID,
          item.name,
          item.unit
        );
        if (deviceItem.device_item_id) {
          this.deviceItems.push(deviceItem);
        }
      });
    },
    setDeviceMessage(data) {
      this.deviceMessage = data;
    },
    createDefaultDeviceItems() {
      const items = [];
      for (let index = 0; index < 10; index++) {
        const item = {
          column_id: "item" + index,
          device_id: "",
          device_item_id: "",
          name: "",
          unit: ""
        };
        items.push(item);
      }
      return items;
    }
  }
};
</script>

<style scoped>
div.select-chart {
  width: 7em;
  float: left;
  text-align: left;
}

div.clear {
  clear: both;
}

div.master-maintenance-button,
div.csv-download-button {
  margin-top: 3em;
}
</style>