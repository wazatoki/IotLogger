<template>
  <div class="csv-download">
    <div>
      <el-select v-model="selectedDevice" placeholder="Device Select" class="device-select">
        <el-option v-for="item in devices" :key="item" :label="item" :value="item"></el-option>
      </el-select>
    </div>
    <div>
      <el-radio v-model="selectedDataType" label="cyclic">Cyclic Data</el-radio>
      <el-radio v-model="selectedDataType" label="asynchronous">Asynchronous Data</el-radio>
    </div>
    <el-date-picker v-model="fromDateTime" type="datetime" placeholder="開始日時"></el-date-picker>
    <span>〜</span>
    <el-date-picker v-model="toDateTime" type="datetime" placeholder="終了日時"></el-date-picker>
    <el-button type="primary" v-on:click="getData">データ取得</el-button>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "csvDownload",
  props: {
    device: String,
    devices: Array,
    fromDate: Date,
    toDate: Date
  },
  mounted: function() {
    this.selectedDevice = this.device;
    this.fromDateTime = this.fromDate;
    this.toDateTime = this.toDate;
  },
  watch: {
    device: function(val) {
      this.selectedDevice = val;
    },
    fromDate: function(val) {
      this.fromDateTime = val;
    },
    toDate: function(val) {
      this.toDateTime = val;
    }
  },
  data() {
    return {
      selectedDevice: "",
      selectedDataType: "cyclic",
      fromDateTime: "",
      toDateTime: ""
    };
  },
  methods: {
    getData() {
      switch (this.selectedDataType) {
        case "cyclic":
          this.fetchCyclicData();
          break;
        case "asynchronous":
          this.fetchAsynchronousData();
          break;

        default:
          this.fetchCyclicData();
          break;
      }
    },
    fetchAllDevices() {
      axios.get("api/find_all_devices").then(res => {
        if (res.data && res.data.length > 0) {
          this.options = res.data;
        }
      });
    },
    fetchAsynchronousData() {
      axios
        .get("api/asynchronous/csv/filename", {
          params: {
            from: this.fromDateTime,
            to: this.toDateTime,
            selectedDevice: this.selectedDevice
          }
        })
        .then(res => {
          window.location.href =
            window.location.protocol +
            "//" +
            window.location.host +
            "/api/asynchronous/csv/download?fileName=" +
            res.data.fileName;
        });
    },
    fetchCyclicData() {
      axios
        .get("api/cyclic/csv/filename", {
          params: {
            from: this.fromDateTime,
            to: this.toDateTime,
            selectedDevice: this.selectedDevice
          }
        })
        .then(res => {
          window.location.href =
            window.location.protocol +
            "//" +
            window.location.host +
            "/api/cyclic/csv/download?fileName=" +
            res.data.fileName;
        });
    }
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