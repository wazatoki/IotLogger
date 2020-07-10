<template>
  <div class="select-date">
    <el-select
      v-model="selectedDevice"
      v-on:change="deviceSelected"
      placeholder="Device Select"
      class="device-select"
    >
      <el-option v-for="item in devices" :key="item" :label="item" :value="item"></el-option>
    </el-select>
    <el-date-picker v-model="fromDate" v-on:change="fromDateChanged" type="date" placeholder="開始日"></el-date-picker>
    <span>〜</span>
    <el-date-picker v-model="toDate" v-on:change="toDateChanged" type="date" placeholder="終了日"></el-date-picker>
    <el-button type="primary" v-on:click="getData">データ取得</el-button>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "SelectDate",
  mounted: function() {
    this.fromDateChanged();
    this.toDateChanged();
  },
  props: {
    devices: Array
  },
  data() {
    return {
      selectedDevice: "",
      fromDate: this.getDefaultFromDate(),
      toDate: new Date(),
      parsedDataIntervalID: undefined,
      alertLogIntervalID: undefined,
      currentStateIntervalID: undefined
    };
  },
  methods: {
    fromDateChanged(){
      this.$emit("from-date-changed", this.fromDate);
    },
    toDateChanged(){
      this.$emit("to-date-changed", this.toDate);
    },
    deviceSelected() {
      this.$emit("selected-device-changed", this.selectedDevice);
    },
    getDefaultFromDate() {
      let d;
      d = new Date();
      d.setDate(d.getDate() - 2);
      return d;
    },
    getData() {
      this.fetchParcedData();
      this.fetchAsynchronousData();
      this.fetchCurrentState();
      let d;
      d = new Date();
      const self = this;
      if (
        // 最終日付が本日と同じ時だけデータの再取得を行う
        this.toDate.getFullYear() === d.getFullYear() &&
        this.toDate.getMonth() === d.getMonth() &&
        this.toDate.getDate() === d.getDate()
      ) {
        this.parsedDataIntervalID = setInterval(function() {
          self.fetchParcedData();
        }, 60000);
        this.alertLogIntervalID = setInterval(function() {
          self.fetchAsynchronousData();
        }, 5000);
        this.currentStateIntervalID = setInterval(function() {
          self.fetchCurrentState();
        }, 5000);
      } else {
        // データの再取得の停止。
        clearInterval(this.parsedDataIntervalID);
        clearInterval(this.alertLogIntervalID);
        clearInterval(this.currentStateIntervalID);
      }
    },
    fetchParcedData() {
      axios
        .get("api/find_parsed_by_event_date", {
          params: {
            from: this.fromDate,
            to: this.toDate,
            selectedDevice: this.selectedDevice
          }
        })
        .then(res => {
          this.$emit("parsed-data-fetched", res.data);
        });
    },
    fetchAsynchronousData() {
      axios
        .get("api/find_asynchronous_by_event_date", {
          params: {
            from: this.fromDate,
            to: this.toDate,
            selectedDevice: this.selectedDevice
          }
        })
        .then(res => {
          this.$emit("asynchronous-data-fetched", res.data);
        });
    },
    fetchCurrentState() {
      axios
        .get("api/find_cyclic_current_state", {
          params: {
            selectedDevice: this.selectedDevice
          }
        })
        .then(res => {
          this.$emit("current-state-fetched", res.data);
        });
    },
  }
};
</script>

<style scoped>
span {
  color: darkgray;
}
.device-select {
  margin-right: 2em;
}
</style>