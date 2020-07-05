<template>
  <div class="base-wrapper">
    <el-row>
      <el-col :span="24">
        <select-date
          v-on:parsed-data-fetched="setCyclicData"
          v-on:asynchronous-data-fetched="setAlertData"
          v-on:current-state-fetched="setCurrentState"
          v-on:device-items-fetched="setDeviceItems"
          v-on:from-date-changed="fromDateChanged"
          v-on:to-date-changed="toDateChanged"
          v-on:selected-device-changed="selectedDeviceChanged"
        ></select-date>
      </el-col>
    </el-row>
    <el-row>
      <el-col :span="18">
        <cyclic-logs
          v-bind:device="selectedDevice"
          v-bind:fromDate="fromDate"
          v-bind:toDate="toDate"
          v-bind:cyclickData="cyclickData"
          v-bind:currentState="currentState"
          v-bind:deviceItems="deviceItems"
        ></cyclic-logs>
      </el-col>
      <el-col :span="6">
        <alert-logs v-bind:alertData="alertData"></alert-logs>
      </el-col>
    </el-row>
  </div>
</template>

<script>
import SelectDate from "./SelectDate";
import AlertLogs from "./AlertLogs";
import CyclicLogs from "./CyclicLogs";
export default {
  name: "BaseWrapper",
  components: {
    SelectDate,
    AlertLogs,
    CyclicLogs
  },
  data() {
    return {
      alertData: [],
      cyclickData: [],
      currentState: {},
      deviceItems: this.createDefaultDeviceItems(),
      selectedDevice: '',
      fromDate: Date,
      toDate: Date
    };
  },
  methods: {
    selectedDeviceChanged(val) {
      this.selectedDevice = val;
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
      if(data){
        this.deviceItems = data;
      }else{
        this.deviceItems = this.createDefaultDeviceItems();
      }
      
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